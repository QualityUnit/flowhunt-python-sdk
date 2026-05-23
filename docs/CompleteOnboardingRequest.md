# CompleteOnboardingRequest

Body for PATCH /v2/users/me/onboarding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_goal** | [**OnboardingPrimaryGoal**](OnboardingPrimaryGoal.md) | Product the user picked on the welcome screen. | 

## Example

```python
from flowhunt.models.complete_onboarding_request import CompleteOnboardingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompleteOnboardingRequest from a JSON string
complete_onboarding_request_instance = CompleteOnboardingRequest.from_json(json)
# print the JSON string representation of the object
print(CompleteOnboardingRequest.to_json())

# convert the object into a dict
complete_onboarding_request_dict = complete_onboarding_request_instance.to_dict()
# create an instance of CompleteOnboardingRequest from a dict
complete_onboarding_request_from_dict = CompleteOnboardingRequest.from_dict(complete_onboarding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


