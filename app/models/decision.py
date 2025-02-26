"""
决策领域模型
"""

from sqlmodel import SQLModel, Field
from typing import Optional, List
from datetime import datetime

class Decision(SQLModel, table=True):
    """
    决策类表示一个决策的模型，包含决策的基本信息。
    
    属性:
        id (Optional[int]): 决策的唯一标识符。
        title (str): 决策的标题。
        description (str): 决策的详细描述，提供决策的背景和目的。
        process_steps (List[str]): 梳理决策过程的步骤。
        created_at (datetime): 决策创建的时间，默认为当前时间。
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(datetime.timezone.utc))

class DecisionChoice(SQLModel, table=True):
    """
    决策选项类表示一个决策的选项模型，包含选项的基本信息。
    
    属性:
        id (Optional[int]): 选项的唯一标识符。
        decision_id (int): 关联的决策的唯一标识符。
        description (str): 选项的具体内容，描述该选项的细节。
        created_at (datetime): 选项创建的时间，默认为当前时间。
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    decision_id: int = Field(foreign_key="decision.id")
    description: str  # 选项的具体内容，描述该选项的细节。
    created_at: datetime = Field(default_factory=lambda: datetime.now(datetime.timezone.utc))

