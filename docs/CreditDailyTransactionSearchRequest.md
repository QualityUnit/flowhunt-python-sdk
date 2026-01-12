# CreditDailyTransactionSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at_from** | **datetime** | Transactions created from date | [optional] 
**created_at_to** | **datetime** | Transactions created to date | [optional] 
**transaction_type** | [**TransactionType**](TransactionType.md) | Transaction type | [optional] 
**limit** | **int** | Limit returned number of rows | [optional] [default to 100]
**pagination** | [**Pagination**](Pagination.md) | Pagination parameters | [optional] 

## Example

```python
from flowhunt.models.credit_daily_transaction_search_request import CreditDailyTransactionSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreditDailyTransactionSearchRequest from a JSON string
credit_daily_transaction_search_request_instance = CreditDailyTransactionSearchRequest.from_json(json)
# print the JSON string representation of the object
print(CreditDailyTransactionSearchRequest.to_json())

# convert the object into a dict
credit_daily_transaction_search_request_dict = credit_daily_transaction_search_request_instance.to_dict()
# create an instance of CreditDailyTransactionSearchRequest from a dict
credit_daily_transaction_search_request_from_dict = CreditDailyTransactionSearchRequest.from_dict(credit_daily_transaction_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


