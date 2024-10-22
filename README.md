# flowhunt-python-sdk
FlowHunt API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.0.0
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/flowhunt-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/flowhunt-python-sdk.git`)

Then import the package:
```python
import flowhunt-python-sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import flowhunt-python-sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import flowhunt-python-sdk
from flowhunt-python-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = flowhunt-python-sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = flowhunt-python-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with flowhunt-python-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = flowhunt-python-sdk.ApiKeysApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    api_key_create_request = flowhunt-python-sdk.ApiKeyCreateRequest() # ApiKeyCreateRequest | 

    try:
        # Create Api Key
        api_response = api_instance.create_api_key(workspace_id, api_key_create_request)
        print("The response of ApiKeysApi->create_api_key:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiKeysApi->create_api_key: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiKeysApi* | [**create_api_key**](docs/ApiKeysApi.md#create_api_key) | **POST** /v2/api_keys/create | Create Api Key
*ApiKeysApi* | [**delete_api_key**](docs/ApiKeysApi.md#delete_api_key) | **DELETE** /v2/api_keys/{api_key_id} | Delete Api Key
*ApiKeysApi* | [**search_api_key**](docs/ApiKeysApi.md#search_api_key) | **POST** /v2/api_keys/search | Search Api Key
*ApiKeysApi* | [**update_api_key**](docs/ApiKeysApi.md#update_api_key) | **PUT** /v2/api_keys/{api_key_id} | Update Api Key
*AuthApi* | [**activate_user**](docs/AuthApi.md#activate_user) | **GET** /v2/auth/activate | Activate User
*AuthApi* | [**get_third_party_token**](docs/AuthApi.md#get_third_party_token) | **POST** /v2/auth/token/{provider_name} | Get Third Party Token
*AuthApi* | [**get_token**](docs/AuthApi.md#get_token) | **POST** /v2/auth/token | Get Token
*AuthApi* | [**get_user**](docs/AuthApi.md#get_user) | **GET** /v2/auth/me | Get User
*AuthApi* | [**recover_password**](docs/AuthApi.md#recover_password) | **POST** /v2/auth/password-recovery/{email} | Recover Password
*AuthApi* | [**refresh_token**](docs/AuthApi.md#refresh_token) | **POST** /v2/auth/refresh-token | Refresh Token
*AuthApi* | [**register_user**](docs/AuthApi.md#register_user) | **POST** /v2/auth/ | Register User
*AuthApi* | [**reset_password**](docs/AuthApi.md#reset_password) | **POST** /v2/auth/reset-password | Reset Password
*BillingApi* | [**create_change_plan_portal**](docs/BillingApi.md#create_change_plan_portal) | **POST** /v2/billing/portal/change-plan/create | Create Change Plan Portal
*BillingApi* | [**create_checkout**](docs/BillingApi.md#create_checkout) | **POST** /v2/billing/checkout/create | Create Checkout
*BillingApi* | [**create_update_info_portal**](docs/BillingApi.md#create_update_info_portal) | **POST** /v2/billing/portal/update-info/create | Create Update Info Portal
*BillingApi* | [**get_pricing_plans**](docs/BillingApi.md#get_pricing_plans) | **GET** /v2/billing/plans | Get Pricing Plans
*BillingApi* | [**get_user_plan**](docs/BillingApi.md#get_user_plan) | **GET** /v2/billing/plans/me | Get User Plan
*BillingApi* | [**stripe_webhook**](docs/BillingApi.md#stripe_webhook) | **POST** /v2/billing/webhook | Stripe Webhook
*ChatbotsApi* | [**create_chatbot**](docs/ChatbotsApi.md#create_chatbot) | **POST** /v2/chatbots/create | Create Chatbot
*ChatbotsApi* | [**delete_chatbot**](docs/ChatbotsApi.md#delete_chatbot) | **DELETE** /v2/chatbots/{chatbot_id} | Delete Chatbot
*ChatbotsApi* | [**get_chatbot**](docs/ChatbotsApi.md#get_chatbot) | **GET** /v2/chatbots/{chatbot_id} | Get Chatbot
*ChatbotsApi* | [**search_chatbots**](docs/ChatbotsApi.md#search_chatbots) | **POST** /v2/chatbots/ | Search Chatbots
*ChatbotsApi* | [**update_chatbot**](docs/ChatbotsApi.md#update_chatbot) | **PUT** /v2/chatbots/{chatbot_id} | Update Chatbot
*CreditsApi* | [**get_credit_balance**](docs/CreditsApi.md#get_credit_balance) | **GET** /v2/credits/balance | Get Credit Balance
*CreditsApi* | [**get_workspace_credit_balance**](docs/CreditsApi.md#get_workspace_credit_balance) | **GET** /v2/credits/workspace_balance | Get Workspace Credit Balance
*CreditsApi* | [**search_credit_transactions**](docs/CreditsApi.md#search_credit_transactions) | **POST** /v2/credits/search | Search Credit Transactions
*CreditsApi* | [**search_daily_credit_transactions**](docs/CreditsApi.md#search_daily_credit_transactions) | **POST** /v2/credits/search_daily | Search Daily Credit Transactions
*DocumentsApi* | [**create_document_category**](docs/DocumentsApi.md#create_document_category) | **POST** /v2/documents/categories/create | Create Document Category
*DocumentsApi* | [**create_faq**](docs/DocumentsApi.md#create_faq) | **POST** /v2/documents/faqs/create | Create Faq
*DocumentsApi* | [**delete_document**](docs/DocumentsApi.md#delete_document) | **DELETE** /v2/documents/{doc_id} | Delete Document
*DocumentsApi* | [**delete_document_category**](docs/DocumentsApi.md#delete_document_category) | **DELETE** /v2/documents/categories/{cat_id} | Delete Document Category
*DocumentsApi* | [**delete_faq**](docs/DocumentsApi.md#delete_faq) | **DELETE** /v2/documents/faqs/{faq_id} | Delete Faq
*DocumentsApi* | [**download_binary_document**](docs/DocumentsApi.md#download_binary_document) | **GET** /v2/documents/download/binary/{doc_id} | Download Binary Document
*DocumentsApi* | [**download_text_document**](docs/DocumentsApi.md#download_text_document) | **GET** /v2/documents/download/text/{doc_id} | Download Text Document
*DocumentsApi* | [**search_document_categories**](docs/DocumentsApi.md#search_document_categories) | **POST** /v2/documents/categories/search | Search Document Categories
*DocumentsApi* | [**search_documents**](docs/DocumentsApi.md#search_documents) | **POST** /v2/documents/search | Search Documents
*DocumentsApi* | [**search_faqs**](docs/DocumentsApi.md#search_faqs) | **POST** /v2/documents/faqs/search | Search Faqs
*DocumentsApi* | [**update_document**](docs/DocumentsApi.md#update_document) | **PUT** /v2/documents/{doc_id} | Update Document
*DocumentsApi* | [**update_document_category**](docs/DocumentsApi.md#update_document_category) | **PUT** /v2/documents/categories/{cat_id} | Update Document Category
*DocumentsApi* | [**update_faq**](docs/DocumentsApi.md#update_faq) | **PUT** /v2/documents/faqs/{faq_id} | Update Faq
*DocumentsApi* | [**upload_document**](docs/DocumentsApi.md#upload_document) | **POST** /v2/documents/upload/{cat_id} | Upload Document
*DocumentsApi* | [**upload_from_url_document**](docs/DocumentsApi.md#upload_from_url_document) | **POST** /v2/documents/upload-from-url/{cat_id} | Upload From Url Document
*FlowMessagesApi* | [**search_flow_messages**](docs/FlowMessagesApi.md#search_flow_messages) | **POST** /v2/chatbots/search/{session_id} | Search Flow Messages
*FlowSessionsApi* | [**delete_chatbot_session_view**](docs/FlowSessionsApi.md#delete_chatbot_session_view) | **DELETE** /v2/chatbots/sessions/{session_id} | Delete Chatbot Session View
*FlowSessionsApi* | [**get_chatbot_session_view**](docs/FlowSessionsApi.md#get_chatbot_session_view) | **GET** /v2/chatbots/sessions/{session_id} | Get Chatbot Session View
*FlowSessionsApi* | [**search_chatbot_sessions_view**](docs/FlowSessionsApi.md#search_chatbot_sessions_view) | **POST** /v2/chatbots/sessions/search | Search Chatbot Sessions View
*FlowSessionsApi* | [**update_chatbot_session_view**](docs/FlowSessionsApi.md#update_chatbot_session_view) | **PUT** /v2/chatbots/sessions/{session_id} | Update Chatbot Session View
*FlowWebhooksApi* | [**execute_webhook**](docs/FlowWebhooksApi.md#execute_webhook) | **POST** /v2/flows/webhooks/{chatbot_id} | Execute Webhook
*FlowWebhooksApi* | [**execute_webhook_from_flow**](docs/FlowWebhooksApi.md#execute_webhook_from_flow) | **POST** /v2/flows/webhooks/from_flow/{flow_id} | Execute Webhook From Flow
*FlowWebhooksApi* | [**poll_webhook_response**](docs/FlowWebhooksApi.md#poll_webhook_response) | **POST** /v2/flows/webhooks/invocation_response/{message_id} | Poll Webhook Response
*FlowsApi* | [**create_chatbot_session**](docs/FlowsApi.md#create_chatbot_session) | **POST** /v2/flows/sessions/create | Create Chatbot Session
*FlowsApi* | [**create_flow**](docs/FlowsApi.md#create_flow) | **POST** /v2/flows/create | Create Flow
*FlowsApi* | [**create_flow_category**](docs/FlowsApi.md#create_flow_category) | **POST** /v2/flows/categories/create | Create Flow Category
*FlowsApi* | [**create_flow_session**](docs/FlowsApi.md#create_flow_session) | **POST** /v2/flows/sessions/from_flow/create | Create Flow Session
*FlowsApi* | [**delete_attachment**](docs/FlowsApi.md#delete_attachment) | **DELETE** /v2/flows/sessions/{session_id}/attachments/{file_id} | Delete Attachment
*FlowsApi* | [**delete_flow**](docs/FlowsApi.md#delete_flow) | **DELETE** /v2/flows/{flow_id} | Delete Flow
*FlowsApi* | [**delete_flow_category**](docs/FlowsApi.md#delete_flow_category) | **DELETE** /v2/flows/categories/{cat_id} | Delete Flow Category
*FlowsApi* | [**get**](docs/FlowsApi.md#get) | **GET** /v2/flows/{flow_id} | Get
*FlowsApi* | [**get_all_components**](docs/FlowsApi.md#get_all_components) | **GET** /v2/flows/components/all | Get All Components
*FlowsApi* | [**get_attachments**](docs/FlowsApi.md#get_attachments) | **GET** /v2/flows/sessions/{session_id}/attachments | Get Attachments
*FlowsApi* | [**get_invoked_flow_results**](docs/FlowsApi.md#get_invoked_flow_results) | **GET** /v2/flows/{flow_id}/{task_id} | Get Invoked Flow Results
*FlowsApi* | [**get_public_flow**](docs/FlowsApi.md#get_public_flow) | **GET** /v2/flows/public/{flow_id} | Get Public Flow
*FlowsApi* | [**invoke_flow**](docs/FlowsApi.md#invoke_flow) | **POST** /v2/flows/{flow_id}/invoke | Invoke Flow
*FlowsApi* | [**invoke_flow_response**](docs/FlowsApi.md#invoke_flow_response) | **POST** /v2/flows/sessions/{session_id}/invoke | Invoke Flow Response
*FlowsApi* | [**invoke_flow_singleton**](docs/FlowsApi.md#invoke_flow_singleton) | **POST** /v2/flows/{flow_id}/invoke_singleton | Invoke Flow Singleton
*FlowsApi* | [**poll_flow_response**](docs/FlowsApi.md#poll_flow_response) | **POST** /v2/flows/sessions/{session_id}/invocation_response/{message_id} | Poll Flow Response
*FlowsApi* | [**search**](docs/FlowsApi.md#search) | **POST** /v2/flows/ | Search
*FlowsApi* | [**search_flow_categories**](docs/FlowsApi.md#search_flow_categories) | **POST** /v2/flows/categories/search | Search Flow Categories
*FlowsApi* | [**stream_flow_response**](docs/FlowsApi.md#stream_flow_response) | **POST** /v2/flows/sessions/{session_id}/stream | Stream Flow Response
*FlowsApi* | [**update_flow**](docs/FlowsApi.md#update_flow) | **PUT** /v2/flows/{flow_id} | Update Flow
*FlowsApi* | [**update_flow_category**](docs/FlowsApi.md#update_flow_category) | **PUT** /v2/flows/categories/{cat_id} | Update Flow Category
*FlowsApi* | [**upload_attachments**](docs/FlowsApi.md#upload_attachments) | **POST** /v2/flows/sessions/{session_id}/attachments | Upload Attachments
*HealthApi* | [**health**](docs/HealthApi.md#health) | **GET** /v2/monitoring/health/ | Health
*ImagesApi* | [**convert_image**](docs/ImagesApi.md#convert_image) | **POST** /v2/images/convert | Convert Image
*ImagesApi* | [**get_screenshot**](docs/ImagesApi.md#get_screenshot) | **POST** /v2/images/screenshot | Get Screenshot
*ImagesApi* | [**optimize_image**](docs/ImagesApi.md#optimize_image) | **POST** /v2/images/optimize | Optimize Image
*IntegrationsApi* | [**create_api_integration**](docs/IntegrationsApi.md#create_api_integration) | **POST** /v2/integrations/api_integrations/create | Create Api Integration
*IntegrationsApi* | [**create_api_integration_endpoint**](docs/IntegrationsApi.md#create_api_integration_endpoint) | **POST** /v2/integrations/api_integrations/{integration_id}/endpoints/create | Create Api Integration Endpoint
*IntegrationsApi* | [**get_all_integrations**](docs/IntegrationsApi.md#get_all_integrations) | **GET** /v2/integrations/all | Get All Integrations
*IntegrationsApi* | [**get_api_integration**](docs/IntegrationsApi.md#get_api_integration) | **GET** /v2/integrations/api_integrations/ | Get Api Integration
*IntegrationsApi* | [**get_api_integration_auth_methods**](docs/IntegrationsApi.md#get_api_integration_auth_methods) | **GET** /v2/integrations/api_integrations/auth_methods | Get Api Integration Auth Methods
*IntegrationsApi* | [**get_api_integration_endpoints**](docs/IntegrationsApi.md#get_api_integration_endpoints) | **POST** /v2/integrations/api_integrations/{integration_id}/endpoints | Get Api Integration Endpoints
*IntegrationsApi* | [**get_api_integrations**](docs/IntegrationsApi.md#get_api_integrations) | **POST** /v2/integrations/api_integrations/ | Get Api Integrations
*IntegrationsApi* | [**get_my_integrations**](docs/IntegrationsApi.md#get_my_integrations) | **POST** /v2/integrations/ | Get My Integrations
*IntegrationsApi* | [**import_openapi_spec**](docs/IntegrationsApi.md#import_openapi_spec) | **POST** /v2/integrations/api_integrations/{integration_id}/import/openapi-file | Import Openapi Spec
*IntegrationsApi* | [**import_openapi_spec_from_url**](docs/IntegrationsApi.md#import_openapi_spec_from_url) | **POST** /v2/integrations/api_integrations/{integration_id}/import/openapi-url | Import Openapi Spec From Url
*IntegrationsApi* | [**remove_api_integration**](docs/IntegrationsApi.md#remove_api_integration) | **DELETE** /v2/integrations/api_integrations/{integration_id} | Remove Api Integration
*IntegrationsApi* | [**remove_api_integration_endpoint**](docs/IntegrationsApi.md#remove_api_integration_endpoint) | **DELETE** /v2/integrations/api_integrations/{integration_id}/endpoints/{endpoint_id} | Remove Api Integration Endpoint
*IntegrationsApi* | [**update_api_integration**](docs/IntegrationsApi.md#update_api_integration) | **PUT** /v2/integrations/api_integrations/{integration_id} | Update Api Integration
*IntegrationsApi* | [**update_api_integration_endpoint**](docs/IntegrationsApi.md#update_api_integration_endpoint) | **PUT** /v2/integrations/api_integrations/{integration_id}/endpoints/{endpoint_id} | Update Api Integration Endpoint
*MediaApi* | [**get_transcript**](docs/MediaApi.md#get_transcript) | **POST** /v2/media/transcript | Get Transcript
*MediaApi* | [**get_transcript_result**](docs/MediaApi.md#get_transcript_result) | **POST** /v2/media/transcript_status | Get Transcript Result
*MediaApi* | [**get_youtube_transcript**](docs/MediaApi.md#get_youtube_transcript) | **POST** /v2/media/youtube/transcript | Get Youtube Transcript
*PromptsApi* | [**create_prompt**](docs/PromptsApi.md#create_prompt) | **POST** /v2/prompts/create | Create Prompt
*PromptsApi* | [**create_prompt_category**](docs/PromptsApi.md#create_prompt_category) | **POST** /v2/prompts/categories/create | Create Prompt Category
*PromptsApi* | [**delete_prompt**](docs/PromptsApi.md#delete_prompt) | **DELETE** /v2/prompts/{prompt_id} | Delete Prompt
*PromptsApi* | [**delete_prompt_category**](docs/PromptsApi.md#delete_prompt_category) | **DELETE** /v2/prompts/categories/{cat_id} | Delete Prompt Category
*PromptsApi* | [**search_prompt_categories**](docs/PromptsApi.md#search_prompt_categories) | **POST** /v2/prompts/categories/search | Search Prompt Categories
*PromptsApi* | [**search_prompts**](docs/PromptsApi.md#search_prompts) | **POST** /v2/prompts/search | Search Prompts
*PromptsApi* | [**update_prompt**](docs/PromptsApi.md#update_prompt) | **PUT** /v2/prompts/{prompt_id} | Update Prompt
*PromptsApi* | [**update_prompt_category**](docs/PromptsApi.md#update_prompt_category) | **PUT** /v2/prompts/categories/{cat_id} | Update Prompt Category
*SERPApi* | [**serp_search**](docs/SERPApi.md#serp_search) | **POST** /v2/serp/serp/search | Serp Search
*SERPApi* | [**serp_volumes**](docs/SERPApi.md#serp_volumes) | **POST** /v2/serp/serp/volumes | Serp Volumes
*SERPApi* | [**serp_volumes_pingback**](docs/SERPApi.md#serp_volumes_pingback) | **GET** /v2/serp/serp/volumes/pingback/{id}/{tag} | Serp Volumes Pingback
*SchedulesApi* | [**create_schedules**](docs/SchedulesApi.md#create_schedules) | **POST** /v2/schedules/create | Create Schedules
*SchedulesApi* | [**delete_schedule**](docs/SchedulesApi.md#delete_schedule) | **DELETE** /v2/schedules/{schedule_id} | Delete Schedule
*SchedulesApi* | [**get_schedule**](docs/SchedulesApi.md#get_schedule) | **GET** /v2/schedules/{schedule_id} | Get Schedule
*SchedulesApi* | [**get_schedule_url_details**](docs/SchedulesApi.md#get_schedule_url_details) | **GET** /v2/schedules/{schedule_id}/urls/{domain_id}/{url_id} | Get Schedule Url Details
*SchedulesApi* | [**get_schedules**](docs/SchedulesApi.md#get_schedules) | **POST** /v2/schedules/ | Get Schedules
*SchedulesApi* | [**run_schedule**](docs/SchedulesApi.md#run_schedule) | **POST** /v2/schedules/run/{schedule_id} | Run Schedule
*SchedulesApi* | [**search_schedule_urls**](docs/SchedulesApi.md#search_schedule_urls) | **POST** /v2/schedules/urls/ | Search Schedule Urls
*SchedulesApi* | [**update_schedule**](docs/SchedulesApi.md#update_schedule) | **PUT** /v2/schedules/{schedule_id} | Update Schedule
*SecretsApi* | [**create_secret**](docs/SecretsApi.md#create_secret) | **POST** /v2/secrets/create | Create Secret
*SecretsApi* | [**delete_secret**](docs/SecretsApi.md#delete_secret) | **DELETE** /v2/secrets/{secret_id} | Delete Secret
*SecretsApi* | [**get_secret**](docs/SecretsApi.md#get_secret) | **GET** /v2/secrets/{secret_id} | Get Secret
*SecretsApi* | [**search_secret**](docs/SecretsApi.md#search_secret) | **POST** /v2/secrets/search | Search Secret
*SecretsApi* | [**update_secret**](docs/SecretsApi.md#update_secret) | **PUT** /v2/secrets/{secret_id} | Update Secret
*SemanticSearchApi* | [**get_similar_docs_by_doc_id**](docs/SemanticSearchApi.md#get_similar_docs_by_doc_id) | **POST** /v2/similarities/document/live | Get Similar Docs By Doc Id
*SemanticSearchApi* | [**get_similar_docs_by_query**](docs/SemanticSearchApi.md#get_similar_docs_by_query) | **POST** /v2/similarities/query/live | Get Similar Docs By Query
*SemanticSearchApi* | [**schedule_similar_docs_by_doc_id**](docs/SemanticSearchApi.md#schedule_similar_docs_by_doc_id) | **POST** /v2/similarities/document | Schedule Similar Docs By Doc Id
*SemanticSearchApi* | [**schedule_similar_docs_by_query**](docs/SemanticSearchApi.md#schedule_similar_docs_by_query) | **POST** /v2/similarities/query | Schedule Similar Docs By Query
*TagsApi* | [**create_tag**](docs/TagsApi.md#create_tag) | **POST** /v2/tags/create | Create Tag
*TagsApi* | [**delete_tag**](docs/TagsApi.md#delete_tag) | **DELETE** /v2/tags/{tag_id} | Delete Tag
*TagsApi* | [**search_tags**](docs/TagsApi.md#search_tags) | **POST** /v2/tags/search | Search Tags
*TagsApi* | [**update_tag**](docs/TagsApi.md#update_tag) | **PUT** /v2/tags/{tag_id} | Update Tag
*WorkspacesApi* | [**add_workspace_user**](docs/WorkspacesApi.md#add_workspace_user) | **POST** /v2/workspaces/{workspace_id}/add-member | Add Workspace User
*WorkspacesApi* | [**create_workspace**](docs/WorkspacesApi.md#create_workspace) | **POST** /v2/workspaces/create | Create Workspace
*WorkspacesApi* | [**delete_workspace**](docs/WorkspacesApi.md#delete_workspace) | **DELETE** /v2/workspaces/{workspace_id} | Delete Workspace
*WorkspacesApi* | [**delete_workspace_user**](docs/WorkspacesApi.md#delete_workspace_user) | **DELETE** /v2/workspaces/{workspace_id}/{user_id} | Delete Workspace User
*WorkspacesApi* | [**get_workspace**](docs/WorkspacesApi.md#get_workspace) | **POST** /v2/workspaces/{workspace_id} | Get Workspace
*WorkspacesApi* | [**search_my_workspaces**](docs/WorkspacesApi.md#search_my_workspaces) | **POST** /v2/workspaces/me/my_workspaces | Search My Workspaces
*WorkspacesApi* | [**search_workspace_users**](docs/WorkspacesApi.md#search_workspace_users) | **POST** /v2/workspaces/{workspace_id}/users | Search Workspace Users
*WorkspacesApi* | [**update_workspace**](docs/WorkspacesApi.md#update_workspace) | **PUT** /v2/workspaces/{workspace_id} | Update Workspace
*WorkspacesApi* | [**update_workspace_user**](docs/WorkspacesApi.md#update_workspace_user) | **PUT** /v2/workspaces/{workspace_id}/{user_id} | Update Workspace User


## Documentation For Models

 - [ApiEndpointCreateRequest](docs/ApiEndpointCreateRequest.md)
 - [ApiEndpointResponse](docs/ApiEndpointResponse.md)
 - [ApiEndpointSearchRequest](docs/ApiEndpointSearchRequest.md)
 - [ApiEndpointUpdateRequest](docs/ApiEndpointUpdateRequest.md)
 - [ApiIntegrationAuthType](docs/ApiIntegrationAuthType.md)
 - [ApiIntegrationAuthenticationMethod](docs/ApiIntegrationAuthenticationMethod.md)
 - [ApiIntegrationCreateRequest](docs/ApiIntegrationCreateRequest.md)
 - [ApiIntegrationOpenApiImportRequest](docs/ApiIntegrationOpenApiImportRequest.md)
 - [ApiIntegrationResponse](docs/ApiIntegrationResponse.md)
 - [ApiIntegrationSearchRequest](docs/ApiIntegrationSearchRequest.md)
 - [ApiIntegrationUpdateRequest](docs/ApiIntegrationUpdateRequest.md)
 - [ApiKeyCreateRequest](docs/ApiKeyCreateRequest.md)
 - [ApiKeyResponse](docs/ApiKeyResponse.md)
 - [ApiKeySearchRequest](docs/ApiKeySearchRequest.md)
 - [ApiKeyUpdateRequest](docs/ApiKeyUpdateRequest.md)
 - [ApiMethod](docs/ApiMethod.md)
 - [AppUrlInput](docs/AppUrlInput.md)
 - [AppUrlOutput](docs/AppUrlOutput.md)
 - [BoolChar](docs/BoolChar.md)
 - [ChatbotCreateRequest](docs/ChatbotCreateRequest.md)
 - [ChatbotResponse](docs/ChatbotResponse.md)
 - [ChatbotSearchRequest](docs/ChatbotSearchRequest.md)
 - [ChatbotStatusInput](docs/ChatbotStatusInput.md)
 - [ChatbotStatusOutput](docs/ChatbotStatusOutput.md)
 - [ChatbotUpdateRequest](docs/ChatbotUpdateRequest.md)
 - [CheckoutCreateRequest](docs/CheckoutCreateRequest.md)
 - [Completed](docs/Completed.md)
 - [CreditBalanceResponse](docs/CreditBalanceResponse.md)
 - [CreditDailyTransactionResponse](docs/CreditDailyTransactionResponse.md)
 - [CreditDailyTransactionSearchRequest](docs/CreditDailyTransactionSearchRequest.md)
 - [CreditTransactionResponse](docs/CreditTransactionResponse.md)
 - [CreditTransactionSearchRequest](docs/CreditTransactionSearchRequest.md)
 - [Data](docs/Data.md)
 - [DocumentCategoryCreateRequest](docs/DocumentCategoryCreateRequest.md)
 - [DocumentCategoryResponse](docs/DocumentCategoryResponse.md)
 - [DocumentCategorySearchRequest](docs/DocumentCategorySearchRequest.md)
 - [DocumentCategoryUpdateRequest](docs/DocumentCategoryUpdateRequest.md)
 - [DocumentContent](docs/DocumentContent.md)
 - [DocumentContentResponse](docs/DocumentContentResponse.md)
 - [DocumentResponse](docs/DocumentResponse.md)
 - [DocumentSearchRequest](docs/DocumentSearchRequest.md)
 - [DocumentSimilarityRequest](docs/DocumentSimilarityRequest.md)
 - [DocumentSimilarityTaskRequest](docs/DocumentSimilarityTaskRequest.md)
 - [DocumentStatus](docs/DocumentStatus.md)
 - [DocumentType](docs/DocumentType.md)
 - [DocumentUpdateRequest](docs/DocumentUpdateRequest.md)
 - [FaqCreateRequest](docs/FaqCreateRequest.md)
 - [FaqResponse](docs/FaqResponse.md)
 - [FaqSearchRequest](docs/FaqSearchRequest.md)
 - [FaqStatus](docs/FaqStatus.md)
 - [FaqType](docs/FaqType.md)
 - [FaqUpdateRequest](docs/FaqUpdateRequest.md)
 - [FeatureResponse](docs/FeatureResponse.md)
 - [FlowCategoryCreateRequest](docs/FlowCategoryCreateRequest.md)
 - [FlowCategoryResponse](docs/FlowCategoryResponse.md)
 - [FlowCategorySearchRequest](docs/FlowCategorySearchRequest.md)
 - [FlowConfig](docs/FlowConfig.md)
 - [FlowCreate](docs/FlowCreate.md)
 - [FlowDetailResponse](docs/FlowDetailResponse.md)
 - [FlowInvokeRequest](docs/FlowInvokeRequest.md)
 - [FlowLoadingIndicator](docs/FlowLoadingIndicator.md)
 - [FlowMessageResponse](docs/FlowMessageResponse.md)
 - [FlowMessageRole](docs/FlowMessageRole.md)
 - [FlowRequestChatRole](docs/FlowRequestChatRole.md)
 - [FlowResponse](docs/FlowResponse.md)
 - [FlowSearchRequest](docs/FlowSearchRequest.md)
 - [FlowSessionAttachmentResponse](docs/FlowSessionAttachmentResponse.md)
 - [FlowSessionCreateFromFlowRequest](docs/FlowSessionCreateFromFlowRequest.md)
 - [FlowSessionCreateRequest](docs/FlowSessionCreateRequest.md)
 - [FlowSessionInvocationMessageResponse](docs/FlowSessionInvocationMessageResponse.md)
 - [FlowSessionInvocationResponse](docs/FlowSessionInvocationResponse.md)
 - [FlowSessionInvokeRequest](docs/FlowSessionInvokeRequest.md)
 - [FlowSessionMessage](docs/FlowSessionMessage.md)
 - [FlowSessionResponse](docs/FlowSessionResponse.md)
 - [FlowSessionStatus](docs/FlowSessionStatus.md)
 - [FlowSessionStreamRequest](docs/FlowSessionStreamRequest.md)
 - [FlowSessionViewResponse](docs/FlowSessionViewResponse.md)
 - [FlowSessionViewSearchRequest](docs/FlowSessionViewSearchRequest.md)
 - [FlowSessionViewUpdateRequest](docs/FlowSessionViewUpdateRequest.md)
 - [FlowType](docs/FlowType.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [Health](docs/Health.md)
 - [ImageConvertRequest](docs/ImageConvertRequest.md)
 - [ImageOptimizeRequest](docs/ImageOptimizeRequest.md)
 - [IntegrationCategory](docs/IntegrationCategory.md)
 - [IntegrationDetailResponse](docs/IntegrationDetailResponse.md)
 - [IntegrationResponse](docs/IntegrationResponse.md)
 - [IntegrationSearchRequest](docs/IntegrationSearchRequest.md)
 - [IntegrationSlug](docs/IntegrationSlug.md)
 - [LoginUserRequest](docs/LoginUserRequest.md)
 - [NewPasswordRequest](docs/NewPasswordRequest.md)
 - [PlanResponse](docs/PlanResponse.md)
 - [PointerType](docs/PointerType.md)
 - [PromptCategoryCreateRequest](docs/PromptCategoryCreateRequest.md)
 - [PromptCategoryResponse](docs/PromptCategoryResponse.md)
 - [PromptCategorySearchRequest](docs/PromptCategorySearchRequest.md)
 - [PromptCategoryUpdateRequest](docs/PromptCategoryUpdateRequest.md)
 - [PromptCreateRequest](docs/PromptCreateRequest.md)
 - [PromptResponse](docs/PromptResponse.md)
 - [PromptSearchRequest](docs/PromptSearchRequest.md)
 - [PromptUpdateRequest](docs/PromptUpdateRequest.md)
 - [QuerySimilarityRequest](docs/QuerySimilarityRequest.md)
 - [QuerySimilarityTaskRequest](docs/QuerySimilarityTaskRequest.md)
 - [RefreshTokenRequest](docs/RefreshTokenRequest.md)
 - [RegisterUserRequest](docs/RegisterUserRequest.md)
 - [Role](docs/Role.md)
 - [ScheduleCreateRequest](docs/ScheduleCreateRequest.md)
 - [ScheduleFrequency](docs/ScheduleFrequency.md)
 - [ScheduleResponse](docs/ScheduleResponse.md)
 - [ScheduleSearchRequest](docs/ScheduleSearchRequest.md)
 - [ScheduleStatus](docs/ScheduleStatus.md)
 - [ScheduleType](docs/ScheduleType.md)
 - [ScheduleUpdateRequest](docs/ScheduleUpdateRequest.md)
 - [ScheduleUrlDetailResponse](docs/ScheduleUrlDetailResponse.md)
 - [ScheduleUrlResponse](docs/ScheduleUrlResponse.md)
 - [ScheduleUrlSearchRequest](docs/ScheduleUrlSearchRequest.md)
 - [ScreenshotRequest](docs/ScreenshotRequest.md)
 - [ScreenshotResponse](docs/ScreenshotResponse.md)
 - [SecretCreateRequest](docs/SecretCreateRequest.md)
 - [SecretResponse](docs/SecretResponse.md)
 - [SecretSearchRequest](docs/SecretSearchRequest.md)
 - [SecretUpdateRequest](docs/SecretUpdateRequest.md)
 - [SerpSearchRequest](docs/SerpSearchRequest.md)
 - [SerpSearchRequests](docs/SerpSearchRequests.md)
 - [SerpVolumeRequest](docs/SerpVolumeRequest.md)
 - [SubscriptionPlan](docs/SubscriptionPlan.md)
 - [TagCreateRequest](docs/TagCreateRequest.md)
 - [TagResponse](docs/TagResponse.md)
 - [TagSearchRequest](docs/TagSearchRequest.md)
 - [TagUpdateRequest](docs/TagUpdateRequest.md)
 - [TaskResponse](docs/TaskResponse.md)
 - [TaskStatus](docs/TaskStatus.md)
 - [ThridPartyLoginRequest](docs/ThridPartyLoginRequest.md)
 - [Token](docs/Token.md)
 - [TransactionType](docs/TransactionType.md)
 - [TranscriptTaskRequest](docs/TranscriptTaskRequest.md)
 - [TriggerType](docs/TriggerType.md)
 - [UrlScreenshotResponse](docs/UrlScreenshotResponse.md)
 - [UserDocumentStatus](docs/UserDocumentStatus.md)
 - [UserPlanResponse](docs/UserPlanResponse.md)
 - [UserResponse](docs/UserResponse.md)
 - [UserTokenResponse](docs/UserTokenResponse.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)
 - [VectorDocumentResponse](docs/VectorDocumentResponse.md)
 - [VectorDocumentType](docs/VectorDocumentType.md)
 - [VectorDocumentsTaskResponse](docs/VectorDocumentsTaskResponse.md)
 - [WorkspaceCreateRequest](docs/WorkspaceCreateRequest.md)
 - [WorkspaceResponse](docs/WorkspaceResponse.md)
 - [WorkspaceRole](docs/WorkspaceRole.md)
 - [WorkspaceSearchRequest](docs/WorkspaceSearchRequest.md)
 - [WorkspaceUpdateRequest](docs/WorkspaceUpdateRequest.md)
 - [WorkspaceUserCreateRequest](docs/WorkspaceUserCreateRequest.md)
 - [WorkspaceUserResponse](docs/WorkspaceUserResponse.md)
 - [WorkspaceUserUpdateRequest](docs/WorkspaceUserUpdateRequest.md)
 - [WorkspaceUsersSearchRequest](docs/WorkspaceUsersSearchRequest.md)
 - [YoutubeContent](docs/YoutubeContent.md)
 - [YoutubeTranscriptRequest](docs/YoutubeTranscriptRequest.md)
 - [YoutubeTranscriptResponse](docs/YoutubeTranscriptResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="sudo_api_key_header"></a>
### sudo_api_key_header

- **Type**: API key
- **API key parameter name**: Sudo-Api-Key
- **Location**: HTTP header

<a id="APIKeyHeader"></a>
### APIKeyHeader

- **Type**: API key
- **API key parameter name**: Api-Key
- **Location**: HTTP header

<a id="HTTPBearer"></a>
### HTTPBearer

- **Type**: Bearer authentication


## Author




