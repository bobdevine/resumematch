import re

MONTH_NAMES = r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"
    
DATE_RANGE_RE = re.compile(
    rf"({MONTH_NAMES}[\s,.']*\d{{2,4}}|\d{{1,2}}[/\-.]?\d{{2,4}}|\d{{4}})"
    r"\s*[\-–—]+\s*"
    rf"({MONTH_NAMES}[\s,.']*\d{{2,4}}|\d{{1,2}}[/\-.]?\d{{2,4}}|\d{{4}}|Present|Current|Till\s*(?:Date|Now|Present))",
    re.IGNORECASE
)

GITHUB_RE  = re.compile(r"github\.com/[\w\-]+", re.IGNORECASE)
LINKEDIN_RE= re.compile(r"linkedin\.com/in/[\w\-]+", re.IGNORECASE)
    
WORK_TITLE_RE = re.compile(
    r"(?:"
    r"(?:senior|junior|lead|principal|staff|chief|head|associate|assistant|deputy|vice|managing|executive)?\s*" 
    r"(?:software|web|full[\s\-]?stack|front[\s\-]?end|back[\s\-]?end|mobile|cloud|data|ml|ai|devops|qa|test|ui/?ux|product|project|program|business|system|network|database|security|solutions?)?\s*"
    r"(?:engineer|developer|architect|analyst|manager|consultant|designer|administrator|specialist|coordinator|director|officer|scientist|researcher|tester|lead|trainee)"
    r"|Intern(?:ship)?"
    r"|founder|advisor|consultant"
    r"|artist|musician|actor|dancer"
    r"|journalist|writer|editor"
    r"|CTO|CEO|CFO|COO|CIO|VP|SVP|AVP"
    r")",
    re.IGNORECASE
)

"""
photographer
videographer
actor
dancer
model
journalist
writer
editor
translator
interpreter
librarian
researcher
professor
lecturer
academic advisor
counselor
therapist
psychologist
social worker
police officer
firefighter
paramedic
soldier
pilot
flight attendant
driver
farmer
entrepreneur
business owner
investor
accountant
banker
economist
financial advisor
insurance agent
actuary
statistician
mathematician
physicist
astronomer
biologist
chemist
geologist
meteorologist
pharmacist
physician
nurse
dentist
dietitian
nutritionist
pharmacist
veterinarian
psychiatrist
psychologist
therapist
"""

COMPANY_SUFFIXES = re.compile(
    r"\b(?:Inc\.?|LLC|Ltd\.?|Pvt\.?|Private|Limited|Corp(?:oration)?\.?|Co\.?|Group|Technologies|Tech|Solutions|Services|Consulting|Systems|Software|Labs?|Global|International)\b",
    re.IGNORECASE
)

BULLET_STARTS = ("•", "-", "●", "▪", "◦", "*", "→", "–")

USA_ZIP_CODE_RE = re.compile(r'\b\d{5}(?:[-\s]\d{4})?\b')

# USA_STATE_RE = re.compile(r'\bA[LKSZRAP] | C[AOT] | D[EC] | F[LM] | G[AU] | HI | I[ADL N] | K[SY] | LA | M[ADEHINOPST] | N[CDEHJMVY] | O[HKR] | P[ARW] | RI | S[CD] | T[NX] | UT | V[AIT] | W[AIVY]\b')

US_STATES = [
    "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA",
    "KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ",
    "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT",
    "VA","WA","WV","WI","WY","DC"
]

COUNTRY_RE = re.compile(
    r"\b(?:India|USA|United States|United Kingdom|UK|Canada|Australia|Germany|Singapore|UAE|Dubai)\b",
    re.IGNORECASE
)

CITY_NAME_PATTERN = r'^[A-Za-z]+(?:[\s\-][A-Za-z]+)*$'

#-----------------------

def new_job_entry():
    return {
        "company": None,
        "title": None,
        "startDate": None,
        "endDate": None,
        "location": None,
        "description": None,
    }


def find_jobs(section_text):
    lines = section_text.split("\n")
    entries = []
    entry = None
    in_description = False

    for line in lines:
        #print("find_jobs() LINE:", line)
        line = line.strip()
        if not line:
            # if empty line, assume end of entry
            in_description = False
            if entry:
                entries.append(entry)
                entry = None
            continue

        if not entry:
            entry = new_job_entry()
            
        if has_date := DATE_RANGE_RE.search(line):
            #print("DATE LINE:", line)
            if entry["startDate"]:
                entries.append(entry)
                entry = new_job_entry()
            else:
                entry["startDate"] = has_date.group(1).strip()
                entry["endDate"] = has_date.group(2).strip()
        elif line.startswith(BULLET_STARTS) or bool(re.match(r"^\d+[\.—\)]\s", line)):
            cleaned = re.sub(r"^[\s•●▪◦\-\*→–—]+\s*", "", line).strip()
            if cleaned:
                if entry["description"]:
                    entry["description"] += "\n" + cleaned
                else:
                    entry["description"] = cleaned
        else:
            #print("LINE:", line)
            # try splitting to extract a field
            parts = re.split(r"\s*[,;\|—]\s*", line)
            for idx, part in enumerate(parts):
                #print("PART :", part)
                part = part.strip()
                if WORK_TITLE_RE.search(part) and not entry["title"]:
                    #print(" -TITLE :", part)
                    entry["title"] = part
                elif COMPANY_SUFFIXES.search(part) and not entry["company"]:
                    #print(" -COMPANY :", part)
                    entry["company"] = part
                elif idx > 0 and (part in US_STATES or COUNTRY_RE.match(part) or re.match(CITY_NAME_PATTERN, part) or USA_ZIP_CODE_RE.match(part)):
                    #print("-LOC", part)
                    if entry["location"]:
                        entry["location"] += ', '
                        entry["location"] += part
                    else:
                        entry["location"] = part
                elif idx == 0 and not entry["company"]:
                    # HACK, assume the first part is the company name
                    #print(" -0 :", part)
                    entry["company"] = part
            if entry["description"]:
                entry["description"] += "\n" + line
            else:
                entry["description"] = line

    if entry:
        entries.append(entry)
    return entries
