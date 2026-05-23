# FlowSessionEvaluateClientJsMetadata

Metadata for evaluate-client-js hook events.  The widget receives this metadata, runs the script in a sandboxed iframe, and posts the result back via ``POST /flows/sessions/{id}/resume-hook``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hook_id** | **str** | Hook ID for resuming the hook | 
**hook_name** | **str** | Internal pyworkflow hook name | 
**script** | **str** | JS expression to evaluate in the visitor&#39;s browser | 
**timeout_ms** | **int** | Maximum time the widget should wait before returning a timeout error | [optional] [default to 5000]
**request_id** | **str** | Correlates the request with the response posted back from the widget | 

## Example

```python
from flowhunt.models.flow_session_evaluate_client_js_metadata import FlowSessionEvaluateClientJsMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FlowSessionEvaluateClientJsMetadata from a JSON string
flow_session_evaluate_client_js_metadata_instance = FlowSessionEvaluateClientJsMetadata.from_json(json)
# print the JSON string representation of the object
print(FlowSessionEvaluateClientJsMetadata.to_json())

# convert the object into a dict
flow_session_evaluate_client_js_metadata_dict = flow_session_evaluate_client_js_metadata_instance.to_dict()
# create an instance of FlowSessionEvaluateClientJsMetadata from a dict
flow_session_evaluate_client_js_metadata_from_dict = FlowSessionEvaluateClientJsMetadata.from_dict(flow_session_evaluate_client_js_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


