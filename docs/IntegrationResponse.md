# IntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | The slug of the integration. | 
**name** | **str** | The name of the integration. | 
**description** | **str** | The description of the integration. | 
**integrated_instance_cnt** | **int** | The number of integrated instances. | 
**categories** | [**List[IntegrationCategory]**](IntegrationCategory.md) | The categories of the integration. | 
**alpha** | **bool** | Whether the integration is in alpha or not. | [optional] [default to False]
**beta** | **bool** | Whether the integration is in beta or not. | [optional] [default to False]
**public_flow_id** | **str** |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.integration_response import IntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationResponse from a JSON string
integration_response_instance = IntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationResponse.to_json())

# convert the object into a dict
integration_response_dict = integration_response_instance.to_dict()
# create an instance of IntegrationResponse from a dict
integration_response_from_dict = IntegrationResponse.from_dict(integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


