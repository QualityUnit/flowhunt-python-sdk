# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.models.document_similarity_request import DocumentSimilarityRequest

class TestDocumentSimilarityRequest(unittest.TestCase):
    """DocumentSimilarityRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocumentSimilarityRequest:
        """Test DocumentSimilarityRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocumentSimilarityRequest`
        """
        model = DocumentSimilarityRequest()
        if include_optional:
            return DocumentSimilarityRequest(
                document_type = 'U',
                pointer_type = 'C',
                schema_type = '',
                limit = 56,
                score_trheshold = 1.337,
                with_vectors = True,
                pointer_position_from = 56,
                pointer_position_to = 56,
                vector_id_from = 56,
                vector_id_to = 56,
                filter_url = '',
                filter_domains = [
                    ''
                    ],
                document_id = '',
                faq_id = '',
                url_id = '',
                url = ''
            )
        else:
            return DocumentSimilarityRequest(
        )
        """

    def testDocumentSimilarityRequest(self):
        """Test DocumentSimilarityRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
