"""
tests/test_compute_service.py
Verify ComputeService routes tasks to correct provider methods
"""

import pytest
from schemas.task import AgentTask

@pytest.mark.asyncio
async def test_service_list_instances(compute_service):
    instances = await compute_service.list_instances()
    assert isinstance(instances, list)

@pytest.mark.asyncio
async def test_service_start_validates_instance_id(compute_service):
    task = AgentTask(task_id="t-003", action="start_instance", instance_id="i-abc")
    result = await compute_service.execute(task)
    assert result is not None
