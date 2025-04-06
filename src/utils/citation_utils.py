import re

def extract_citations(text):
    pattern = r"\[([^\]]+)\]"
    return list(set(re.findall(pattern, text)))
