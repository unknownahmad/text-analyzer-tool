def count_sentences(text):
    clean_text = text.replace("!", ".")
    clean_text = clean_text.replace("?", ".")
    sentences = clean_text.split(".")
    real_sentences = []
    for s in sentences:
        if len(s.strip()) > 0:
            real_sentences.append(s)
    return len(real_sentences)


##tracks how many sentenses are in the users text

def get_top_sentences(text):
    
    clean_text = text.replace("!", ".")
    clean_text = clean_text.replace("?", ".")
    
    parts = clean_text.split(".")
    
    sentences = []
    for p in parts:
        clean_s = p.strip() 
        if len(clean_s) > 0:
            sentences.append(clean_s)
            

    counts = {}
    for s in sentences:
        s_lower = s.lower()
        if s_lower in counts:
            counts[s_lower] = counts[s_lower] + 1
        else:
            counts[s_lower] = 1
            
    pairs = list(counts.items())
    
    def get_count(item):
        return item[1]
        
    sorted_sentences = sorted(pairs, key=get_count, reverse=True)
    
    return sorted_sentences[:3]

##tracks how many times each sentence was repeated and return top 3