from textblob import TextBlob

def analyze_sentiment(text):
    try:
        blob = TextBlob(text)
        score = blob.sentiment.polarity
        if score > 0.1:
            label = "Positive 🟢"
        elif score < -0.1:
            label = "Negative 🔴"
        else:
            label = "Neutral ⚪"
            
        return f"{label} (Polarity Score: {score:.2f})"
        
    except Exception as e:
        return f"Analysis Error: {e}"