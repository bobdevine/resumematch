import re

# email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# email = re.findall(r"([^@|\s]+@[^@]+\.[^@|\s]+)", text)
# EMAIL_RE = re.compile( r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")

#EMAIL_RE   = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

EMAIL_RE = re.compile(
    r"([a-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)")

def find_email_addresses(text):
    addresses = []
    lines = text.split("\n")

    for i, line in enumerate(lines):
        #print("LINE :", line)
        address_match_count = 0
        stripped = line.strip()
        if not stripped or len(stripped) < 5:
            continue
        if matched := EMAIL_RE.search(stripped):
            #print("EMAIL_RE match", matched.group())
            addresses.append(matched.group())
    return addresses

