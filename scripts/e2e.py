"""
Hacky script for testing end-to-end flow between the client, enterprise-subsidy service, and the
edx-enterprise enrollment layer.
"""
from uuid import uuid4
from django.conf import settings
from pprint import pprint
settings.ENTERPRISE_SUBSIDY_URL = 'http://enterprise-subsidy.app:18280'
from edx_enterprise_subsidy_client import EnterpriseSubsidyAPIClient
client = EnterpriseSubsidyAPIClient()
enterprise_customer_uuid = '70699d54-7504-4429-8295-e1c0ec68dbc7'  # Test Enterprise
content_key = 'course-v1:edX+DemoX+Demo_Course'

print('\nget_content_data\n')
pprint(client.get_subsidy_content_data(enterprise_customer_uuid, content_key))

print('\nlist_subsidies\n')
subsidy_list = client.list_subsidies(enterprise_customer_uuid)
pprint(subsidy_list)

print('\nretrieve_subsidy\n')
subsidy_uuid = subsidy_list['results'][0]['uuid']
pprint(client.retrieve_subsidy(subsidy_uuid))

print('list_subsidy_transactions')
pprint(client.list_subsidy_transactions(subsidy_uuid))

# TODO: known to break
# transaction_uuid = '3631785b-d3ff-41eb-80a4-e61529098592' # initial tx for this subsidy
# print('\nretrieve transaction\n')
# pprint(client.retrieve_subsidy_transaction(transaction_uuid))

print('\ncan_redeem\n')
lms_user_id = 13 # verified@example.com, member of Test Enterprise
pprint(client.can_redeem(subsidy_uuid, lms_user_id, content_key))

print('\ncreate_subsidy_transaction\n')
subsidy_access_policy_uuid = str(uuid4())
pprint(client.create_subsidy_transaction(
    subsidy_uuid, lms_user_id, content_key, subsidy_access_policy_uuid
))
