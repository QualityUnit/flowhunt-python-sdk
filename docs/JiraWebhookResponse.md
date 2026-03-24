# JiraWebhookResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**url** | **str** |  | 
**events** | **List[str]** |  | 
**expiration_date** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.jira_webhook_response import JiraWebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JiraWebhookResponse from a JSON string
jira_webhook_response_instance = JiraWebhookResponse.from_json(json)
# print the JSON string representation of the object
print(JiraWebhookResponse.to_json())

# convert the object into a dict
jira_webhook_response_dict = jira_webhook_response_instance.to_dict()
# create an instance of JiraWebhookResponse from a dict
jira_webhook_response_from_dict = JiraWebhookResponse.from_dict(jira_webhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


