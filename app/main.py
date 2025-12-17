from fastapi import FastAPI

app = FastAPI(
    title = "Recommender API",
    description = "Testing FastAPI",
    version = "0.1.0",
)

@app.get("/health")
def health_check():
    return {"Health": "Corona"}