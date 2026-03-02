# Agentic Deals Platform (Best Buy–style)

An end-to-end **Agentic AI deal discovery engine** inspired by a large electronics retailer.

## High-level architecture

- **Java 17 / Spring Boot** – API gateway for deal requests
- **Python 3.11 Agentic AI** – LangGraph + LangChain + RAG
- **MongoDB** – NoSQL store for SKUs, inventory, pricing, region config
- **FAISS** – Vector search over SKU embeddings
- **PyTorch Two-Tower** – Custom embedding model for query ↔ SKU similarity
- **Ollama + vLLM** – Local LLMs for reasoning and reflection
- **Docker Compose** – One-command local environment

## Services

- `java-api`: REST endpoint `/api/deals`
- `agentic-ai`: Agentic reasoning, RAG, embeddings, LLM calls
- `mongodb`: NoSQL backing store
- `faiss-builder`: one-shot container to build FAISS index from MongoDB

## Quick start

```bash
# 1. Build and start all services
docker-compose up --build

# 2. Seed MongoDB and build FAISS index
docker-compose run --rm agentic-ai python scripts/seed_mongodb.py
docker-compose run --rm agentic-ai python scripts/build_faiss_index.py

# 3. Call the Java API
curl -X POST http://localhost:8080/api/deals \
  -H "Content-Type: application/json" \
  -d '{
    "customerId": "CUST-1001",
    "region": "MIDWEST",
    "intentQuery": "4K TV under 900 dollars",
    "velocityType": "VT",
    "preferredCategories": ["TV"]
  }'
