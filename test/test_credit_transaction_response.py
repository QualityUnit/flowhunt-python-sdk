# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt-python-sdk.models.credit_transaction_response import CreditTransactionResponse

class TestCreditTransactionResponse(unittest.TestCase):
    """CreditTransactionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreditTransactionResponse:
        """Test CreditTransactionResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreditTransactionResponse`
        """
        model = CreditTransactionResponse()
        if include_optional:
            return CreditTransactionResponse(
                transaction_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                workspace_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                user_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                created_at = '2021-01-01T00:00:00',
                transaction_type = A,
                context_id = '123456',
                context_desc = 'e.g. Chatbot name',
                amount = 100
            )
        else:
            return CreditTransactionResponse(
                transaction_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                workspace_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                user_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                created_at = '2021-01-01T00:00:00',
                transaction_type = A,
                context_id = '123456',
                amount = 100,
        )
        """

    def testCreditTransactionResponse(self):
        """Test CreditTransactionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
