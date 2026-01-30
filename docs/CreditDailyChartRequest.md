# CreditDailyChartRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at_from** | **datetime** | Transactions created from date | [optional] 
**created_at_to** | **datetime** | Transactions created to date | [optional] 
**transaction_type** | [**TransactionType**](TransactionType.md) | Transaction type filter | [optional] 

## Example

```python
from flowhunt.models.credit_daily_chart_request import CreditDailyChartRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreditDailyChartRequest from a JSON string
credit_daily_chart_request_instance = CreditDailyChartRequest.from_json(json)
# print the JSON string representation of the object
print(CreditDailyChartRequest.to_json())

# convert the object into a dict
credit_daily_chart_request_dict = credit_daily_chart_request_instance.to_dict()
# create an instance of CreditDailyChartRequest from a dict
credit_daily_chart_request_from_dict = CreditDailyChartRequest.from_dict(credit_daily_chart_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


