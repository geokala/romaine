from romaine import schemas
import mock
import sys
import unittest


real_import = __import__


def no_jsonschema_import(*args):
    if args[0] == 'jsonschema':
        raise ImportError()
    else:
        return real_import(*args)


class TestSchemaNoJsonschema(unittest.TestCase):
    """
        Test schemas with no jsonschema
    """
    def setUp(self):
        """
            Prepare the environment for testing.
        """
        # We're doing a lot of long tests- don't limit the diff output length
        self.maxDiff = None

    def test_validate_no_jsonschema(self):
        """
            Test correct result when jsonschema is missing.
        """
        if sys.version[0] == '2':
            import_builtin = '__builtin__.__import__'
        else:
            import_builtin = 'builtins.__import__'
        with mock.patch(import_builtin,
                        side_effect=no_jsonschema_import):
            self.assertIsNone(schemas.validate({}, 'steps'))
