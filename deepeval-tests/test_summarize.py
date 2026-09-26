from checks import summarize


def test_summarize_short_text_is_unchanged():
    assert summarize("Short note") == "Short note"


def test_summarize_long_text_is_shorter():
    source = "This sentence is much longer than the summary limit we set for the lab."
    summary = summarize(source, limit=24)
    assert len(summary) <= 24
    assert summary.endswith("...")
