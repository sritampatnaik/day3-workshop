from checks import intent


def test_intent_question():
    assert intent("Why is the sky blue?") == "question"


def test_intent_command():
    assert intent("Please summarize this paragraph") == "command"


def test_intent_statement():
    assert intent("The pipeline scanned the image") == "statement"
