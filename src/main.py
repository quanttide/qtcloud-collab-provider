"""
程序启动入口
"""

from fastapi import FastAPI

from .routers import topic
from .db import engine

app = FastAPI()

app.include_router(topic.router, prefix="/api", tags=["topics"])
