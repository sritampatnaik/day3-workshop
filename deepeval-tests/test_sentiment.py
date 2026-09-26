from checks import sentiment


def test_sentiment_positive():
    assert sentiment("A great answer") == "positive"


def test_sentiment_negative():
    assert sentiment("A bad answer") == "negative"
