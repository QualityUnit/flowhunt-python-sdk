# LogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_id** | **str** | Unique identifier for the log entry | 
**log_type** | [**LogEntryType**](LogEntryType.md) | Type of log (e.g., &#39;system&#39;, &#39;application&#39;, &#39;user&#39;) | 
**category_id** | **str** | Optional category identifier for the log | [optional] 
**log_level** | [**LogEntryLevel**](LogEntryLevel.md) | Log level (e.g., &#39;info&#39;, &#39;warning&#39;, &#39;error&#39;, &#39;debug&#39;) | 
**message** | **str** | Log message content | 
**created_at** | **datetime** | Timestamp when the log was created | 
**metadata** | **Dict[str, object]** | Additional metadata associated with the log entry | [optional] 

## Example

```python
from flowhunt.models.log_response import LogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LogResponse from a JSON string
log_response_instance = LogResponse.from_json(json)
# print the JSON string representation of the object
print(LogResponse.to_json())

# convert the object into a dict
log_response_dict = log_response_instance.to_dict()
# create an instance of LogResponse from a dict
log_response_from_dict = LogResponse.from_dict(log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


