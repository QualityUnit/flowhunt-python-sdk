# FlowSessionIntegrationMissingMetadata

Metadata for integration missing events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | Integration slug that is missing | 
**integration_url** | **str** | URL for the user to set up the integration | 

## Example

```python
from flowhunt.models.flow_session_integration_missing_metadata import FlowSessionIntegrationMissingMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionIntegrationMissingMetadata from a JSON string
flow_session_integration_missing_metadata_instance = FlowSessionIntegrationMissingMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionIntegrationMissingMetadata.to_json())

# convert the object into a dict
flow_session_integration_missing_metadata_dict = flow_session_integration_missing_metadata_instance.to_dict()
# create an instance of FlowSessionIntegrationMissingMetadata from a dict
flow_session_integration_missing_metadata_from_dict = FlowSessionIntegrationMissingMetadata.from_dict(flow_session_integration_missing_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


