import json
import os
import urllib.error
import urllib.request

from flask import Flask, request, render_template_string

app = Flask(__name__)
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8080").rstrip("/")

PAGE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>llmapp09</title>
  <style>
    body { font-family: Georgia, serif; margin: 2rem auto; max-width: 40rem; color: #1c1917; }
    textarea { width: 100%; min-height: 6rem; font: inherit; }
    button { margin-top: 0.75rem; }
    .answer { white-space: pre-wrap; background: #f5f5f4; padding: 1rem; }
    .error { color: #9f1239; }
  </style>
</head>
<body>
  <h1>llmapp09</h1>
  <form method="post">
    <label for="prompt">Prompt</label>
    <textarea id="prompt" name="prompt" required>{{ prompt }}</textarea>
    <button type="submit">Send</button>
  </form>
  {% if error %}<p class="error">{{ error }}</p>{% endif %}
  {% if answer %}<h2>Answer</h2><div class="answer">{{ answer }}</div>{% endif %}
</body>
</html>
"""


def ask_backend(prompt: str) -> str:
    payload = json.dumps({"prompt": prompt}).encode()
    req = urllib.request.Request(
        f"{BACKEND_URL}/chat",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as response:
        body = json.loads(response.read().decode())
    return body.get("response", "")


@app.get("/")
def index():
    return render_template_string(PAGE, prompt="", answer="", error="")


@app.post("/")
def submit():
    prompt = request.form.get("prompt", "").strip()
    answer = ""
    error = ""
    if prompt:
        try:
            answer = ask_backend(prompt)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            error = str(exc)
    return render_template_string(PAGE, prompt=prompt, answer=answer, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
