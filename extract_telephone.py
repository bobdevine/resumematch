import re

#PHONE_RE = re.compile(r"[\+]?\d[\d\s\-\(\)\.]{6,}")
#PHONE_RE   = re.compile(r"(\+?\d[\d\s\-().]{7,}\d)")

X_PHONE_RE = re.compile(
    r"(?:\+?\d{1,3}[\s\-.]?)?"
    r"(?:\(?\d{2,5}\)?[\s\-.]?)?"
    r"\d{3,5}[\s\-.]?\d{3,5}"
    r"(?:\s*(?:ext|x|extension)\.?\s*\d{1,5})?"
)

# phone_pattern = r'\b(?:\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b|\(\d{3}\)\s*\d{3}[-.\s]??\d{4}\b|\d{4}[-.\s]??\d{3}[-.\s]??\d{4}\b)'

# num_regex = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)
#                [-\.\s]*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'

PHONE_RE = re.compile(
    r'((?:(?<![\d-])(?:\+?\d{1,3}[-.\s*]?)?'
    r'(?:\(?\d{3}\)?[-.\s*]?)?\d{3}[-.\s*]?'
    r'\d{4}(?![\d-]))|(?:(?<![\d-])(?:(?:\(\+?\d{2}\))|(?:\+?\d{2}))\s*'
    r'\d{2}\s*\d{3}\s*\d{4}(?![\d-])))'
)
PHONE_WITH_EXT_RE = re.compile(
    r'((?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*(?:[2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|(?:[2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?(?:[2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?(?:[0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(?:\d+)?))'
)

def find_telephone_numbers(text):
    phone_numbers = []
    lines = text.split("\n")

    for i, line in enumerate(lines):
        #print("LINE :", line)
        stripped = line.strip()
        if not stripped or len(stripped) < 6:
            continue
        
        if matched := PHONE_WITH_EXT_RE.search(stripped):
            #print("PNONE_WITH_EXT_RE match", stripped)
            phone_numbers.append(matched.group())
        elif matched := PHONE_RE.search(stripped):
            #print("PHONE_RE match", stripped)
            phone_numbers.append(matched.group())
    return phone_numbers
