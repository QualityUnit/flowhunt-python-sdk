# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.document_response import DocumentResponse

class TestDocumentResponse(unittest.TestCase):
    """DocumentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocumentResponse:
        """Test DocumentResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocumentResponse`
        """
        model = DocumentResponse()
        if include_optional:
            return DocumentResponse(
                doc_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                cat_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                workspace_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                doc_name = 'Document name',
                url = '',
                doc_type = 'PDF',
                user_status = 'N',
                status = 'N',
                updated_at = '2021-01-01T00:00:00'
            )
        else:
            return DocumentResponse(
                doc_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                cat_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                workspace_id = 'd719f5f5-5433-4cb4-9993-8053bda1a384',
                doc_name = 'Document name',
                doc_type = 'PDF',
                user_status = 'N',
                status = 'N',
                updated_at = '2021-01-01T00:00:00',
        )
        """

    def testDocumentResponse(self):
        """Test DocumentResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
