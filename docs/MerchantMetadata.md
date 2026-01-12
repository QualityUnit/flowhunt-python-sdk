# MerchantMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**item_group_id** | **str** |  | [optional] 
**gtin** | **str** |  | [optional] 
**mpn** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**brand** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**image_link** | **str** |  | [optional] 
**additional_image_link** | **str** |  | [optional] 
**availability** | **str** |  | [optional] 
**condition** | **str** |  | [optional] 
**google_product_category** | **str** |  | [optional] 
**product_type** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**size** | **str** |  | [optional] 
**material** | **str** |  | [optional] 
**age_group** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**shipping** | **object** |  | [optional] 

## Example

```python
from flowhunt.models.merchant_metadata import MerchantMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantMetadata from a JSON string
merchant_metadata_instance = MerchantMetadata.from_json(json)
# print the JSON string representation of the object
print(MerchantMetadata.to_json())

# convert the object into a dict
merchant_metadata_dict = merchant_metadata_instance.to_dict()
# create an instance of MerchantMetadata from a dict
merchant_metadata_from_dict = MerchantMetadata.from_dict(merchant_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


