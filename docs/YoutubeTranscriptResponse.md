# YoutubeTranscriptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Task ID | 
**status** | [**TaskStatus**](TaskStatus.md) | Task status | 
**result** | [**YoutubeContent**](YoutubeContent.md) |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.youtube_transcript_response import YoutubeTranscriptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of YoutubeTranscriptResponse from a JSON string
youtube_transcript_response_instance = YoutubeTranscriptResponse.from_json(json)
# print the JSON string representation of the object
print(YoutubeTranscriptResponse.to_json())

# convert the object into a dict
youtube_transcript_response_dict = youtube_transcript_response_instance.to_dict()
# create an instance of YoutubeTranscriptResponse from a dict
youtube_transcript_response_from_dict = YoutubeTranscriptResponse.from_dict(youtube_transcript_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


