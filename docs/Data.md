# Data

Document linked to vector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | **str** |  | 
**domain_id** | **str** |  | 
**url_id** | **str** |  | 
**url** | **str** |  | 
**last_text_timestamp** | **datetime** |  | 
**page_screenshot** | [**UrlScreenshotResponse**](UrlScreenshotResponse.md) |  | 
**url_title** | **str** |  | 
**url_meta_description** | **str** |  | 
**url_og_image** | **str** |  | 
**is_original_url** | **bool** |  | 
**dest_url_id** | **str** |  | 
**created_at** | **datetime** |  | 
**url_text** | **List[Dict[str, str]]** |  | 
**faq_id** | **str** | FAQ ID | 
**workspace_id** | **str** | Workspace ID | 
**cat_id** | **str** | Category ID | 
**question** | **str** | Question | 
**answer** | **str** |  | [optional] 
**parent_faq_id** | **str** |  | [optional] 
**status** | **str** | Document status | 
**updated_at** | **datetime** | Document updated at | 
**indexed_at** | **datetime** |  | [optional] 
**doc_id** | **str** | Document ID | 
**doc_name** | **str** | Document name | 
**doc_type** | **str** | Document type | 
**user_status** | **str** | User status | 

## Example

```python
from flowhunt.models.data import Data

# TODO update the JSON string below
json = "{}"
# create an instance of Data from a JSON string
data_instance = Data.from_json(json)
# print the JSON string representation of the object
print(Data.to_json())

# convert the object into a dict
data_dict = data_instance.to_dict()
# create an instance of Data from a dict
data_from_dict = Data.from_dict(data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


