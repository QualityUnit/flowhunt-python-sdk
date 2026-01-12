# CreditTransactionSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Transaction ID | [optional] 
**created_at_from** | **datetime** | Transactions created from date | [optional] 
**created_at_to** | **datetime** | Transactions created to date | [optional] 
**transaction_type** | [**TransactionType**](TransactionType.md) | Transaction type | [optional] 
**context_id** | **str** | Context ID | [optional] 
**context_desc** | **str** | Context description | [optional] 
**limit** | **int** | Limit returned number of rows | [optional] [default to 100]
**pagination** | [**Pagination**](Pagination.md) | Pagination parameters | [optional] 

## Example

```python
from flowhunt.models.credit_transaction_search_request import CreditTransactionSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreditTransactionSearchRequest from a JSON string
credit_transaction_search_request_instance = CreditTransactionSearchRequest.from_json(json)
# print the JSON string representation of the object
print(CreditTransactionSearchRequest.to_json())

# convert the object into a dict
credit_transaction_search_request_dict = credit_transaction_search_request_instance.to_dict()
# create an instance of CreditTransactionSearchRequest from a dict
credit_transaction_search_request_from_dict = CreditTransactionSearchRequest.from_dict(credit_transaction_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


