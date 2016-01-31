import unittest
from tests import common
from romaine import schemas


class TestBackgroundsParserSchemas(unittest.TestCase):
    """
        Test backgrounds results from parser comply with schema.
    """
    def setUp(self):
        """
            Prepare the environment for testing.
        """
        # We're doing a lot of long tests- don't limit the diff output length
        self.maxDiff = None

    def test_basic_background_schema(self):
        """
            Check we can get basic backgrounds.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_background with input from background/basic_input
        input_data = common.get_parser_input('background/basic_input')

        result = parser.section.get_background(input_data)

        # Then I the results match the background schema
        schemas.validate(
            data=result,
            schema_name='background',
        )

    def test_background_without_steps_schema(self):
        """
            Check we can get a background without steps.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_background with input from background/no_steps_input
        input_data = common.get_parser_input('background/no_steps_input')

        result = parser.section.get_background(input_data)

        # Then I the results match the background schema
        schemas.validate(
            data=result,
            schema_name='background',
        )

    def test_background_with_description_schema(self):
        """
            Check we can get background with description.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_background with input from
        # background/with_description_input
        input_data = common.get_parser_input(
            'background/with_description_input',
        )

        result = parser.section.get_background(input_data)

        # Then I the results match the background schema
        schemas.validate(
            data=result,
            schema_name='background',
        )

    def test_background_with_comment_schema(self):
        """
            Check we can get background with comment.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_background with input from
        # background/with_comment_input
        input_data = common.get_parser_input('background/with_comment_input')

        result = parser.section.get_background(input_data)

        # Then I the results match the background schema
        schemas.validate(
            data=result,
            schema_name='background',
        )

    def test_background_with_trailing_space_schema(self):
        """
            Check we can get a background with trailing space.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_background with input from
        # background/with_trailing_space_input
        input_data = common.get_parser_input(
            'background/with_trailing_space_input',
        )

        result = parser.section.get_background(input_data)

        # Then I the results match the background schema
        schemas.validate(
            data=result,
            schema_name='background',
        )

    def test_no_background_with_leading_noise_schema(self):
        """
            Confirm we get no background with leading noise.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_background with input from
        # background/with_leading_noise_input
        input_data = common.get_parser_input(
            'background/with_leading_noise_input',
        )

        result = parser.section.get_background(input_data)

        # Then I the results match the background schema
        schemas.validate(
            data=result,
            schema_name='background',
        )

    def test_background_with_trailing_background_schema(self):
        """
            Check we can get only one background when there are two.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_background with input from
        # background/with_trailing_background_input
        input_data = common.get_parser_input(
            'background/with_trailing_background_input',
        )

        result = parser.section.get_background(input_data)

        # Then I the results match the background schema
        schemas.validate(
            data=result,
            schema_name='background',
        )

    def test_no_background_with_no_input_schema(self):
        """
            Confirm we get no background for no input.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_background with input from background/no_input
        input_data = common.get_parser_input('background/no_input')

        result = parser.section.get_background(input_data)

        # Then I the results match the background schema
        schemas.validate(
            data=result,
            schema_name='background',
        )
