"""
API client for interacting with the enterprise-subsidy service.
"""
import logging
from urllib.parse import urljoin

import requests
from django.conf import settings
from edx_rest_api_client.client import OAuthAPIClient

logger = logging.getLogger(__name__)


class EnterpriseSubsidyAPIClient:
    """
    API client for calls to the enterprise-subsidy service.

    To use this within your service, ensure the service's settings contain the following vars:
    ENTERPRISE_BACKEND_SERVICE_EDX_OAUTH2_PROVIDER_URL=backend-service-oauth-provider-url
    ENTERPRISE_BACKEND_SERVICE_EDX_OAUTH2_KEY=your-services-application-key
    ENTERPRISE_BACKEND_SERVICE_EDX_OAUTH2_SECRET=your-services-application-secret
    ENTERPRISE_SUBSIDY_URL=enterprise-subsidy-service-base-url
    """

    API_BASE_URL = settings.ENTERPRISE_SUBSIDY_URL.strip('/') + '/api/v1/'
    SUBSIDIES_ENDPOINT = API_BASE_URL + 'subsidies/'
    TRANSACTIONS_ENDPOINT = API_BASE_URL + 'transactions/'
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
            if exc.request.status_code == 404:
                logger.error('Failed to fetch subsidy data- 404 content not found')
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
        self, subsidy_uuid, include_aggregates=True, lms_user_id=None, content_key=None
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

    def create_subsidy_transaction(self, subsidy_uuid, lms_user_id, content_key, subsidy_access_policy_uuid):
        """
        TODO: add docstring.
        """
        request_payload = {
            'subsidy_uuid': subsidy_uuid,
            'learner_id': lms_user_id,
            'content_key': content_key,
            'subsidy_access_policy_uuid': subsidy_access_policy_uuid,
        }
        response = self.client.post(
            self.TRANSACTIONS_ENDPOINT,
            json=request_payload,
        )
        print(response.json())
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
