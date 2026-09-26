from checks import classify


def test_classify_positive():
    assert classify("I love this result") == "positive"


def test_classify_negative():
    assert classify("This output is terrible") == "negative"


def test_classify_neutral():
    assert classify("The server is on port 8080") == "neutral"
