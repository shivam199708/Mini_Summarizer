from app.summarizer import summarize_text

if __name__ == "__main__":
    input_text = """Machine learning is a field of artificial intelligence that uses statistical techniques to give computer systems the ability to learn from data."""
    print("Summary:")
    print(summarize_text(input_text))
