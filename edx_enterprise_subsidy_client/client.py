"""
API client for interacting with the enterprise-subsidy service.
"""
import logging

import requests
from django.conf import settings
from edx_rest_api_client.client import OAuthAPIClient

logger = logging.getLogger(__name__)


class TransactionStateChoices:
    """
    Lifecycle states for a ledger transaction.
    """

    CREATED = 'created'
    PENDING = 'pending'
    COMMITTED = 'committed'
    FAILED = 'failed'

    VALID_CHOICES = {
        CREATED,
        PENDING,
        COMMITTED,
        FAILED,
    }


class EnterpriseSubsidyAPIClientException(Exception):
    """
    A general exception to represent non-http errors
    arising during Subsidy API client usage.
    """


def get_enterprise_subsidy_api_client(version=1):
    """
    Helper to get a versioned client.
    """
    assert version in [1, 2]
    if version == 1:
        return EnterpriseSubsidyAPIClient()
    if version == 2:
        return EnterpriseSubsidyAPIClientV2()
    raise EnterpriseSubsidyAPIClientException(f'{version} is not a valid version!')


class EnterpriseSubsidyAPIClient:
    """
    API client for calls to the enterprise-subsidy service.

    To use this within your service, ensure the service's settings contain the following vars:
    OAUTH2_PROVIDER_URL=backend-service-oauth-provider-url
    BACKEND_SERVICE_EDX_OAUTH2_KEY=your-services-application-key
    BACKEND_SERVICE_EDX_OAUTH2_SECRET=your-services-application-secret
    ENTERPRISE_SUBSIDY_URL=enterprise-subsidy-service-base-url
    """
    API_BASE_URL = settings.ENTERPRISE_SUBSIDY_URL.strip('/') + '/api/'
    V1_BASE_URL = API_BASE_URL + 'v1/'
    SUBSIDIES_ENDPOINT = V1_BASE_URL + 'subsidies/'
    TRANSACTIONS_ENDPOINT = V1_BASE_URL + 'transactions/'
    CONTENT_METADATA_ENDPOINT = V1_BASE_URL + 'content-metadata/'

    def __init__(self):
        """
        Initializes the OAuthAPIClient instance.
        """
        self.client = OAuthAPIClient(
            settings.OAUTH2_PROVIDER_URL,
            settings.BACKEND_SERVICE_EDX_OAUTH2_KEY,
            settings.BACKEND_SERVICE_EDX_OAUTH2_SECRET,
        )

    def get_content_metadata_url(self, content_identifier):
        """Helper method to generate the subsidy service metadata API url."""
        return self.CONTENT_METADATA_ENDPOINT + content_identifier

    def get_subsidy_content_data(self, enterprise_customer_uuid, content_identifier):
        """
        Client method to fetch enterprise specific content data.

        Args:
            enterprise_customer_uuid (str): Enterprise customer UUID
            content_identifier (str): Either content key or UUID for the associated content to be fetched
        Returns:
            json subsidy content data response:
                {
                    'content_uuid': '484ad134-8004-43b3-ad56-b57c83e4ba24',
                    'content_key': 'edX+DemoX',
                    'source': 'edX',
                    'content_price': '149.00'
                }
        """
        try:
            resp = self.client.get(
                self.get_content_metadata_url(content_identifier),
                params={'enterprise_customer_uuid': enterprise_customer_uuid}
            )
            response_data = resp
            resp.raise_for_status()
        except requests.exceptions.HTTPError as exc:
            logger.exception(
                f'Subsidy client failed to fetch content metadata for {content_identifier} '
                f'in customer {enterprise_customer_uuid}'
            )
            raise exc
        return response_data.json()

    def list_subsidies(self, enterprise_customer_uuid):
        """
        Client method to list enterprise subsidy records for the given enterprise_customer_uuid.

        Args:
            enterprise_customer_uuid (str): Enterprise customer UUID
        Returns:
            Paginated response of serialized Subsidy records:
            ```
            {
                "count": 123,
                "next": "http://api.example.org/accounts/?page=4",
                "previous": "http://api.example.org/accounts/?page=2",
                "results": [
                  {
                    "uuid": "095be615-a8ad-4c33-8e9c-c7612fbf6c9f",
                    "title": "string",
                    "enterprise_customer_uuid": "fdfda46b-94d9-42dc-a755-6e2ed472a413",
                    "active_datetime": "2019-08-24T14:15:22Z",
                    "expiration_datetime": "2019-08-24T14:15:22Z",
                    "unit": "usd_cents",
                    "reference_id": "string",
                    "reference_type": "opportunity_product_id",
                    "current_balance": "string"
                  }
                ]
              }
            ```
        """
        response = self.client.get(
            self.SUBSIDIES_ENDPOINT,
            params={'enterprise_customer_uuid': enterprise_customer_uuid}
        )
        response.raise_for_status()
        return response.json()

    def retrieve_subsidy(self, subsidy_uuid):
        """
        TODO: add docstring.
        """
        response = self.client.get(
            self.SUBSIDIES_ENDPOINT + f'{subsidy_uuid}/'
        )
        response.raise_for_status()
        return response.json()

    def list_subsidy_transactions(
        self, subsidy_uuid, include_aggregates=True,
        lms_user_id=None, content_key=None,
        subsidy_access_policy_uuid=None,
    ):
        """
        TODO: add docstring.
        """
        query_params = {'subsidy_uuid': subsidy_uuid}
        if include_aggregates:
            query_params['include_aggregates'] = include_aggregates
        if lms_user_id:
            query_params['lms_user_id'] = lms_user_id
        if content_key:
            query_params['content_key'] = content_key
        if subsidy_access_policy_uuid:
            query_params['subsidy_access_policy_uuid'] = str(subsidy_access_policy_uuid)

        response = self.client.get(
            self.TRANSACTIONS_ENDPOINT,
            params=query_params,
        )
        response.raise_for_status()
        return response.json()

    def retrieve_subsidy_transaction(self, transaction_uuid):
        """
        TODO: add docstring.
        """
        response = self.client.get(
            self.TRANSACTIONS_ENDPOINT + f'{transaction_uuid}/'
        )
        response.raise_for_status()
        return response.json()

    def create_subsidy_transaction(self, subsidy_uuid, lms_user_id, content_key, subsidy_access_policy_uuid, metadata):
        """
        TODO: add docstring.
        """
        request_payload = {
            'subsidy_uuid': str(subsidy_uuid),
            'lms_user_id': lms_user_id,
            'content_key': content_key,
            'subsidy_access_policy_uuid': str(subsidy_access_policy_uuid),
            'metadata': metadata,
        }
        response = self.client.post(
            self.TRANSACTIONS_ENDPOINT,
            json=request_payload,
        )
        response.raise_for_status()
        return response.json()

    def reverse_subsidy_transaction(self, subsidy_uuid, transaction_uuid):
        """
        TODO: add docstring.
        """
        raise NotImplementedError

    def can_redeem(self, subsidy_uuid, lms_user_id, content_key):
        """
        TODO: add docstring.
        """
        query_params = {
            'lms_user_id': lms_user_id,
            'content_key': content_key,
        }
        response = self.client.get(
            self.SUBSIDIES_ENDPOINT + f'{subsidy_uuid}/can_redeem/',
            params=query_params,
        )
        response.raise_for_status()
        return response.json()


class EnterpriseSubsidyAPIClientV2(EnterpriseSubsidyAPIClient):  # pylint: disable=abstract-method
    """
    API client for calls to the enterprise-subsidy service.  Supports v2 transaction
    admin list and create actions.

    To use this within your service, ensure the service's settings contain the following vars:
    OAUTH2_PROVIDER_URL=backend-service-oauth-provider-url
    BACKEND_SERVICE_EDX_OAUTH2_KEY=your-services-application-key
    BACKEND_SERVICE_EDX_OAUTH2_SECRET=your-services-application-secret
    ENTERPRISE_SUBSIDY_URL=enterprise-subsidy-service-base-url
    """
    V2_BASE_URL = EnterpriseSubsidyAPIClient.API_BASE_URL + 'v2/'
    TRANSACTIONS_LIST_ENDPOINT = V2_BASE_URL + 'subsidies/{subsidy_uuid}/admin/transactions/'

    def list_subsidy_transactions(
        self, subsidy_uuid, include_aggregates=True,
        lms_user_id=None, content_key=None,
        subsidy_access_policy_uuid=None, transaction_states=None,
    ):
        """
        List transactions in a subsidy with admin- or operator-level permissions.
        """
        query_params = {
            'state': [TransactionStateChoices.COMMITTED, TransactionStateChoices.PENDING],
        }
        if include_aggregates:
            query_params['include_aggregates'] = include_aggregates
        if lms_user_id:
            query_params['lms_user_id'] = lms_user_id
        if content_key:
            query_params['content_key'] = content_key
        if subsidy_access_policy_uuid:
            query_params['subsidy_access_policy_uuid'] = str(subsidy_access_policy_uuid)
        if transaction_states:
            valid_states = [
                state for state in transaction_states
                if state in TransactionStateChoices.VALID_CHOICES
            ]
            query_params['state'] = valid_states

        response = self.client.get(
            self.TRANSACTIONS_LIST_ENDPOINT.format(subsidy_uuid=subsidy_uuid),
            params=query_params,
        )
        response.raise_for_status()
        return response.json()

    def create_subsidy_transaction(self, subsidy_uuid, lms_user_id, content_key, subsidy_access_policy_uuid, metadata):
        """
        Creates a transaction in the given subsidy, requires operator-level permissions.
        """
        request_payload = {
            'subsidy_uuid': str(subsidy_uuid),
            'lms_user_id': lms_user_id,
            'content_key': content_key,
            'subsidy_access_policy_uuid': str(subsidy_access_policy_uuid),
            'metadata': metadata,
        }
        response = self.client.post(
            self.TRANSACTIONS_LIST_ENDPOINT.format(subsidy_uuid=subsidy_uuid),
            json=request_payload,
        )
        response.raise_for_status()
        return response.json()
