# CreditDailyChartResponse

Response containing chart data for daily credit transactions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_day** | [**List[CreditDailyChartDataRow]**](CreditDailyChartDataRow.md) | List of daily transaction data rows | 
**transaction_types** | [**List[TransactionType]**](TransactionType.md) | List of all transaction type codes present in the data | 

## Example

```python
from flowhunt.models.credit_daily_chart_response import CreditDailyChartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditDailyChartResponse from a JSON string
credit_daily_chart_response_instance = CreditDailyChartResponse.from_json(json)
# print the JSON string representation of the object
print(CreditDailyChartResponse.to_json())

# convert the object into a dict
credit_daily_chart_response_dict = credit_daily_chart_response_instance.to_dict()
# create an instance of CreditDailyChartResponse from a dict
credit_daily_chart_response_from_dict = CreditDailyChartResponse.from_dict(credit_daily_chart_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


