import os
import sys

# Allow the tests to work from a tests subdir, then import the test target
test_path = os.path.dirname(__file__)
package_directory = os.path.join(os.path.split(test_path)[0], 'src')
sys.path.append(package_directory)
sys.path.append(os.path.split(test_path)[0])

# Module to be tested
import romaine  # noqa
