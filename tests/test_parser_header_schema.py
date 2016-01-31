import unittest
from tests import common
from romaine import schemas


class TestHeaderParserSchemas(unittest.TestCase):
    """
        Test header results from parser comply with schema.
    """
    def setUp(self):
        """
            Prepare the environment for testing.
        """
        # We're doing a lot of long tests- don't limit the diff output length
        self.maxDiff = None

    def test_just_header(self):
        """
            Check we can get a header alone.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_header with input from header/basic_input
        input_data = common.get_parser_input('header/basic_input')

        result = parser.section.get_header(input_data)

        # Then I the results match the header schema
        schemas.validate(
            data=result,
            schema_name='header',
        )

    def test_header_with_scenario_and_noise(self):
        """
            Check we can get a header without eating the following scenario.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_header with input from header/with_scenario_input
        input_data = common.get_parser_input('header/with_scenario_input')

        result = parser.section.get_header(input_data)

        # Then I the results match the header schema
        schemas.validate(
            data=result,
            schema_name='header',
        )

    def test_header_with_scenario_outline_and_noise(self):
        """
            Check we can get a header without eating the following outline.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_header with input from
        # header/with_scenario_outline_input
        input_data = common.get_parser_input(
            'header/with_scenario_outline_input',
        )

        result = parser.section.get_header(input_data)

        # Then I the results match the header schema
        schemas.validate(
            data=result,
            schema_name='header',
        )

    def test_header_with_background_and_noise(self):
        """
            Check we can get a header without eating the following background.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_header with input from
        # header/with_background_input
        input_data = common.get_parser_input(
            'header/with_background_input',
        )

        result = parser.section.get_header(input_data)

        # Then I the results match the header schema
        schemas.validate(
            data=result,
            schema_name='header',
        )

    def test_no_header_from_nothing(self):
        """
            Confirm we get no header from no input.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_header with input from header/empty_input
        input_data = common.get_parser_input(
            'header/empty_input',
        )

        result = parser.section.get_header(input_data)

        # Then I the results match the header schema
        schemas.validate(
            data=result,
            schema_name='header',
        )
