"""
tests/test_health.py
Verify API health & readiness endpoints
"""

def test_health_endpoint_gets_200(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json().get("status") in ("ok", "healthy")
