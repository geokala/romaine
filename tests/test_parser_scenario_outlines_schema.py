import unittest
from tests import common
from romaine import schemas


class TestScenarioOutlinesParserSchema(unittest.TestCase):
    """
        Test scenario outlines results from parser comply with schema.
    """
    def setUp(self):
        """
            Prepare the environment for testing.
        """
        # We're doing a lot of long tests- don't limit the diff output length
        self.maxDiff = None

    def test_basic_scenario_outline(self):
        """
            Check we can get basic scenario outlines.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_element with input from
        # scenario_outline/basic_input
        input_data = common.get_parser_input(
            'scenario_outline/basic_input',
        )

        result = parser.section.get_element(input_data)

        # Then I the results match the scenario_outline schema
        schemas.validate(
            data=result,
            schema_name='scenario_outline',
        )

    def test_basic_scenario_outline_without_examples(self):
        """
            Check we can get basic scenario outlines without examples.
        """
        # Note: We want to be able to do this to allow for, e.g. populating
        # scenario outlines based on hooks

        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_element with input from
        # scenario_outline/no_examples_input
        input_data = common.get_parser_input(
            'scenario_outline/no_examples_input',
        )

        result = parser.section.get_element(input_data)

        # Then I the results match the scenario_outline schema
        schemas.validate(
            data=result,
            schema_name='scenario_outline',
        )

    def test_basic_scenario_outline_with_leading_comment(self):
        """
            Check we can get basic scenario outline with leading comment.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_element with input from
        # scenario_outline/leading_comment_input
        input_data = common.get_parser_input(
            'scenario_outline/leading_comment_input',
        )

        result = parser.section.get_element(input_data)

        # Then I the results match the scenario_outline schema
        schemas.validate(
            data=result,
            schema_name='scenario_outline',
        )

    def test_basic_scenario_outline_with_trailing_space(self):
        """
            Check we can get basic scenario outline with trailing space.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_element with input from
        # scenario_outline/trailing_space_input
        input_data = common.get_parser_input(
            'scenario_outline/trailing_space_input',
        )

        result = parser.section.get_element(input_data)

        # Then I the results match the scenario_outline schema
        schemas.validate(
            data=result,
            schema_name='scenario_outline',
        )

    def test_basic_scenario_outline_leading_comment_and_trailing_space(self):
        """
            Check we can get scenario outline with comment and trailing space.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_element with input from
        # scenario_outline/leading_comment_trailing_space_input
        input_data = common.get_parser_input(
            'scenario_outline/leading_comment_trailing_space_input',
        )

        result = parser.section.get_element(input_data)

        # Then I the results match the scenario_outline schema
        schemas.validate(
            data=result,
            schema_name='scenario_outline',
        )

    def test_basic_scenario_outline_no_steps(self):
        """
            Check we can get basic scenario outline without steps.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_element with input from
        # scenario_outline/no_steps_input
        input_data = common.get_parser_input(
            'scenario_outline/no_steps_input',
        )

        result = parser.section.get_element(input_data)

        # Then I the results match the scenario_outline schema
        schemas.validate(
            data=result,
            schema_name='scenario_outline',
        )

    def test_basic_scenario_outline_with_description(self):
        """
            Check we can get basic scenario outline with description.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_element with input from
        # scenario_outline/with_description_input
        input_data = common.get_parser_input(
            'scenario_outline/with_description_input',
        )

        result = parser.section.get_element(input_data)

        # Then I the results match the scenario_outline schema
        schemas.validate(
            data=result,
            schema_name='scenario_outline',
        )

    def test_basic_scenario_outline_with_tags(self):
        """
            Check we can get basic scenario outline with tags.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_element with input from
        # scenario_outline/with_tags_input
        input_data = common.get_parser_input(
            'scenario_outline/with_tags_input',
        )

        result = parser.section.get_element(input_data)

        # Then I the results match the scenario_outline schema
        schemas.validate(
            data=result,
            schema_name='scenario_outline',
        )

    def test_basic_scenario_outline_with_tag_and_comment(self):
        """
            Check we can get basic scenario outline with tag and comment.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_element with input from
        # scenario_outline/with_tags_and_comment_input
        input_data = common.get_parser_input(
            'scenario_outline/with_tags_and_comment_input',
        )

        result = parser.section.get_element(input_data)

        # Then I the results match the scenario_outline schema
        schemas.validate(
            data=result,
            schema_name='scenario_outline',
        )

    def test_basic_scenario_outline_with_trailing_outline(self):
        """
            Check we can get basic scenario outline without second outline.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_element with input from
        # scenario_outline/trailing_outline_input
        input_data = common.get_parser_input(
            'scenario_outline/trailing_outline_input',
        )

        result = parser.section.get_element(input_data)

        # Then I the results match the scenario_outline schema
        schemas.validate(
            data=result,
            schema_name='scenario_outline',
        )

    def test_do_not_get_scenario_outline_with_leading_noise(self):
        """
            Confirm we get no outline with leading noise.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_element with input from
        # scenario_outline/leading_noise_input
        input_data = common.get_parser_input(
            'scenario_outline/leading_noise_input',
        )

        result = parser.section.get_element(input_data)

        # Then I the results match the scenario_outline schema
        schemas.validate(
            data=result,
            schema_name='scenario_outline',
        )

    def test_scenario_outline_with_two_examples(self):
        """
            Check we can get scenario outline with two examples sections.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_element with input from
        # scenario_outline/two_examples_sections_input
        input_data = common.get_parser_input(
            'scenario_outline/two_examples_sections_input',
        )

        result = parser.section.get_element(input_data)

        # Then I the results match the scenario_outline schema
        schemas.validate(
            data=result,
            schema_name='scenario_outline',
        )

    def test_do_not_get_scenario_from_nothing(self):
        """
            Confirm we get no outline with no input.
        """
        # Given I have Romaine core's parser
        parser = common.get_romaine_parser()

        # When I call get_element with input from
        # scenario_outline/empty_input
        input_data = common.get_parser_input(
            'scenario_outline/empty_input',
        )

        result = parser.section.get_element(input_data)

        # Then I the results match the scenario_outline schema
        schemas.validate(
            data=result,
            schema_name='scenario_outline',
        )
