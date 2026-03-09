import customtkinter as ctk
import word
import sentence
import sentiment

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  

app = ctk.CTk()
app.title("Text Analyzer Pro")
app.geometry("850x650") 

def get_user_text():
    """Grabs text and checks if it's empty."""
    user_text = text_input.get("1.0", "end-1c")
    if not user_text.strip():
        display_result("⚠️ Error: Please paste some text first!")
        return None
    return user_text

def display_result(text_to_show):
    """Safely updates the read-only result box."""
    result_box.configure(state="normal") 
    result_box.delete("1.0", "end")      
    result_box.insert("1.0", text_to_show) 
    result_box.configure(state="disabled") 

def run_top_words():
    text = get_user_text()
    if text:
        result = word.get_top_words(text)
        output = "🏆 TOP 5 WORDS:\n" + "-" * 25 + "\n"
        for item in result:
            output += f"'{item[0]}': {item[1]}\n"
        display_result(output)

def run_least_words():
    text = get_user_text()
    if text:
        result = word.least_words(text)
        output = "📉 LEAST 5 WORDS:\n" + "-" * 25 + "\n"
        for item in result:
            output += f"'{item[0]}': {item[1]}\n"
        display_result(output)

def run_letter_counts():
    text = get_user_text()
    if text:
        result = word.get_letter_counts(text)
        output = "🔤 LETTER FREQUENCY:\n" + "-" * 25 + "\n"
        for item in result:
            output += f"{item[0].upper()}: {item[1]}\n"
        display_result(output)

def run_sentence_stats():
    text = get_user_text()
    if text:
        count = sentence.count_sentences(text)
        top_sent = sentence.get_top_sentences(text)
        output = "📝 SENTENCE STATS:\n" + "-" * 25 + f"\nTotal Sentences: {count}\n\nTop 3 Most Frequent:\n"
        for item in top_sent:
            output += f"'{item[0].capitalize()}': {item[1]} times\n"
        display_result(output)

def run_sentiment():
    text = get_user_text()
    if text:
        display_result("🧠 Running NLP Sentiment Analysis... please wait.")
        app.update() 
        
        result = sentiment.analyze_sentiment(text)
        output = "🎭 SENTIMENT ANALYSIS:\n" + "-" * 25 + f"\n{result}"
        display_result(output)


# --- UI ELEMENTS ---
title_label = ctk.CTkLabel(app, text="📊 Text Analyzer Pro", font=("Helvetica", 26, "bold"))
title_label.pack(pady=20)

text_input = ctk.CTkTextbox(app, height=180, width=700, font=("Helvetica", 14))
text_input.pack(pady=10)

# Button Grid Layout
button_frame = ctk.CTkFrame(app, fg_color="transparent")
button_frame.pack(pady=15)

# Row 0 Buttons
btn_top_words = ctk.CTkButton(button_frame, text="Top 5 Words", command=run_top_words)
btn_top_words.grid(row=0, column=0, padx=10, pady=10)

btn_least_words = ctk.CTkButton(button_frame, text="Least 5 Words", command=run_least_words)
btn_least_words.grid(row=0, column=1, padx=10, pady=10)

btn_letters = ctk.CTkButton(button_frame, text="Letter Frequency", command=run_letter_counts)
btn_letters.grid(row=0, column=2, padx=10, pady=10)

# Row 1 Buttons
btn_sentences = ctk.CTkButton(button_frame, text="Sentence Stats", command=run_sentence_stats)
btn_sentences.grid(row=1, column=0, padx=10, pady=10)

btn_sentiment = ctk.CTkButton(button_frame, text="Sentiment Analysis", command=run_sentiment, fg_color="#2b7a4b", hover_color="#1e5c36")
btn_sentiment.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10, pady=10) # Makes the AI button wider and green!

result_label = ctk.CTkLabel(app, text="Analysis Results:", font=("Helvetica", 16, "bold"))
result_label.pack(pady=(10, 0))

result_box = ctk.CTkTextbox(app, height=180, width=700, font=("Helvetica", 15), state="disabled")
result_box.pack(pady=10)

# 3. Start the App
if __name__ == "__main__":
    app.mainloop()