from textblob import TextBlob

def analyze_sentiment(text: str) -> str:
    """Performs NLP analysis to determine polarity and subjectivity."""
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        if polarity > 0.1:
            label = "Positive 🟢"
        elif polarity < -0.1:
            label = "Negative 🔴"
        else:
            label = "Neutral ⚪"
            
        sub_label = "Objective (Fact-based)" if subjectivity < 0.5 else "Subjective (Opinion-based)"
            
        return (f"Sentiment: {label} ({polarity:.2f})\n"
                f"Tone: {sub_label} ({subjectivity:.2f})")
        
    except Exception as e:
        return f"Analysis Error: {e}"