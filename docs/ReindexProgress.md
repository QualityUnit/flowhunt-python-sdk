# ReindexProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | [optional] 
**embedding_model** | **str** |  | 
**status** | [**ReindexStatus**](ReindexStatus.md) |  | 
**data_source** | [**ReindexDataSource**](ReindexDataSource.md) |  | 
**total_items** | **int** |  | [optional] [default to 0]
**processed_items** | **int** |  | [optional] [default to 0]
**failed_items** | **int** |  | [optional] [default to 0]
**started_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**completed_at** | **datetime** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from flowhunt.models.reindex_progress import ReindexProgress

# TODO update the JSON string below
json = "{}"
# create an instance of ReindexProgress from a JSON string
reindex_progress_instance = ReindexProgress.from_json(json)
# print the JSON string representation of the object
print(ReindexProgress.to_json())

# convert the object into a dict
reindex_progress_dict = reindex_progress_instance.to_dict()
# create an instance of ReindexProgress from a dict
reindex_progress_from_dict = ReindexProgress.from_dict(reindex_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


