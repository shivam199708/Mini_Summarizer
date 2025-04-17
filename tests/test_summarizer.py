import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.summarizer import summarize_text

def test_summarization():
    input_text = "Machine learning is a subset of artificial intelligence that gives computers the ability to learn without being explicitly programmed."
    summary = summarize_text(input_text)
    assert isinstance(summary, str)
    assert len(summary) > 0
