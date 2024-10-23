# YoutubeTranscriptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_back_url** | **str** |  | [optional] 
**video_id** | **str** |  | [optional] 
**video_url** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.youtube_transcript_request import YoutubeTranscriptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of YoutubeTranscriptRequest from a JSON string
youtube_transcript_request_instance = YoutubeTranscriptRequest.from_json(json)
# print the JSON string representation of the object
print(YoutubeTranscriptRequest.to_json())

# convert the object into a dict
youtube_transcript_request_dict = youtube_transcript_request_instance.to_dict()
# create an instance of YoutubeTranscriptRequest from a dict
youtube_transcript_request_from_dict = YoutubeTranscriptRequest.from_dict(youtube_transcript_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


