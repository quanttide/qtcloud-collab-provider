"""
决策智能体
"""

from src.models.decision import Decision, DecisionChoice
from typing import List


class DecisionMaker:
    def __init__(self, decision: Decision, choices: List[DecisionChoice]):
        self.decision = decision
        self.choices = choices

    def analyze_choices(self):
        # 这里可以实现 AI 算法来分析选项
        # 例如，使用简单的评分系统或机器学习模型
        scores = {choice.id: self.evaluate_choice(choice) for choice in self.choices}
        best_choice_id = max(scores, key=scores.get)
        return best_choice_id

    def evaluate_choice(self, choice: DecisionChoice):
        # 评估选项的逻辑，可以根据具体需求进行调整
        # 这里可以使用一些简单的规则或 AI 模型
        return len(choice.content)  # 示例：根据内容长度评分

