#!/usr/bin/env bash
# Reference build for both workshop platforms. The second push replaces the tag.
set -euo pipefail

IMAGE="${DOCKERHUB_USER:-sritampatnaik}/llm-frontend-python:1.0.0"

docker build --platform linux/arm64 -t "$IMAGE" .
docker push "$IMAGE"

docker build --platform linux/amd64 -t "$IMAGE" .
docker push "$IMAGE"
