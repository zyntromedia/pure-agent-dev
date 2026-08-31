"""
tests/test_executor.py
Verify Agent executes tasks via ComputeProvider interface
"""

import pytest
from schemas.task import AgentTask

@pytest.mark.asyncio
async def test_executor_calls_provider_list_instances(executor, mock_provider):
    task = AgentTask(task_id="t-001", action="list_instances")
    await executor.run(task)
    mock_provider.list_instances.assert_awaited_once()

@pytest.mark.asyncio
async def test_executor_calls_provider_start_instance(executor, mock_provider):
    task = AgentTask(task_id="t-002", action="start_instance", instance_id="i-test")
    await executor.run(task)
    mock_provider.start_instance.assert_awaited_once_with("i-test")
