def get_count(item):
   return item[1]


def get_top_words(text):
   clean_text = text.lower()
   punctuation = '.,!?:;"\'()[]-'
   for char in punctuation:
       clean_text = clean_text.replace(char, " ")
   words = clean_text.split()
  
   stop_words = ["the", "and", "is", "of", "to", "a", "in", "it", "that", "or", "for", "on", "are", "this", "my", "be", "as","which","from"]
  
   filtered_words = []
   for w in words:
       if w not in stop_words:
           filtered_words.append(w)


   counts = {}
  
   for w in filtered_words:
       if w in counts:
           counts[w] = counts[w] + 1
       else:
           counts[w] = 1
          
   pairs = list(counts.items())
  
   sorted_words = sorted(pairs, key=get_count, reverse=True)
   return sorted_words[:5]

def get_letter_counts(text):
  
   text = text.lower()
  
   letters = {}
  
   alphabet = "abcdefghijklmnopqrstuvwxyz"
  
   for char in text:
       if char in alphabet:
           if char in letters:
               letters[char] = letters[char] + 1
           else:
               letters[char] = 1
   return letters