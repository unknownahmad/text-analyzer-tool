from textblob import TextBlob

def analyze_sentiment(text):
    """
    Ingests raw text into a local NLP model and extracts the emotional polarity.
    Returns a formatted string with the Sentiment (Positive/Negative/Neutral) and the raw score.
    """
    try:
        # Load the text into the TextBlob engine
        blob = TextBlob(text)
        
        # Polarity is a float ranging from -1.0 (Very Negative) to 1.0 (Very Positive)
        score = blob.sentiment.polarity
        
        # Convert the mathematical score into a human-readable label
        if score > 0.1:
            label = "Positive 🟢"
        elif score < -0.1:
            label = "Negative 🔴"
        else:
            label = "Neutral ⚪"
            
        return f"{label} (Polarity Score: {score:.2f})"
        
    except Exception as e:
        # Catch unexpected errors so the main app doesn't crash
        return f"Analysis Error: {e}"