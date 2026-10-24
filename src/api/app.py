from fastapi import FastAPI

from src.api.routes import router

app = FastAPI(title="Robot Tool Server")
app.include_router(router)
