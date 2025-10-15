# FailedFaqItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** | Question that failed to import | 
**answer** | **str** | Answer (truncated to 200 chars) | 
**reason** | **str** | Reason for failure | 

## Example

```python
from flowhunt.models.failed_faq_item import FailedFaqItem

# TODO update the JSON string below
json = "{}"
# create an instance of FailedFaqItem from a JSON string
failed_faq_item_instance = FailedFaqItem.from_json(json)
# print the JSON string representation of the object
print(FailedFaqItem.to_json())

# convert the object into a dict
failed_faq_item_dict = failed_faq_item_instance.to_dict()
# create an instance of FailedFaqItem from a dict
failed_faq_item_from_dict = FailedFaqItem.from_dict(failed_faq_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


