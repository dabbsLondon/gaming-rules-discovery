from fastapi import FastAPI

app = FastAPI(title="HH3 Rules Harvester")


@app.get("/health")
def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}
