# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt-python-sdk.models.query_similarity_task_request import QuerySimilarityTaskRequest

class TestQuerySimilarityTaskRequest(unittest.TestCase):
    """QuerySimilarityTaskRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuerySimilarityTaskRequest:
        """Test QuerySimilarityTaskRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuerySimilarityTaskRequest`
        """
        model = QuerySimilarityTaskRequest()
        if include_optional:
            return QuerySimilarityTaskRequest(
                post_back_url = '',
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
                query = ''
            )
        else:
            return QuerySimilarityTaskRequest(
        )
        """

    def testQuerySimilarityTaskRequest(self):
        """Test QuerySimilarityTaskRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
