# IntegrationFlowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_to** | **str** | The URL to redirect to. | 

## Example

```python
from flowhunt.models.integration_flow_response import IntegrationFlowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationFlowResponse from a JSON string
integration_flow_response_instance = IntegrationFlowResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationFlowResponse.to_json())

# convert the object into a dict
integration_flow_response_dict = integration_flow_response_instance.to_dict()
# create an instance of IntegrationFlowResponse from a dict
integration_flow_response_from_dict = IntegrationFlowResponse.from_dict(integration_flow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


