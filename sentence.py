def count_sentences(text):
    # Standardize all sentence endings to a period so we can split cleanly
    clean_text = text.replace("!", ".")
    clean_text = clean_text.replace("?", ".")
    
    sentences = clean_text.split(".")
    
    # Filter out empty strings caused by trailing punctuation
    real_sentences = []
    for s in sentences:
        if len(s.strip()) > 0:
            real_sentences.append(s)
            
    return len(real_sentences)


def get_top_sentences(text):
    # Normalize punctuation for splitting
    clean_text = text.replace("!", ".")
    clean_text = clean_text.replace("?", ".")
    
    parts = clean_text.split(".")
    
    # Clean up whitespace and drop empty strings
    sentences = []
    for p in parts:
        clean_s = p.strip() 
        if len(clean_s) > 0:
            sentences.append(clean_s)
            
    # Count the frequency of each exact sentence
    counts = {}
    for s in sentences:
        s_lower = s.lower() # Case-insensitive counting
        if s_lower in counts:
            counts[s_lower] = counts[s_lower] + 1
        else:
            counts[s_lower] = 1
            
    # Convert dictionary to a list of tuples for sorting
    pairs = list(counts.items())
    
    # Custom sorting key to sort by the count (index 1 of the tuple)
    def get_count(item):
        return item[1]
        
    sorted_sentences = sorted(pairs, key=get_count, reverse=True)
    
    # Return only the top 3 most repeated sentences
    return sorted_sentences[:3]