import unittest
from tests import common
from romaine import schemas


class TestElementsParserSchema(unittest.TestCase):
    """
        Test elements results from parser comply with schema.
    """
    def setUp(self):
        """
            Prepare the environment for testing.
        """
        # We're doing a lot of long tests- don't limit the diff output length
        self.maxDiff = None

    def test_get_elements_one_scenario(self):
        """
            Check we can get one scenario.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_elements with input from
        # elements/one_scenario_input
        input_data = common.get_parser_input(
            'elements/one_scenario_input',
        )

        result = parser.section.get_elements(input_data)

        # Then I the results match the elements schema
        schemas.validate(
            data=result,
            schema_name='elements',
        )

    def test_get_elements_one_outline(self):
        """
            Check we can get one scenario outline.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_elements with input from
        # elements/one_outline_input
        input_data = common.get_parser_input(
            'elements/one_outline_input',
        )

        result = parser.section.get_elements(input_data)

        # Then I the results match the elements schema
        schemas.validate(
            data=result,
            schema_name='elements',
        )

    def test_get_multiple_elements(self):
        """
            Check we can get more than one scenario/outline.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_elements with input from
        # elements/multiple_elements_input
        input_data = common.get_parser_input(
            'elements/multiple_elements_input',
        )

        result = parser.section.get_elements(input_data)

        # Then I the results match the elements schema
        schemas.validate(
            data=result,
            schema_name='elements',
        )

    def test_get_multiple_elements_trailing_noise(self):
        """
            Check we don't eat trailing noise with elements.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_elements with input from
        # elements/multiple_elements_trailing_noise_input
        input_data = common.get_parser_input(
            'elements/multiple_elements_trailing_noise_input',
        )

        result = parser.section.get_elements(input_data)

        # Then I the results match the elements schema
        schemas.validate(
            data=result,
            schema_name='elements',
        )

    def test_get_elements_one_scenario_with_empty(self):
        """
            Check we cannot get one scenario with leading noise.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_elements with input from
        # elements/empty_input
        input_data = common.get_parser_input(
            'elements/empty_input',
        )

        result = parser.section.get_elements(input_data)

        # Then I the results match the elements schema
        schemas.validate(
            data=result,
            schema_name='elements',
        )

    def test_get_no_elements_from_nothing(self):
        """
            Check we cannot get any elements from nothing.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_elements with input from
        # elements/empty_input
        input_data = common.get_parser_input(
            'elements/empty_input',
        )

        result = parser.section.get_elements(input_data)

        # Then I the results match the elements schema
        schemas.validate(
            data=result,
            schema_name='elements',
        )
