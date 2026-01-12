# CreditDailyChartDataRow

A single row in the chart data representing one day's transactions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date in YYYY-MM-DD format | 
**transaction_types** | **Dict[str, int]** | Dictionary of transaction type codes to their total amounts | 

## Example

```python
from flowhunt.models.credit_daily_chart_data_row import CreditDailyChartDataRow

# TODO update the JSON string below
json = "{}"
# create an instance of CreditDailyChartDataRow from a JSON string
credit_daily_chart_data_row_instance = CreditDailyChartDataRow.from_json(json)
# print the JSON string representation of the object
print(CreditDailyChartDataRow.to_json())

# convert the object into a dict
credit_daily_chart_data_row_dict = credit_daily_chart_data_row_instance.to_dict()
# create an instance of CreditDailyChartDataRow from a dict
credit_daily_chart_data_row_from_dict = CreditDailyChartDataRow.from_dict(credit_daily_chart_data_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


