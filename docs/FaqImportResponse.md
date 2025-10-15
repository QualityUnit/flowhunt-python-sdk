# FaqImportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | [**List[FaqResponse]**](FaqResponse.md) | List of successfully imported FAQs | 
**failed** | [**List[FailedFaqItem]**](FailedFaqItem.md) | List of FAQs that failed to import | 
**total_attempted** | **int** | Total number of FAQs attempted | 
**total_successful** | **int** | Number of successfully imported FAQs | 
**total_failed** | **int** | Number of failed FAQs | 

## Example

```python
from flowhunt.models.faq_import_response import FaqImportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FaqImportResponse from a JSON string
faq_import_response_instance = FaqImportResponse.from_json(json)
# print the JSON string representation of the object
print(FaqImportResponse.to_json())

# convert the object into a dict
faq_import_response_dict = faq_import_response_instance.to_dict()
# create an instance of FaqImportResponse from a dict
faq_import_response_from_dict = FaqImportResponse.from_dict(faq_import_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


