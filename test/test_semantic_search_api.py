# coding: utf-8

"""
    FlowHunt

    FlowHunt API

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from flowhunt.semantic_search_api import SemanticSearchApi


class TestSemanticSearchApi(unittest.TestCase):
    """SemanticSearchApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SemanticSearchApi()

    def tearDown(self) -> None:
        pass

    def test_get_similar_docs_by_doc_id(self) -> None:
        """Test case for get_similar_docs_by_doc_id

        Get Similar Docs By Doc Id
        """
        pass

    def test_get_similar_docs_by_query(self) -> None:
        """Test case for get_similar_docs_by_query

        Get Similar Docs By Query
        """
        pass

    def test_schedule_similar_docs_by_doc_id(self) -> None:
        """Test case for schedule_similar_docs_by_doc_id

        Schedule Similar Docs By Doc Id
        """
        pass

    def test_schedule_similar_docs_by_query(self) -> None:
        """Test case for schedule_similar_docs_by_query

        Schedule Similar Docs By Query
        """
        pass


if __name__ == '__main__':
    unittest.main()