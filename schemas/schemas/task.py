"""
schemas/task.py
Structured Agent Task — validated at runtime by Pydantic.
Mirrors JSON Schema: schemas/agent-task.schema.json
"""

from typing import Literal, Optional
from pydantic import BaseModel, Field


class AgentTask(BaseModel):
    """
    Structured task for the Agent — NEVER free-form text.
    Validates: task_id, allowed actions, and instance_id presence rules.
    """

    task_id: str = Field(
        ...,
        description="Unique identifier for this task",
        min_length=1
    )

    action: Literal[
        "list_instances",
        "start_instance",
        "stop_instance",
        "reboot_instance",
    ] = Field(..., description="Operation to perform")

    instance_id: Optional[str] = Field(
        default=None,
        description="Target instance ID — required for start/stop/reboot",
    )
