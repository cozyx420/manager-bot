# manager-bot (Orchestrator)

FastAPI-Service, der Anfragen entgegennimmt, Schritte plant (z. B. Recherche) und Ergebnisse konsolidiert.
Entwickelt für Zusammenspiel mit spezialisierten Agents (Researcher, Critic, Chat, RAG).

## Quickstart (lokal)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
# → http://localhost:8000/healthz
