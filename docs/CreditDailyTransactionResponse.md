# CreditDailyTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Transactions from date | 
**workspace_id** | **str** | Workspace ID | 
**transaction_type** | [**TransactionType**](TransactionType.md) | Transaction type | 
**amount** | **int** | Amount of credits | 
**cnt** | **int** | Number of transactions | 

## Example

```python
from flowhunt-python-sdk.models.credit_daily_transaction_response import CreditDailyTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditDailyTransactionResponse from a JSON string
credit_daily_transaction_response_instance = CreditDailyTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(CreditDailyTransactionResponse.to_json())

# convert the object into a dict
credit_daily_transaction_response_dict = credit_daily_transaction_response_instance.to_dict()
# create an instance of CreditDailyTransactionResponse from a dict
credit_daily_transaction_response_from_dict = CreditDailyTransactionResponse.from_dict(credit_daily_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


