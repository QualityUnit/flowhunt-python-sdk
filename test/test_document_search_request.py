# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.document_search_request import DocumentSearchRequest

class TestDocumentSearchRequest(unittest.TestCase):
    """DocumentSearchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocumentSearchRequest:
        """Test DocumentSearchRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocumentSearchRequest`
        """
        model = DocumentSearchRequest()
        if include_optional:
            return DocumentSearchRequest(
                doc_id = '',
                cat_id = '',
                doc_name = '',
                doc_type = 'PDF',
                status = 'N',
                user_status = 'E',
                updated_at_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at_to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                limit = 56
            )
        else:
            return DocumentSearchRequest(
        )
        """

    def testDocumentSearchRequest(self):
        """Test DocumentSearchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
