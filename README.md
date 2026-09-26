# day3-workshop

LLMSecOps day 3 work for this repo is **llmapp09 onwards**: Docker, Kubernetes, and GitHub Actions. Earlier labs stay listed below and are out of scope.

Docker Hub account used in the workflows and image tags: `sritampatnaik`.

## llmapp09

```bash
docker compose up -d --build
```

API: http://localhost:8080/docs  
Frontend: http://localhost:5000

On macOS, AirPlay Receiver often already listens on port 5000. Turn it off in System Settings, or run the frontend with `PORT=5001`.

Kubernetes, from this folder:

```bash
cd llm-multiroute && kubectl apply -f ./k8s/deployment.yaml
kubectl port-forward svc/llm-multiroute-service -n llm-multiroute-backend 8080

cd llm-frontend-python && kubectl apply -f ./k8s/deployment.yaml
kubectl port-forward svc/llm-frontend-service -n llm-frontend 5000
```

Workflows:

- `.github/workflows/llm-multiroute-ci.yaml` builds the API image, scans it with Trivy (`HIGH,CRITICAL`), then pushes `sritampatnaik/llm-multiroute:1.0.0`
- `.github/workflows/llm-frontend-python-ci.yaml` does the same for `sritampatnaik/llm-frontend-python:1.0.0`
- `.github/workflows/promptfoo-tests.yaml`
- `.github/workflows/deepeval-tests.yaml`

## Not done

### Still open from pre-setup

- [ ] Start Docker Desktop and confirm `docker info` works

### llmapp01 — Self-host

Ollama, `gemma:2b`, and the custom `ipe` model are done. The app is not.

- [ ] Start the backend in `llmapp01/llm-python` (Python 3.11.9 or 3.11.10, port 8080)
- [ ] Open http://localhost:8080/swagger-ui.html
- [ ] Start the frontend in `llmapp01/llm-frontend-python` (port 5000)
- [ ] Open http://localhost:5000

The `llmapp01` source is not in this folder yet.

### llmapp02 — Centralized API (15 min)

- [ ] Set `OLLAMA_API_KEY` (trainer key, valid only during the session)
- [ ] Point inference at the cloud and walk through the provided code
- [ ] Start backend `llmapp02/llm-python` on port 8080
- [ ] Start frontend `llmapp02/llm-frontend-python` on port 5000

### llmapp03 — Multi-model routing (15 min)

- [ ] Walk through the routing code
- [ ] Start backend `llmapp03/llm-multiroute` on port 8080
- [ ] Start frontend `llmapp03/llm-frontend-python` on port 5000

### llmapp04 — Promptfoo (20 min)

- [ ] Install Promptfoo (`npm install -g promptfoo`) and check `promptfoo --version`
- [ ] Run `promptfoo init`
- [ ] Start backend and frontend under `llmapp04/`
- [ ] In `llmapp04/promptfoo-tests`, run `nvm use 22` and `npm run eval`

### llmapp05 — Toxicity, bias, and hallucination with DeepEval (20 min)

- [ ] Start the app
- [ ] In `llmapp05/deepeval-tests`, use Python 3.11 and `pip install -r requirements.txt`
- [ ] Optional: `deepeval set-ollama --model=<modelname>` to skip `OPENAI_API_KEY`
- [ ] Run `deepeval test run test_classify.py test_sentiment.py test_summarize.py test_intent.py`

### llmapp06 — Logging (15 min)

- [ ] Walk through the logging code
- [ ] Start the backend and frontend

### llmapp07 — Langfuse (15 min)

- [ ] Create a Langfuse account, project, and API key
- [ ] Create an OpenAI API key
- [ ] Fill `.env` with `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, `LANGFUSE_HOST`, and `OPENAI_API_KEY`
- [ ] Walk through the tracing code
- [ ] Start backend and frontend under `llmapp07/`

### llmapp08 — Guardrails (20 min)

- [ ] Walk through the guardrails code
- [ ] Start backend and frontend under `llmapp08/`

### llmapp09 — CI/CD (90 min)

- [x] Dockerfiles for `llm-multiroute` and `llm-frontend-python`
- [x] Root `docker-compose.yml` (services, images, ports, volume, network)
- [x] Kubernetes manifests: `llm-multiroute/k8s/deployment.yaml` and `llm-frontend-python/k8s/deployment.yaml`
- [x] GitHub Actions for image build, Trivy scan, Docker Hub push, Promptfoo, and DeepEval
- [x] Workflows use Docker Hub account `sritampatnaik`
- [x] Published in this repo, not a separate `llmapp09` repository
- [ ] Start Docker Desktop and run `docker compose up -d --build`
- [ ] Scan a built image with `trivy image --severity HIGH,CRITICAL <image>`
- [ ] Push `sritampatnaik/llm-multiroute:1.0.0` and `sritampatnaik/llm-frontend-python:1.0.0`
- [ ] Apply the Kubernetes manifests and port-forward ports 8080 and 5000
- [ ] Create a Docker Hub token (Read & Write) and add GitHub Actions secrets: `DOCKERHUB_TOKEN`, `OLLAMA_API_KEY`, `OLLAMA_BASE_URL`, `OPENAI_API_KEY`

## Done

- [x] Git, VS Code, Homebrew, nvm, and pyenv
- [x] Node 22.23.3 (`nvm use 22` in the Promptfoo lab; new terminals still default to Node 20)
- [x] pyenv hooked into `~/.zshrc` (labs use `pyenv shell 3.11.9`)
- [x] This repo on GitHub: https://github.com/sritampatnaik/day3-workshop
- [x] Ollama 0.34.4 listening on `127.0.0.1:11434`
- [x] `gemma:2b` pulled
- [x] Custom model `ipe` created from `Modelfile` (plain-English system prompt)
