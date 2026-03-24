# ClickUpSpaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**space_id** | **str** |  | 
**space_name** | **str** |  | 

## Example

```python
from flowhunt.models.click_up_space_response import ClickUpSpaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClickUpSpaceResponse from a JSON string
click_up_space_response_instance = ClickUpSpaceResponse.from_json(json)
# print the JSON string representation of the object
print(ClickUpSpaceResponse.to_json())

# convert the object into a dict
click_up_space_response_dict = click_up_space_response_instance.to_dict()
# create an instance of ClickUpSpaceResponse from a dict
click_up_space_response_from_dict = ClickUpSpaceResponse.from_dict(click_up_space_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


