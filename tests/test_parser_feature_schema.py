import unittest
from tests import common
from romaine import schemas


class TestFeatureParserSchema(unittest.TestCase):
    """
        Test feature results from parser comply with the schema.
    """
    def setUp(self):
        """
            Prepare the environment for testing.
        """
        # We're doing a lot of long tests- don't limit the diff output length
        self.maxDiff = None

    def test_get_feature(self):
        """
            Check we can get a feature.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_feature with input from background/basic_input
        input_data = common.get_parser_input('feature/basic_input')

        result = parser.feature.get_feature(input_data)

        # Then I the results match the feature schema
        schemas.validate(
            data=result,
            schema_name='feature',
        )
