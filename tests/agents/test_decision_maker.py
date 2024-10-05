import pytest
from src.models.decision import Decision, DecisionChoice
from src.agents.decision_maker import DecisionMaker  # 假设 DecisionMaker 在这个模块中

@pytest.fixture
def decision_maker():
    # 设置测试数据
    decision = Decision(title="选择最佳方案", description="选择最优的决策方案")
    choices = [
        DecisionChoice(content="方案A", decision_id=decision.id),
        DecisionChoice(content="方案B", decision_id=decision.id),
    ]
    return DecisionMaker(decision, choices)

def test_analyze_choices(decision_maker):
    # 测试 analyze_choices 方法
    best_choice_id = decision_maker.analyze_choices()
    assert best_choice_id in [choice.id for choice in decision_maker.choices], "推荐的最佳选项ID 应该在选项列表中"