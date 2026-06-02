import re

# https://www.mjt.me.uk/posts/falsehoods-programmers-believe-about-addresses/

# Simple address regex for: Addr# Street Name, City, State ZIP code
# "^(\\d{1,}) [a-zA-Z0-9\\s]+(\\,)? [a-zA-Z]+(\\,)? [A-Z]{2} [0-9]{5,6}$"

STREET_ADDRESS_RE = re.compile(r'\d{1,4} [\w\s]{1,20}(?:street|st|avenue|ave|road|rd|highway|hwy|lane|ln|square|sq|trail|trl|drive|dr|court|ct|park|parkway|pkwy|circle|cir|boulevard|blvd)\W?(?=\s|$)', re.IGNORECASE)

USA_ZIP_CODE_RE = re.compile(r'\b\d{5}(?:[-\s]\d{4})?\b')

USA_STATE_RE = re.compile(r'\bA[LKSZRAP] | C[AOT] | D[EC] | F[LM] | G[AU] | HI | I[ADL N] | K[SY] | LA | M[ADEHINOPST] | N[CDEHJMVY] | O[HKR] | P[ARW] | RI | S[CD] | T[NX] | UT | V[AIT] | W[AIVY]\b', re.IGNORECASE)

def find_postal_addresses(text):
    addresses = []
    lines = text.split("\n")

    for i, line in enumerate(lines):
        #print("LINE :", line)
        address_match_count = 0
        stripped = line.strip()
        if not stripped or len(stripped) < 5:
            continue
        if STREET_ADDRESS_RE.search(stripped):
            #print("STREET_ADDRESS_RE match", stripped)
            address_match_count += 1
        if USA_STATE_RE.search(stripped):
            #print("STATE_RE match", stripped)
            address_match_count += 1
        if USA_ZIP_CODE_RE.search(stripped):
            #print("ZIP_CODE_RE match", stripped)
            address_match_count += 1
        if address_match_count > 1:
            addresses.append(stripped)
    return addresses

