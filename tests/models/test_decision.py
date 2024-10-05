import pytest
from src.models.decision import Decision

def test_decision_creation():
    decision = Decision(title="项目启动", description="启动新产品开发项目")
    assert decision.id is not None
    assert decision.title == "项目启动"
    assert decision.description == "启动新产品开发项目"
    assert decision.created_at is not None

if __name__ == "__main__":
    pytest.main()
