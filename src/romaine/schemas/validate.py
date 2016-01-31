import json
import os
import sys


def validate(data, schema_name):
    # This does not feel like the best approach, but I cannot find another way
    # that is testable.
    try:
        import jsonschema
    except ImportError:
        # jsonschema not installed, do not validate
        return None
    else:
        package_location = os.path.dirname(
            sys.modules['romaine'].__file__,
        )
        schemas_path = os.path.join(package_location, 'schemas')

        resolver = jsonschema.RefResolver(
            'file://{schema_dir}/'.format(schema_dir=schemas_path),
            None,
        )

        schema_path = os.path.join(
            schemas_path,
            '{schema}.json'.format(schema=schema_name),
        )

        with open(schema_path) as schema_handle:
            schema = json.load(schema_handle)

        # This raises an exception if validation fails
        jsonschema.validate(
            instance=data,
            schema=schema,
            resolver=resolver,
        )
