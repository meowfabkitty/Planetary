"""
nodes.autonomy

Autonomy level helpers and policies.
"""

AUTONOMY_LEVELS = {
    1: "Outpost",
    2: "Assisted settlement",
    3: "Autonomous settlement",
    4: "Self-maintaining settlement",
    5: "Generative settlement",
    6: "Frontier civilization",
}


def describe_level(level: int) -> str:
    return AUTONOMY_LEVELS.get(level, "Unknown")


# TODO: implement capability checks, escalation, and local policy enforcement
