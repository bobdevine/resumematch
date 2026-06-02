#

import re


# Detect resume boundary
# "Dummy Resume 2", "Name: Xyz", or a line that looks like a new header
RESUME_BOUNDARY_RE = re.compile(
    r"^(?:dummy\s+resume|resume\s*\d|---+|===+)\s*\d*\s*$",
    re.IGNORECASE
)

NEW_PERSON_HEADER_RE = re.compile(
    r"^Name\s*:\s*.+",
    re.IGNORECASE
)

def is_resume_boundary(line, prev_sections):
    stripped = line.strip()
    if RESUME_BOUNDARY_RE.match(stripped):
        return True
    # "Name: Xyz" appearing AFTER we've already parsed sections = new resume 
    if NEW_PERSON_HEADER_RE.match(stripped) and len(prev_sections) > 2:
        return True 
    return False


# Common resume section headers
SECTION_PATTERNS = [
    ("summary", re.compile(
        r"(summary|profile|objective)\s*",
        re.IGNORECASE
    )),
    ("education", re.compile(
        r"^(?:education(al)?|academic|\s+(?:background|qualification|details))\s*:?\s*$",
        re.IGNORECASE
    )),
    ("work_experience", re.compile(
        r"^(?:work|professional|employment|career)?\s+(?:experience|history|background)|(?:experience|internship)\s*:?\s*$",
        re.IGNORECASE
    )),
    ("skills", re.compile(
        r"^(?:skills(?:\s+(?:&|and)\s+(?:competencies|expertise|tools))?|(?:technologies|tech\s+stack|tools?)\s*(?:&|and)?\s*technologies)\s*:?\s*$",
        re.IGNORECASE
    )),
    ("certifications", re.compile(
        r"^(?:certifications?|licenses?(?:\s*(?:&|and)\s*certifications?)?|professional\s+certifications?|accreditations?)\s*:?\s*$",
        re.IGNORECASE
    )),
    ("projects", re.compile(
        r"^(?:(?:key|major|personal|academic|notable)\s+)?projects?\s*:?\s*$",
        re.IGNORECASE
    )),
    ("awards", re.compile(
        r"^(?:awards?|honors?)(?:\s*(?:&|and)\s*(?:awards?|honors?))?\s*:?\s*$",
        re.IGNORECASE
    )),
    ("languages", re.compile(
        r"^(?:languages?\s*(?:known|spoken|proficiency)?)\s*:?\s*$",
        re.IGNORECASE
    )),
    ("interests", re.compile(
        r"^(?:interests?|hobbies?|extra[\s-]?curricular(?:\s+activities)?)\s*:?\s*$",
        re.IGNORECASE
    )),
    ("references", re.compile(
        r"^(?:references?)\s*:?\s*$",
        re.IGNORECASE
    )),
    ("activities", re.compile(
        r"^(?:activities|extra[\s-]?curricular|volunteer(?:ing)?|community)\s*:?\s*$",
        re.IGNORECASE
    )),
]

OTHER_SECTION_PATTERNS = {
    'projects': r'(?i)(projects|portfolio|works|achievements)',
    'publications': r'(?i)(publications|papers|research)',
    'awards': r'(?i)(awards|honors|recognition)'
}


#################################
def detect_sections(text, resume_sections):
    lines = text.split("\n")
    sections = {}
    current_section = "header"
    current_lines = []
    detected_sections = []

    # internal consistency check
    for section_name, pattern in SECTION_PATTERNS:
        if section_name not in resume_sections:
            print("INTERNAL ERROR -- section", section_name)    
                    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            # keep a blank line
            current_lines.append("")
            continue

        #print("detect_sections() SECTION:", current_section, "LINE:", stripped)

        # Check for multi-resume boundary - stop parsing
        if is_resume_boundary(stripped, detected_sections):
            #print("RESUME BOUNDARY")
            if current_lines or current_section != "header":
                sections[current_section] = "\n".join(current_lines).strip()
            break
            
        new_section = None
        for section_name, pattern in SECTION_PATTERNS:
            if pattern.match(stripped):
                #print("detect_sections() SECTION CURRENT:", current_section, "MATCHED:", section_name, "PATTERN", pattern, "STRIPPED", stripped)
                new_section = section_name
                break

        if new_section:
            if current_lines or current_section != "header":
                sections[current_section] = "\n".join(current_lines).strip()
                detected_sections.append(current_section)
            current_section = new_section
            current_lines = []
        else:
            #print("APPEND", current_section, stripped)
            current_lines.append(stripped)

    return sections


def zzz():
    # Detect inline headers like "SKILLS:" with content after
    if len(stripped) < 60:
        for section_name, pattern in SECTION_PATTERNS:
            header_match = re.match(
                r"^(" + pattern.pattern.lstrip("^").rstrip(r"\s*:?\s*$") + r")\s*[:\-–—]\s*(.+)$",
                stripped, re.IGNORECASE
            )
            if header_match:
                matched_section = section_name
                print("detect_sections() HEADER:", section_name, "//", stripped)
                remaining = header_match.group(2).strip() if header_match.lastindex >= 2 else ""
                if current_lines or current_section != "header":
                    sections[current_section] = "\n".join(current_lines).strip()
                    detected_sections.append(current_section)
                current_section = matched_section
                current_lines = [remaining] if remaining else []
                matched_section = None
                break
