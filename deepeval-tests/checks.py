def classify(text: str) -> str:
    lowered = text.lower()
    if any(word in lowered for word in ("love", "great", "good", "happy")):
        return "positive"
    if any(word in lowered for word in ("hate", "bad", "terrible", "awful")):
        return "negative"
    return "neutral"


def sentiment(text: str) -> str:
    return classify(text)


def summarize(text: str, limit: int = 40) -> str:
    compact = " ".join(text.split())
    if len(compact) <= limit:
        return compact
    return compact[: limit - 3].rstrip() + "..."


def intent(text: str) -> str:
    lowered = text.lower()
    if lowered.startswith(("what", "why", "how", "when", "where")):
        return "question"
    if any(word in lowered for word in ("please", "summarize", "classify", "translate")):
        return "command"
    return "statement"
