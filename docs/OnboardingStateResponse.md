# OnboardingStateResponse

Current onboarding state for the authenticated user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **bool** | Whether the user finished the welcome screen. | 
**primary_goal** | [**OnboardingPrimaryGoal**](OnboardingPrimaryGoal.md) | The product the user selected, if any. | [optional] 
**completed_at** | **str** | ISO-8601 timestamp of completion, if completed. | [optional] 

## Example

```python
from flowhunt.models.onboarding_state_response import OnboardingStateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardingStateResponse from a JSON string
onboarding_state_response_instance = OnboardingStateResponse.from_json(json)
# print the JSON string representation of the object
print(OnboardingStateResponse.to_json())

# convert the object into a dict
onboarding_state_response_dict = onboarding_state_response_instance.to_dict()
# create an instance of OnboardingStateResponse from a dict
onboarding_state_response_from_dict = OnboardingStateResponse.from_dict(onboarding_state_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


