# YoutubeContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL of the document | [optional] 
**img_url** | **str** | Image URL or Thumbnail URL | [optional] 
**status_code** | **int** | HTTP Status Code | [optional] 
**created_at** | **float** | Creation date of the document (timestamp) | [optional] [default to 1.768217590159811E9]
**published_at** | **float** | Publication date of the document (timestamp) | [optional] 
**title** | **str** | Title of the document | [optional] 
**doc_name** | **str** | Original file name of the document | [optional] 
**lang** | **str** | Language of the document | [optional] 
**content_type** | **str** | Content type of the document | [optional] 
**encoding** | **str** | Encoding of the document | [optional] 
**apparent_encoding** | **str** | Apparent encoding of the document | [optional] 
**description** | **str** | Description of the document | [optional] 
**content** | **str** | Youtube video transcript content | [optional] 
**metadata** | **Dict[str, object]** | Metadata of the document. Supported formats: json-ld, microdata, opengraph | [optional] 
**alt_content** | **List[str]** | Alternative content for embedding representing the same document (e.g. in FAQs it is alternative questions as the primary question) | [optional] 
**content_hash** | **str** | Hash of the content | [optional] 
**author** | **str** | Document Author | [optional] 
**channel_id** | **str** | Youtube Channel ID | [optional] 
**channel_url** | **str** | Youtube Channel URL | [optional] 
**channel_title** | **str** | Youtube Channel Title | [optional] 
**duration** | **int** | Duration of the video in seconds | [optional] 
**keywords** | **List[str]** | Keywords of the document | [optional] 
**doc_type** | [**DocumentType**](DocumentType.md) | Document Type | [optional] 
**credits** | **int** | Credits used for processing the document | [optional] 
**url_content** | **Dict[str, object]** | URL content if applicable | [optional] 
**merchant_metadata** | [**MerchantMetadata**](MerchantMetadata.md) | Metadata associated with the document | [optional] 

## Example

```python
from flowhunt.models.youtube_content import YoutubeContent

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


