from fastapi import FastAPI

app = FastAPI(title="BA Copilot API")

@app.get("/")
def root():
    return {"message": "BA Copilot backend running"}
