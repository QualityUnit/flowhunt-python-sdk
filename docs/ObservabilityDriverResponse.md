# ObservabilityDriverResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver_type** | **str** |  | 
**additional_data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from flowhunt.models.observability_driver_response import ObservabilityDriverResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ObservabilityDriverResponse from a JSON string
observability_driver_response_instance = ObservabilityDriverResponse.from_json(json)
# print the JSON string representation of the object
print(ObservabilityDriverResponse.to_json())

# convert the object into a dict
observability_driver_response_dict = observability_driver_response_instance.to_dict()
# create an instance of ObservabilityDriverResponse from a dict
observability_driver_response_from_dict = ObservabilityDriverResponse.from_dict(observability_driver_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


