# IntegrationDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | The type of the integration. | 
**integration_id** | **str** | The ID of the integration. | 
**created_at** | **datetime** | The creation date of the integration. | 

## Example

```python
from flowhunt-python-sdk.models.integration_detail_response import IntegrationDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationDetailResponse from a JSON string
integration_detail_response_instance = IntegrationDetailResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationDetailResponse.to_json())

# convert the object into a dict
integration_detail_response_dict = integration_detail_response_instance.to_dict()
# create an instance of IntegrationDetailResponse from a dict
integration_detail_response_from_dict = IntegrationDetailResponse.from_dict(integration_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


