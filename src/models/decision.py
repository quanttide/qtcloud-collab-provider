"""
决策领域模型
"""

from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Decision(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(datetime.timezone.utc))
