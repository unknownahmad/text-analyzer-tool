import re
from collections import Counter

STOP_WORDS = {
    "the", "and", "is", "of", "to", "a", "in", "it", "that", "or", 
    "for", "on", "are", "this", "my", "be", "as", "which", "from",
    "you", "why", "because", "we", "they", "he", "she", "with", 
    "at", "by", "an", "not", "but", "what", "all", "were", "when", 
    "how", "can", "your", "have", "has", "do", "will", "i", "so"
}

def clean_and_tokenize(text: str) -> list:
    """Helper to clean punctuation and split text into lowercase words."""
    return re.findall(r'\w+', text.lower())

def get_top_words(text: str, limit: int = 5) -> list:
    """Returns the most frequent non-stop words."""
    words = clean_and_tokenize(text)
    filtered_words = [w for w in words if w not in STOP_WORDS]
    
    return Counter(filtered_words).most_common(limit)

def least_words(text: str, limit: int = 5) -> list:
    """Returns the least frequent non-stop words."""
    words = clean_and_tokenize(text)
    filtered_words = [w for w in words if w not in STOP_WORDS]
    
    counts = Counter(filtered_words)
    return sorted(counts.items(), key=lambda x: x[1])[:limit]

def get_letter_counts(text: str) -> list:
    """Returns alphabetically sorted letter frequencies."""
    letters = [char for char in text.lower() if char.isalpha()]
    return sorted(Counter(letters).items())