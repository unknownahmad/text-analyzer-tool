import word
import sentence
import sentiment  # Pulling in our local NLP engine

def welcome():
    # Setting up the initial landing screen so it feels like a real app
    print("=" * 60)
    print("       📊   T E X T   A N A L Y Z E R   P R O   📊")
    print("=" * 60)
    print("         Analyze words, letters, sentences, and emotion.")
    print("-" * 60)
    print("") 

    print("Instructions:")
    print("1. Copy your text.")
    print("2. Paste it below.")
    print("3. Press ENTER.")
    print("")

    # Grab the raw text from the user
    text_input = input("PASTE YOUR TEXT HERE:\n>> ")
    return text_input


def menu():
   # Keeps the terminal looking clean between operations
   print("\n\n⚙️  ANALYSIS MENU ⚙️")
   print("-" * 28)
   print("1. Top 5 Word Frequency")
   print("2. Letter Frequency (A-Z)")
   print("3. Sentence Count")
   print("4. Sentiment Analysis (Local NLP)")
   print("5. Least 5 Word Frequency")  # Wired up your new function!
   print("6. Exit")


def main():
    user_text = welcome()
    
    # Quick safety check: don't let them crash the program by passing empty spaces
    if len(user_text.strip()) == 0:
        print("Error: No text entered. Please restart and paste valid text.")
        return

    # Main application loop - keeps running until they explicitly choose to exit
    while True:
        menu()
        choice = input("\nSelect an option (1-6): ")
        
        if choice == "1":
            result = word.get_top_words(user_text)
            print("\nTOP 5 WORDS")
            for item in result:
                print(f"'{item[0]}': {item[1]}")
                
        elif choice == "2":
            result = word.get_letter_counts(user_text)
            print("\nLETTER FREQUENCY")
            for item in result:
                print(f"{item[0].upper()}: {item[1]}")
                
        elif choice == "3":
            count = sentence.count_sentences(user_text)
            top_sent = sentence.get_top_sentences(user_text)
            
            print("\nSENTENCE STATS")
            print(f"Total Sentences: {count}")
            print("\nTop 3 Most Frequent:")
            for item in top_sent:
                print(f"'{item[0].capitalize()}': {item[1]} times")
                
        elif choice == "4":
            # Fire up the NLP model to get the emotional polarity
            print("\n🧠 RUNNING NLP SENTIMENT ANALYSIS...")
            result = sentiment.analyze_sentiment(user_text)
            print(f"Result: {result}")

        elif choice == "5":
            # Your brand new function!
            result = word.least_words(user_text)
            print("\nLEAST 5 WORDS")
            for item in result:
                print(f"'{item[0]}': {item[1]}")
            
        elif choice == "6":
            print("Goodbye!")
            break
            
        else:
            # Catch typos or invalid numbers so the loop doesn't break
            print("Invalid choice. Please select a number between 1 and 6.")
            
        # Pause the terminal so they can actually read the results before the menu redraws
        input("\nPress Enter to continue...")

# Fire up the app
if __name__ == "__main__":
    main()