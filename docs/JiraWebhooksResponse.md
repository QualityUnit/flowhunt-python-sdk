# JiraWebhooksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhooks** | [**List[JiraWebhookResponse]**](JiraWebhookResponse.md) |  | 

## Example

```python
from flowhunt.models.jira_webhooks_response import JiraWebhooksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JiraWebhooksResponse from a JSON string
jira_webhooks_response_instance = JiraWebhooksResponse.from_json(json)
# print the JSON string representation of the object
print(JiraWebhooksResponse.to_json())

# convert the object into a dict
jira_webhooks_response_dict = jira_webhooks_response_instance.to_dict()
# create an instance of JiraWebhooksResponse from a dict
jira_webhooks_response_from_dict = JiraWebhooksResponse.from_dict(jira_webhooks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


