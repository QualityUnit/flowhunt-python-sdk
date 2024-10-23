# CreditTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Transaction ID | 
**workspace_id** | **str** | Workspace ID | 
**user_id** | **str** | User ID or user to whom is transaction assigned | 
**created_at** | **datetime** | Transaction creation date | 
**transaction_type** | [**TransactionType**](TransactionType.md) | Transaction type | 
**context_id** | **str** | Context ID - identification of transaction context - eg chatbot id | 
**context_desc** | **str** | Context description - description of transaction context | [optional] 
**amount** | **int** | Amount of credits | 

## Example

```python
from flowhunt.models.credit_transaction_response import CreditTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditTransactionResponse from a JSON string
credit_transaction_response_instance = CreditTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(CreditTransactionResponse.to_json())

# convert the object into a dict
credit_transaction_response_dict = credit_transaction_response_instance.to_dict()
# create an instance of CreditTransactionResponse from a dict
credit_transaction_response_from_dict = CreditTransactionResponse.from_dict(credit_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


