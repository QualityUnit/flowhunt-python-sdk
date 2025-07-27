# LangfuseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**langfuse_public_key** | **str** |  | [optional] 
**langfuse_secret_key** | **str** |  | [optional] 
**langfuse_host** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.langfuse_request import LangfuseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LangfuseRequest from a JSON string
langfuse_request_instance = LangfuseRequest.from_json(json)
# print the JSON string representation of the object
print(LangfuseRequest.to_json())

# convert the object into a dict
langfuse_request_dict = langfuse_request_instance.to_dict()
# create an instance of LangfuseRequest from a dict
langfuse_request_from_dict = LangfuseRequest.from_dict(langfuse_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


