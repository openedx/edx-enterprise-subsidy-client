"""
API client for interacting with the enterprise-subsidy service.
"""
import logging

import requests  # pylint: disable=unused-import
from django.conf import settings
from edx_rest_api_client.client import OAuthAPIClient

logger = logging.getLogger(__name__)


class EnterpriseSubsidyAPIClient:
    """
    API client for calls to the enterprise-subsidy service.

    To use this within your service, ensure the service's settings contain the following vars:
    SOCIAL_AUTH_EDX_OAUTH2_URL_ROOT=root-url-for-oauth-2
    BACKEND_SERVICE_EDX_OAUTH2_KEY=your-services-application-key
    BACKEND_SERVICE_EDX_OAUTH2_SECRET=your-services-application-secret
    ENTERPRISE_SUBSIDY_URL=enterprise-subsidy-service-base-url
    """

    API_BASE_URL = settings.ENTERPRISE_SUBSIDY_URL.strip('/') + '/api/v1/'
    SUBSIDIES_ENDPOINT = API_BASE_URL + 'subsidies/'
    TRANSACTIONS_ENDPOINT = API_BASE_URL + 'subsidies/{subsidy_uuid}/transactions/'

    def __init__(self):
        """
        Initializes the OAuthAPIClient instance.
        """
        self.client = OAuthAPIClient(
            settings.SOCIAL_AUTH_EDX_OAUTH2_URL_ROOT.strip('/'),
            settings.BACKEND_SERVICE_EDX_OAUTH2_KEY,
            settings.BACKEND_SERVICE_EDX_OAUTH2_SECRET,
        )

    def list_subsidies(self, enterprise_uuid=None, subsidy_type=None):
        """
        TODO: add docstring.
        """
        raise NotImplementedError

    def retrieve_subsidy(self, subsidy_uuid):
        """
        TODO: add docstring.
        """
        raise NotImplementedError

    def list_subsidy_transactions(
        self, subsidy_uuid, include_aggregates=True, user_id=None, content_key=None,
    ):
        """
        TODO: add docstring.
        """
        raise NotImplementedError

    def retrieve_subsidy_transaction(self, subsidy_uuid, transaction_uuid):
        """
        TODO: add docstring.
        """
        raise NotImplementedError

    def create_subsidy_transaction(self, subsidy_uuid, user_id, content_key, **kwargs):
        """
        TODO: add docstring.
        """
        raise NotImplementedError

    def reverse_subsidy_transaction(self, subsidy_uuid, transaction_uuid):
        """
        TODO: add docstring.
        """
        raise NotImplementedError

    def can_redeem(self, subsidy_uuid, user_id, content_key):
        """
        TODO: add docstring.
        """
        raise NotImplementedError
