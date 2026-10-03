#!/usr/bin/env python3
"""
PRINCE2 Manage-By-Exception Tolerance Monitor
Evaluates project variances against predefined Project Board tolerances.
"""

class ProjectStage:
    def __init__(self, name: str, cost_budget: float, time_weeks: int, cost_tolerance_pct: float = 0.10, time_tolerance_weeks: int = 2):
        self.name = name
        self.budget = cost_budget
        self.planned_weeks = time_weeks
        self.cost_tolerance = cost_budget * cost_tolerance_pct
        self.time_tolerance = time_tolerance_weeks

    def evaluate_variance(self, actual_cost: float, actual_weeks: int):
        cost_var = actual_cost - self.budget
        time_var = actual_weeks - self.planned_weeks

        cost_breached = cost_var > self.cost_tolerance
        time_breached = time_var > self.time_tolerance

        status = "EXCEPTION: Escalate to Project Board" if (cost_breached or time_breached) else "NORMAL: Within Tolerance"
        return {
            "Stage": self.name,
            "Cost_Variance": cost_var,
            "Time_Variance_Weeks": time_var,
            "Status": status
        }

if __name__ == "__main__":
    stage1 = ProjectStage("Architecture Foundation", cost_budget=150000.0, time_weeks=8)
    res = stage1.evaluate_variance(actual_cost=162000.0, actual_weeks=9)
    print("[*] PRINCE2 Stage Tolerance Audit:")
    for k, v in res.items():
        print(f"  {k}: {v}")
