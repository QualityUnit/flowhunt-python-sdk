# SystemMessageMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | Message ID | 
**message** | **str** | Message | 

## Example

```python
from flowhunt.models.system_message_metadata import SystemMessageMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SystemMessageMetadata from a JSON string
system_message_metadata_instance = SystemMessageMetadata.from_json(json)
# print the JSON string representation of the object
print(SystemMessageMetadata.to_json())

# convert the object into a dict
system_message_metadata_dict = system_message_metadata_instance.to_dict()
# create an instance of SystemMessageMetadata from a dict
system_message_metadata_from_dict = SystemMessageMetadata.from_dict(system_message_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


