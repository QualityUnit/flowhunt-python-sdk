# YoutubeContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**img_url** | **str** |  | [optional] 
**status_code** | **int** |  | [optional] 
**created_at** | **float** |  | [optional] 
**published_at** | **float** |  | [optional] 
**title** | **str** |  | [optional] 
**lang** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**encoding** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**alt_content** | **List[str]** |  | [optional] 
**content_hash** | **str** |  | [optional] 
**author** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**channel_url** | **str** |  | [optional] 
**channel_title** | **str** |  | [optional] 
**duration** | **int** |  | [optional] 
**keywords** | **List[str]** |  | [optional] 
**doc_type** | [**DocumentType**](DocumentType.md) |  | [optional] 
**credits** | **int** |  | [optional] 

## Example

```python
from flowhunt-python-sdk.models.youtube_content import YoutubeContent

# TODO update the JSON string below
json = "{}"
# create an instance of YoutubeContent from a JSON string
youtube_content_instance = YoutubeContent.from_json(json)
# print the JSON string representation of the object
print(YoutubeContent.to_json())

# convert the object into a dict
youtube_content_dict = youtube_content_instance.to_dict()
# create an instance of YoutubeContent from a dict
youtube_content_from_dict = YoutubeContent.from_dict(youtube_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


