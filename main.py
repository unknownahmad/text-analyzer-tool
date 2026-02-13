import word
import sentence

def welcome():
    print("=" * 60)
    print("       📊   T E X T   A N A L Y Z E R   P R O   📊")
    print("=" * 60)
    print("         Analyze words, letters, and sentences.")
    print("-" * 60)
    print("") 

    print("Instructions:")
    print("1. Copy your text.")
    print("2. Paste it below.")
    print("3. Press ENTER.")
    print("")

    text_input = input("PASTE YOUR TEXT HERE:\n>> ")
    return text_input
##welcome page/text the 


def menu():
   print("\n\n⚙️  ANALYSIS MENU ⚙️")
   print("-" * 28)
   print("1. Top 5 Word Frequency")
   print("2. Letter Frequency (A-Z)")
   print("3. Sentence Count")
   print("4. Exit")
## the manu of my programme to showcase the diffrent options 


def main():
    user_text = welcome()
    
    if len(user_text.strip()) == 0:
        print("Error: No text entered.")
        return

    while True:
        menu()
        choice = input("\nSelect an option (1-4): ")
        
        if choice == "1":
            result = word.get_top_words(user_text)
            
            print("\nTOP 5 WORDS")
            for item in result:
                word_text = item[0]
                count = item[1]
                print(f"'{word_text}': {count}")
                
        elif choice == "2":
            result = word.get_letter_counts(user_text)
            
            print("\nLETTER FREQUENCY")
            for item in result:
                letter = item[0]
                count = item[1]
                print(f"{letter.upper()}: {count}")
                
        elif choice == "3":
            count = sentence.count_sentences(user_text)
            
            top_sent = sentence.get_top_sentences(user_text)
            
            print("\nSENTENCE STATS")
            print(f"Total Sentences: {count}")
            
            print("\nTop 3 Most Frequent:")
            for item in top_sent:
                sent_text = item[0]
                sent_count = item[1]
                print(f"'{sent_text.capitalize()}': {sent_count} times")
            
        elif choice == "4":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice, try again.")
            
        input("\nPress Enter to continue...")
##main fuction that orchertrate the whole programme



main()
