# SerpKeyword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword_id** | **str** | Keyword ID, if not provided it will be generated | [optional] 
**keyword** | **str** | Keyword to search | 
**language** | **str** | Language to search | [optional] [default to 'en']
**country** | **str** | Country to search from | [optional] [default to 'us']
**search_engine** | [**SerpSearchEngineType**](SerpSearchEngineType.md) | Search engine to analyze keyword clusters | [optional] 

## Example

```python
from flowhunt.models.serp_keyword import SerpKeyword

# TODO update the JSON string below
json = "{}"
# create an instance of SerpKeyword from a JSON string
serp_keyword_instance = SerpKeyword.from_json(json)
# print the JSON string representation of the object
print(SerpKeyword.to_json())

# convert the object into a dict
serp_keyword_dict = serp_keyword_instance.to_dict()
# create an instance of SerpKeyword from a dict
serp_keyword_from_dict = SerpKeyword.from_dict(serp_keyword_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


