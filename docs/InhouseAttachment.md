# InhouseAttachment

Attachment whose bytes live in our S3 delivery bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | File name | 
**file_type** | **str** | File type | 
**file_id** | **str** | Session-local identifier | 
**type** | [**DocumentType**](DocumentType.md) | Document type | 
**source** | **str** |  | [optional] [default to 'inhouse']

## Example

```python
from flowhunt.models.inhouse_attachment import InhouseAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of InhouseAttachment from a JSON string
inhouse_attachment_instance = InhouseAttachment.from_json(json)
# print the JSON string representation of the object
print(InhouseAttachment.to_json())

# convert the object into a dict
inhouse_attachment_dict = inhouse_attachment_instance.to_dict()
# create an instance of InhouseAttachment from a dict
inhouse_attachment_from_dict = InhouseAttachment.from_dict(inhouse_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


