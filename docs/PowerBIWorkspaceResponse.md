# PowerBIWorkspaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** | Power BI workspace ID | 
**workspace_name** | **str** | Power BI workspace name | 

## Example

```python
from flowhunt.models.power_bi_workspace_response import PowerBIWorkspaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PowerBIWorkspaceResponse from a JSON string
power_bi_workspace_response_instance = PowerBIWorkspaceResponse.from_json(json)
# print the JSON string representation of the object
print(PowerBIWorkspaceResponse.to_json())

# convert the object into a dict
power_bi_workspace_response_dict = power_bi_workspace_response_instance.to_dict()
# create an instance of PowerBIWorkspaceResponse from a dict
power_bi_workspace_response_from_dict = PowerBIWorkspaceResponse.from_dict(power_bi_workspace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


