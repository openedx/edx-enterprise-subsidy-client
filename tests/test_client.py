"""
Tests for edx_enterprise_subsidy_client.py.
"""
from edx_enterprise_subsidy_client import EnterpriseSubsidyAPIClient


def test_client_init():
    """
    Tests that the client can be successfully initialized.
    """
    subsidy_client = EnterpriseSubsidyAPIClient()
    assert subsidy_client is not None
