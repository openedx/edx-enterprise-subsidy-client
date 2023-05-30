"""
Tests for edx_enterprise_subsidy_client.py.
"""
import uuid
from unittest import mock

from edx_enterprise_subsidy_client import EnterpriseSubsidyAPIClient, EnterpriseSubsidyAPIClientV2
from test_utils.utils import MockResponse


def test_client_init():
    """
    Tests that the client can be successfully initialized.
    """
    subsidy_client = EnterpriseSubsidyAPIClient()
    assert subsidy_client is not None


@mock.patch('edx_enterprise_subsidy_client.client.OAuthAPIClient', return_value=mock.MagicMock())
def test_client_fetch_subsidy_content_data_success(
    mock_oauth_client,
):
    """
    Test the client's ability to handle api requests to fetch subsidy content metadata from the subsidy service
    """
    course_key = 'edX+DemoX'
    mocked_data = {
        'content_uuid': '484ad134-8004-43b3-ad56-b57c83e4ba24',
        'content_key': course_key,
        'source': 'edX',
        'content_price': '149.00'
    }
    mock_oauth_client.return_value.get.return_value = MockResponse(mocked_data, 200)
    subsidy_service_client = EnterpriseSubsidyAPIClient()
    response = subsidy_service_client.get_subsidy_content_data(
        enterprise_customer_uuid='6d3ad134-8004-43b3-ad56-c57c83e4ea21',
        content_identifier=course_key
    )
    assert response == mocked_data


@mock.patch('edx_enterprise_subsidy_client.client.OAuthAPIClient', return_value=mock.MagicMock())
def test_v2_list_subsidy_transactions(
    mock_oauth_client,
):
    """
    Test the v2 client's ability to make API requests to the admin/transactions list view.
    Really just tests some method signatures.
    """
    mocked_response_data = {
        'next': None,
        'previous': None,
        'count': 0,
        'results': 0,
    }
    mock_oauth_client.return_value.get.return_value = MockResponse(mocked_response_data, 200)

    subsidy_uuid = uuid.uuid4()
    lms_user_id = 123
    content_key = 'the-best-content'
    subsidy_access_policy_uuid = uuid.uuid4()

    subsidy_service_client = EnterpriseSubsidyAPIClientV2()

    data_driven_test = [
        (
            {
                'page_size': 1,
                'transaction_states': ['committed', 'pending', 'district-of-columbia'],
            },
            ['committed', 'pending'],
        ),
        (
            {'page_size': 1},
            ['committed', 'pending', 'created'],
        ),
    ]
    for kwargs, expected_state_call_param in data_driven_test:
        response = subsidy_service_client.list_subsidy_transactions(
            subsidy_uuid=subsidy_uuid,
            lms_user_id=lms_user_id,
            content_key=content_key,
            subsidy_access_policy_uuid=subsidy_access_policy_uuid,
            **kwargs,
        )

        assert response == mocked_response_data
        mock_oauth_client.return_value.get.assert_called_with(
            f'enterprise-subsidy-service-base-url/api/v2/subsidies/{subsidy_uuid}/admin/transactions/',
            params={
                'state': expected_state_call_param,
                'include_aggregates': True,
                'lms_user_id': 123,
                'content_key': 'the-best-content',
                'subsidy_access_policy_uuid': str(subsidy_access_policy_uuid),
                'page_size': 1,
            },
        )
