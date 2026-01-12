# SerpSubclusterKeywordsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**missing_keywords** | **List[str]** | List of keywords not assigned yet | 
**keywords** | **List[str]** | List of keywords already assigned | 
**count** | **int** | Count of keywords in subcluster | 

## Example

```python
from flowhunt.models.serp_subcluster_keywords_response import SerpSubclusterKeywordsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SerpSubclusterKeywordsResponse from a JSON string
serp_subcluster_keywords_response_instance = SerpSubclusterKeywordsResponse.from_json(json)
# print the JSON string representation of the object
print(SerpSubclusterKeywordsResponse.to_json())

# convert the object into a dict
serp_subcluster_keywords_response_dict = serp_subcluster_keywords_response_instance.to_dict()
# create an instance of SerpSubclusterKeywordsResponse from a dict
serp_subcluster_keywords_response_from_dict = SerpSubclusterKeywordsResponse.from_dict(serp_subcluster_keywords_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


