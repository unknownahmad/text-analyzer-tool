# 📊 Text Analyzer Pro

A comprehensive Python-based NLP tool designed to process unstructured text and extract meaningful data insights through a modern graphical desktop interface. 

## 🚀 Key Features

- **🧠 Local NLP Sentiment Analysis**: Utilizes a local machine learning model to determine the emotional polarity (Positive, Negative, or Neutral) of any text without needing external APIs.
- **📂 Document Parsing**: Seamlessly extract and analyze text directly from uploaded `.pdf` and `.docx` files.
- **📈 Advanced Word Frequency**: Identifies both the top 5 most used words and the least frequent words while automatically filtering out "noise" (common stop words).
- **📝 Sentence Analytics**: Tracks total sentence counts and identifies recurring sentence patterns.
- **🖥️ Modern Dashboard**: Built with a sleek, dark-mode CustomTkinter interface for a high-quality user experience.
- **🔤 Character Mapping**: Analyzes the distribution of every letter (A-Z) used in the text.

## 🛠️ Technical Implementation

- **Language**: Python 3
- **GUI Framework**: CustomTkinter
- **NLP Engine**: TextBlob (Local ML Model)
- **Document Processing**: PyPDF, Python-docx
- **Architecture**: Modular design with dedicated components for word, sentence, sentiment, and file processing.