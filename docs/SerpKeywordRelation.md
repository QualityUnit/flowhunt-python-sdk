# SerpKeywordRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword_id_1** | **str** | The keyword id | 
**keyword_1** | **str** | The keyword | 
**keyword_id_2** | **str** | The related keyword id | 
**keyword_2** | **str** | The related keyword | 
**count** | **int** | The count of cluster strength | 

## Example

```python
from flowhunt.models.serp_keyword_relation import SerpKeywordRelation

# TODO update the JSON string below
json = "{}"
# create an instance of SerpKeywordRelation from a JSON string
serp_keyword_relation_instance = SerpKeywordRelation.from_json(json)
# print the JSON string representation of the object
print(SerpKeywordRelation.to_json())

# convert the object into a dict
serp_keyword_relation_dict = serp_keyword_relation_instance.to_dict()
# create an instance of SerpKeywordRelation from a dict
serp_keyword_relation_from_dict = SerpKeywordRelation.from_dict(serp_keyword_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


