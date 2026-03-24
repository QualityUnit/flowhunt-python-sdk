# TodoItem

Single todo item in agent's todo list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Todo item content/description | 
**status** | **str** | Todo status: pending, in_progress, or completed | 

## Example

```python
from flowhunt.models.todo_item import TodoItem

# TODO update the JSON string below
json = "{}"
# create an instance of TodoItem from a JSON string
todo_item_instance = TodoItem.from_json(json)
# print the JSON string representation of the object
print(TodoItem.to_json())

# convert the object into a dict
todo_item_dict = todo_item_instance.to_dict()
# create an instance of TodoItem from a dict
todo_item_from_dict = TodoItem.from_dict(todo_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


