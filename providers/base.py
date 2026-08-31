Here's **`providers/base.py`** — the clean, production-ready abstract base that enforces your provider interface perfectly. The Agent will **only depend on this ABC**, never on concrete implementations. ✅

```python
"""
providers/base.py
Core Architecture: Abstract Base Class for all Compute Providers
Agent depends ONLY on this interface — completely provider-agnostic.
"""

from abc import ABC, abstractmethod
from typing import Any, List


class ComputeProvider(ABC):
    """
    Abstract interface for compute instance management.
    Every cloud/provider must implement these methods.

    ⚠️ The Agent ONLY talks to this ABC.
    Implementation does NOT matter:
        BytePlus | AWS | Azure | GCP | Mock | Local Docker | Kubernetes
    """

    @abstractmethod
    async def list_instances(self) -> List[Any]:
        """List all instances visible to this provider."""
        raise NotImplementedError

    @abstractmethod
    async def start_instance(self, instance_id: str) -> None:
        """Start a stopped instance."""
        raise NotImplementedError

    @abstractmethod
    async def stop_instance(self, instance_id: str) -> None:
        """Stop a running instance."""
        raise NotImplementedError

    @abstractmethod
    async def reboot_instance(self, instance_id: str) -> None:
        """Reboot an instance."""
        raise NotImplementedError
```

---

### 🧱 Architecture — How It Fits
```
                     ┌──────────────┐
                     │    AGENT     │
                     │ (NO CLOUD CODE)
                     └──────┬───────┘
                            │  only calls ComputeProvider ABC
                     ┌──────▼──────────────┐
                     │  ComputeProvider    │  ← base.py — your contract
                     │  (abstract methods) │
                     └──┬──────┬──────┬────┘
                        │      │      │
          ┌──────────────┼───┐  │  ┌───┼──────────────┐
     BytePlusProvider    │  AWSProvider  │    MockProvider
     (byteplus/)       GCP/Azure...    (local/test)
```

### ✅ Key Principles Enforced
- **Single contract** — all providers implement exactly the same 4 methods
- **Zero business logic** — base.py defines only the **shape**, never the **implementation**
- **Agent-agnostic** — import `ComputeProvider`, never `BytePlusClient` or AWS SDK directly
- **Test-friendly** — swap any provider with `MockProvider()` in 1 line, zero code changes
- **Async-first** — all methods are `async` so every implementation stays consistent

### 📌 Example — BytePlus Implements It
```python
# providers/byteplus/provider.py
from providers.base import ComputeProvider
from providers.byteplus.client import BytePlusClient  # ← only config/credentials

class BytePlusProvider(ComputeProvider):
    def __init__(self):
        self.client = BytePlusClient()  # ← credentials/config only

    async def list_instances(self):
        # uses self.client.* to call BytePlus API
        ...

    async def start_instance(self, instance_id: str):
        ...

    async def stop_instance(self, instance_id: str):
        ...

    async def reboot_instance(self, instance_id: str):
        ...
```

### 🧠 Agent Usage (Clean & Simple)
```python
class Agent:
    def __init__(self, provider: ComputeProvider):
        # Agent knows NOTHING about BytePlus/AWS/GCP
        self.provider = provider

    async def restart_all(self):
        instances = await self.provider.list_instances()
        for inst in instances:
            await self.provider.reboot_instance(inst.id)
```

---

### 📂 Recommended Folder Structure
```
providers/
├── base.py               # ← THIS FILE — ComputeProvider ABC
├── byteplus/
│   ├── __init__.py
│   ├── client.py         # credentials & config only
│   └── provider.py       # implements ComputeProvider
├── aws/
├── gcp/
├── azure/
├── mock.py                # test-friendly fake implementation
└── docker_local.py        # local dev implementation
```

Want me to generate:
1. **`mock.py`** — a fake in-memory provider for fast unit tests (no API calls)?
2. **Full `byteplus/provider.py`** — implements this ABC using your `BytePlusClient`?
