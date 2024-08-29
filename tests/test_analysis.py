import pytest
import pandas as pd
import matplotlib.pyplot as plt

from notebooks import classify_sentiment

def test_perform_sentiment_analysis():
    sample_data = pd.DataFrame({
        'headline': ["This is good", "This is bad", "Neutral statement"]
    })
    result = classify_sentiment(sample_data)
    
    assert 'compound' in result.columns
    assert result['compound'].dtype == 'float64'
    assert result.shape[0] == 3

