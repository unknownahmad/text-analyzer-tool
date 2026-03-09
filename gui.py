import customtkinter as ctk
from customtkinter import filedialog
import os
import word
import sentence
import sentiment
import file_handler 

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  

app = ctk.CTk()
app.title("Text Analyzer Pro")
app.geometry("900x750")

def get_user_text():
    user_text = text_input.get("1.0", "end-1c")
    if not user_text.strip():
        display_result("⚠️ Error: Please paste some text first!")
        return None
    return user_text

def display_result(text_to_show):
    result_box.configure(state="normal") 
    result_box.delete("1.0", "end")      
    result_box.insert("1.0", text_to_show) 
    result_box.configure(state="disabled") 

def upload_file():
    file_path = filedialog.askopenfilename(
        title="Select a Document",
        filetypes=[("Documents", "*.pdf *.docx *.txt"), ("All Files", "*.*")]
    )
    if file_path:
        content = file_handler.get_file_content(file_path)
        text_input.delete("1.0", "end")
        text_input.insert("1.0", content)
        display_result(f"✅ Successfully loaded: {os.path.basename(file_path)}")

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

title_label = ctk.CTkLabel(app, text="📊 Text Analyzer Pro", font=("Helvetica", 28, "bold"))
title_label.pack(pady=(20, 10))

input_frame = ctk.CTkFrame(app, fg_color="transparent")
input_frame.pack(pady=5, padx=30, fill="x")

input_header = ctk.CTkFrame(input_frame, fg_color="transparent")
input_header.pack(fill="x", pady=(0, 5))

ctk.CTkLabel(input_header, text="1. Paste Text or Upload File", font=("Helvetica", 16, "bold")).pack(side="left")
ctk.CTkButton(input_header, text="📂 Upload PDF / Word", command=upload_file, fg_color="#4a4a4a", hover_color="#3a3a3a", width=140).pack(side="right")

text_input = ctk.CTkTextbox(input_frame, height=150, font=("Helvetica", 14), border_width=2, border_color="#3a3a3a", corner_radius=10)
text_input.pack(fill="x")

button_label = ctk.CTkLabel(app, text="2. Select Analysis", font=("Helvetica", 16, "bold"))
button_label.pack(pady=(15, 0))

button_frame = ctk.CTkFrame(app, fg_color="transparent")
button_frame.pack(pady=10)

btn_style = {"width": 160, "height": 40, "font": ("Helvetica", 14, "bold"), "corner_radius": 8}

ctk.CTkButton(button_frame, text="Top 5 Words", command=run_top_words, **btn_style).grid(row=0, column=0, padx=10, pady=10)
ctk.CTkButton(button_frame, text="Least 5 Words", command=run_least_words, **btn_style).grid(row=0, column=1, padx=10, pady=10)
ctk.CTkButton(button_frame, text="Letter Frequency", command=run_letter_counts, **btn_style).grid(row=0, column=2, padx=10, pady=10)
ctk.CTkButton(button_frame, text="Sentence Stats", command=run_sentence_stats, **btn_style).grid(row=1, column=0, padx=10, pady=10)
ctk.CTkButton(button_frame, text="Sentiment Analysis", command=run_sentiment, fg_color="#2b7a4b", hover_color="#1e5c36", **btn_style).grid(row=1, column=1, columnspan=2, sticky="ew", padx=10, pady=10)

output_frame = ctk.CTkFrame(app, fg_color="transparent")
output_frame.pack(pady=5, padx=30, fill="x")

ctk.CTkLabel(output_frame, text="3. Analysis Results", font=("Helvetica", 16, "bold")).pack(anchor="w", pady=(0, 5))

result_box = ctk.CTkTextbox(output_frame, height=180, font=("Helvetica", 15), state="disabled", fg_color="#1e1e1e", border_width=2, border_color="#3a3a3a", corner_radius=10)
result_box.pack(fill="x")

if __name__ == "__main__":
    app.mainloop()
