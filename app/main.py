from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from app.router import router

app = FastAPI()  # Initializing the app



app.include_router(router)
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")


def main():
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)



if __name__ == "__main__":
    main()