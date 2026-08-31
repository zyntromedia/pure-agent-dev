"""
tests/test_planner.py
Verify Agent task planning & schema validation
"""

from schemas.task import AgentTask

def test_planner_produces_valid_schema(planner):
    task = planner.plan("list all instances")
    assert isinstance(task, AgentTask)
    assert task.task_id
    assert task.action in {
        "list_instances", "start_instance", "stop_instance", "reboot_instance"
    }

def test_list_instances_needs_no_instance_id(planner):
    task = planner.plan("list instances")
    assert task.action == "list_instances"
    assert task.instance_id is None
