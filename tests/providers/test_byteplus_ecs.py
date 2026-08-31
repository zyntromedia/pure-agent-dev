"""
tests/providers/test_byteplus_ecs.py
Verify BytePlus implementation conforms to ComputeProvider ABC
"""

import pytest
from providers.base import ComputeProvider
from providers.byteplus.provider import BytePlusProvider


def test_byteplus_implements_abc():
    assert issubclass(BytePlusProvider, ComputeProvider)

@pytest.mark.asyncio
async def test_byteplus_list_instances(byteplus_provider):
    instances = await byteplus_provider.list_instances()
    assert isinstance(instances, list)

@pytest.mark.asyncio
async def test_byteplus_start_instance(byteplus_provider):
    await byteplus_provider.start_instance("i-test-001")

@pytest.mark.asyncio
async def test_byteplus_stop_instance(byteplus_provider):
    await byteplus_provider.stop_instance("i-test-001")

@pytest.mark.asyncio
async def test_byteplus_reboot_instance(byteplus_provider):
    await byteplus_provider.reboot_instance("i-test-001")
