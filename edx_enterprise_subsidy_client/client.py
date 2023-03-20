"""
API client for interacting with the enterprise-subsidy service.
"""
import logging
from urllib.parse import urljoin

import requests  # pylint: disable=unused-import
from django.conf import settings
from edx_rest_api_client.client import OAuthAPIClient

logger = logging.getLogger(__name__)


class EnterpriseSubsidyAPIClient:
    """
    API client for calls to the enterprise-subsidy service.

    To use this within your service, ensure the service's settings contain the following vars:
    BACKEND_SERVICE_EDX_OAUTH2_KEY=your-services-application-key
    BACKEND_SERVICE_EDX_OAUTH2_SECRET=your-services-application-secret
    ENTERPRISE_SUBSIDY_URL=enterprise-subsidy-service-base-url
    """

    API_BASE_URL = settings.ENTERPRISE_SUBSIDY_URL.strip('/') + '/api/v1/'
    SUBSIDIES_ENDPOINT = API_BASE_URL + 'subsidies/'
    TRANSACTIONS_ENDPOINT = API_BASE_URL + 'subsidies/{subsidy_uuid}/transactions/'
    CONTENT_METADATA_ENDPOINT = API_BASE_URL + 'content-metadata/'

    def __init__(self):
        """
        Initializes the OAuthAPIClient instance.
        """
        self.client = OAuthAPIClient(
            settings.ENTERPRISE_BACKEND_SERVICE_EDX_OAUTH2_PROVIDER_URL.strip('/'),
            settings.ENTERPRISE_BACKEND_SERVICE_EDX_OAUTH2_KEY,
            settings.ENTERPRISE_BACKEND_SERVICE_EDX_OAUTH2_SECRET,
        )

    def get_content_metadata_url(self, content_identifier):
        """
        Helper method to generate the subsidy service metadata API url
        """
        return urljoin(self.CONTENT_METADATA_ENDPOINT, content_identifier)

    def get_subsidy_content_data(self, enterprise_uuid, content_identifier):
        """
        Client method to fetch enterprise specific content data (ie price and product source) from the subsidy service.
        Content identifier can be either content key or content uuid.
        """
        try:
            resp = self.client.get(
                self.get_content_metadata_url(content_identifier) +
                f"?enterprise_customer_uuid={enterprise_uuid}"
            )
            response_data = resp
            resp.raise_for_status()
        except requests.exceptions.HTTPError as exc:
            if exc.request.status_code == 404:
                logger.error(f'Failed to fetch subsidy data- 404 content not found')
            raise exc
        return response_data.json()

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
