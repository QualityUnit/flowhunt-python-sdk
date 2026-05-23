# GenerateAgentConfigStartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Session ID for polling events | 
**created_at** | **str** | Timestamp (ms since epoch) for polling | 

## Example

```python
from flowhunt.models.generate_agent_config_start_response import GenerateAgentConfigStartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateAgentConfigStartResponse from a JSON string
generate_agent_config_start_response_instance = GenerateAgentConfigStartResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateAgentConfigStartResponse.to_json())

# convert the object into a dict
generate_agent_config_start_response_dict = generate_agent_config_start_response_instance.to_dict()
# create an instance of GenerateAgentConfigStartResponse from a dict
generate_agent_config_start_response_from_dict = GenerateAgentConfigStartResponse.from_dict(generate_agent_config_start_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


