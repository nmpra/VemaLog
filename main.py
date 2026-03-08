from fastapi import FastAPI

app = FastAPI()


@app.get("/vehicles")
def get_all_vehicles():
    return {"status": "VemaLog API is running!"}
