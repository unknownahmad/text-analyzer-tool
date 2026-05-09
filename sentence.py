import re
from collections import Counter

def count_sentences(text: str) -> int:
    """Counts total sentences using punctuation boundaries."""
    # Splits text at any '.', '!', or '?' followed by a space or end of string
    sentences = re.split(r'[.!?]+\s*', text)
    # Remove empty strings from the list
    return len([s for s in sentences if s.strip()])

def get_top_sentences(text: str, limit: int = 3) -> list:
    """Returns the most frequently occurring sentences."""
    parts = re.split(r'[.!?]+\s*', text)
    sentences = [p.strip().lower() for p in parts if p.strip()]
    return Counter(sentences).most_common(limit)