from app.summarizer import summarize_text

def test_summary_output():
    input_text = "Python is a widely used programming language known for its readability."
    summary = summarize_text(input_text)
    assert isinstance(summary, str)
    assert len(summary) > 0
