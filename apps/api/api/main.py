"""Api routes."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/status")
def status() -> dict:
    """Return the status of the API.

    Returns:
        dict: The status of the API.

    """
    return {"status": "OK"}
