"""
Tests for edx_enterprise_subsidy_client.py.
"""
from unittest import mock

from edx_enterprise_subsidy_client import EnterpriseSubsidyAPIClient
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
