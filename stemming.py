import sys

import re

STEP2LIST = {
    "ational": "ate",
    "tional": "tion",
    "enci": "ence",
    "anci": "ance",
    "izer": "ize",
    "bli": "ble",
    "alli": "al",
    "entli": "ent",
    "eli": "e",
    "ousli": "ous",
    "ization": "ize",
    "ation": "ate",
    "ator": "ate",
    "alism": "al",
    "iveness": "ive",
    "fulness": "ful",
    "ousness": "ous",
    "aliti": "al",
    "iviti": "ive",
    "biliti": "ble",
    "logi": "log",          
}

STEP3LIST = {
    "icate": "ic",
    "ative": "",
    "alize": "al",
    "iciti": "ic",
    "ical": "ic",
    "ful": "",
    "ness": "",          
}

_CONS = "[^aeiou]"
#con_re = re.compile("[bcdfghjklmnpqrstvwxyz]")
_VOWEL = "[aeiouy]"
_CONS_SEQ = "[^aeiouy]+"
_VOWEL_SEQ = "[aeiou]+"

_m_gr0 = re.compile("^(" + _CONS_SEQ + ")?" + _VOWEL_SEQ + _CONS_SEQ)
_meq1 = re.compile("^(" + _CONS_SEQ + ")?" + _VOWEL_SEQ + _CONS_SEQ + "(" + _VOWEL_SEQ + ")?$")
_m_gr1 = re.compile("^(" + _CONS_SEQ + ")?" + _VOWEL_SEQ + _CONS_SEQ + _VOWEL_SEQ + _CONS_SEQ)
_s_v = re.compile("^(" + _CONS_SEQ + ")?" + _VOWEL)
_c_v = re.compile("^" + _CONS_SEQ + _VOWEL + "[^aeiouwxy]$")

# Patterns used in the rules

_ed_ing = re.compile("^(.*)(ed|ing)$")
_at_bl_iz = re.compile("(at|bl|iz)$")
_step1b = re.compile("([^aeiouylsz])\\1$")
_step2 = re.compile("^(.+?)(ational|tional|enci|anci|izer|bli|alli|entli|eli|ousli|ization|ation|ator|alism|iveness|fulness|ousness|aliti|iviti|biliti|logi)$")
_step3 = re.compile("^(.+?)(icate|ative|alize|iciti|ical|ful|ness)$")
_step4_1 = re.compile("^(.+?)(al|ance|ence|er|ic|able|ible|ant|ement|ment|ent|ou|ism|ate|iti|ous|ive|ize)$")
_step4_2 = re.compile("^(.+?)(s|t)(ion)$")


PREFIXES = [
    'contra', 'hetero', 'circum', 'hyper',  'extra', 'inter', 'trans',
    'super', 'intra', 'macro', 'micro', 'mono', 'anti', 'post', 'ante',
    'omni', 'homo', 'auto', 'sub', 'syn', 'con', 'uni',
    'tri', 'non', 'em', 'ex', 'il', 'im', 'in', 'ir', 'un', 'mis',
]

SUFFIXES = [
    'ination', 'able', 'ation', 'ible', 'ial', 'est', 'full',
    'ive', 'ative', 'itive', 'less', 'ly', 'ment', 'ness', 'ous', 'eous',
    'ship', 'wise', 'ious', 'ies',
]

# words will not be stemmed
STOPWORDS = [
    'was', 'have', 'whose', 'whatever', 'whichever',
    'hers', 'mohamed', 'ahmed', 'hamed', 'she', 'there',
    'here', 'these', 'series', 'create',
    "about", "above", "after", "again", "against",
    "all", "also", "and", "any",
    "back", "because", "before", "below", "between", "because",
    "both", "but", "can", "could", "down", "during", "each",
    "few", "from", "for", "from", "further", "give",
    "have", "here", "into",
    "just", "more", "most", "nor", "not", "now",
    "off", "one", "once", "only", "own", "other", "our", "out", "over",
    "see", "she", "some", "such", "same", "some",
    "than", "that", "then", "too", "the", "then", "there",
    "these", "they", "this", "through", "under", "until", "use", "very",
    "was", "when", "where", "why", "while", "which", "who", "will", "with",
    "you", "your",
    'myself', 'ourselves', 'yourselves', 'herself', 'itself', 'themselves',
]


def deletePrefix(word):
    for pref in PREFIXES:
        if word.startswith(pref):
            word = word.replace(pref, "")
    return word

def deleteSuffix(word):
    for suff in SUFFIXES:
        if word.endswith(suff):
            if suff == "ies":
                word2 = word.replace('ies', 'y')  # movies error
                return word2
            elif suff == "ation":
                word3 = word.replace('ation', 'e') # Organization
                return word3
            else:
                #print(word, "drop suffix", suff)
                word = word.replace(suff, "")
    return word



""" remove pre/suffixes from English words """    
def stem(w):
    if w in STOPWORDS:
        return None

    w = deletePrefix(w)
    w = deleteSuffix(w)

    if len(w) < 4:
        return w

    # a 'y' can be a vowel or a consonant, handle  as special case
    first_is_y = (w[0] == "y")

    # Step 1b    
    if w.endswith("eed"):
        s = w[:-3]
        if _m_gr0.match(s):
            w = w[:-1]
    else:
        m = _ed_ing.match(w)
        if m:
            stem = m.group(1)
            if stem[-1] == stem[-2]:
                # handle "stemming" -> "stem" and "pitted" -> "pit"
                # but ... "dressing" -> "dress" and "pulled" -> "pull"
                #print("1b", stem, stem[-1], stem[-2], stem[:-1])
                if stem[-1] in ['s', 'l']:
                    w = stem
                else:
                    w = stem[:-1]
            elif _s_v.match(stem):
                w = stem
                if _at_bl_iz.match(w):
                    w += "e"
                elif _step1b.match(w):
                    w = w[:-1]
                elif _c_v.match(w):
                    w += "e"

    """
    # Step 1c    
    if w.endswith("y"):
        stem = w[:-1]
        if _s_v.match(stem):
            w = stem + "i"
    """
            
    # Step 2    
    m = _step2.match(w)
    if m:
        stem = m.group(1)
        suffix = m.group(2)
        if _m_gr0.match(stem):
            w = stem + STEP2LIST[suffix]
            
    # Step 3    
    m = _step3.match(w)
    if m:
        stem = m.group(1)
        suffix = m.group(2)
        if _m_gr0.match(stem):
            w = stem + STEP3LIST[suffix]

    # Step 4    
    m = _step4_1.match(w)
    if m:
        stem = m.group(1)
        if _m_gr1.match(stem):
            w = stem
    else:
        m = _step4_2.match(w)
        if m:
            stem = m.group(1) + m.group(2)
            if _m_gr1.match(stem):
                w = stem


    if w.endswith("ll") and _m_gr1.match(w):
        w = w[:-1]
    
    if first_is_y:
        #print("first_is_y")
        w = "y" + w[1:]

    return w


#----------------------------------------------
if __name__ == '__main__':
    if sys.argv[1:]:
        comingWord = sys.argv[1]
    else:
        comingWord = "doggy"

    sw = stem(comingWord)
    if sw:
        print(comingWord, "-->", sw)
    else:
        print(comingWord)
