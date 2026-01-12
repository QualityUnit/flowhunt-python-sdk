# HumanAgentSender


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_name** | **str** |  | [optional] 
**sender_avatar** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.human_agent_sender import HumanAgentSender

# TODO update the JSON string below
json = "{}"
# create an instance of HumanAgentSender from a JSON string
human_agent_sender_instance = HumanAgentSender.from_json(json)
# print the JSON string representation of the object
print(HumanAgentSender.to_json())

# convert the object into a dict
human_agent_sender_dict = human_agent_sender_instance.to_dict()
# create an instance of HumanAgentSender from a dict
human_agent_sender_from_dict = HumanAgentSender.from_dict(human_agent_sender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


