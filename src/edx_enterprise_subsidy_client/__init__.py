"""
Client for interacting with the enterprise-subsidy service..
"""
from importlib.metadata import version

from .client import EnterpriseSubsidyAPIClient, EnterpriseSubsidyAPIClientV2, get_enterprise_subsidy_api_client

__version__ = version("edx-enterprise-subsidy-client")
