import os
import sys
from tests import exceptions

# Allow the tests to work from a tests subdir, then import the test target
test_path = os.path.dirname(__file__)
package_directory = os.path.join(os.path.split(test_path)[0], 'src')
sys.path.append(package_directory)

# Module to be tested
import romaine  # noqa


def create_feature_test_trees(feature_paths=('tests/features',
                                             '/tmp/romaine_tests/features'),
                              features=('feature1',
                                        'feature2',
                                        'subdir/feature3')):
    """
        Creates test directory trees with sample feature files.

        Keyword Arguments:
        feature_paths -- List of paths to create feature files in.
        features -- List of feature files to create relative to feature path.

        Returns:
        None.
    """
    for base_path in feature_paths:
        try:
            os.makedirs(os.path.join(base_path, 'subdir'))
        except OSError:
            # Raised if the directory exists, no action required
            pass

        for feature in features:
            feature_path = os.path.join(base_path, feature)

            with open(feature_path, 'a'):
                # No need to write anything, the file should now exist
                pass


def purge_feature_test_trees(feature_paths=('tests/features',
                                            '/tmp/romaine_tests/features'),
                             features=('feature1',
                                       'feature2',
                                       'subdir/feature3')):
    """
        Purges test feature files and directories.
        Keyword Arguments:
        feature_paths -- List of feature file test directories to remove.
        features -- List of feature files relative to feature_paths to remove.

        Returns:
        None.
    """
    for base_path in feature_paths:
        # Remove the feature files
        for feature in features:
            feature = os.path.join(base_path, feature)
            os.remove(feature)

        # Attempt to remove all the directories we created
        os.removedirs(os.path.join(base_path, 'subdir'))


def do_not_run_as_root():
    """
        Perform simple check to see if we're running as root and then fail
        noisily if we are. This is intended to avoid any little accidents with
        parts of test code that purge files and directories.

        This can almost certainly be defeated easily, but is only intended to
        stop people from accidentally shooting themselves in the foot as root,
        rather than deliberate self sabotage.

        Keyword arguments:
        None.

        Returns:
        None.
    """
    if os.geteuid() == 0:
        raise exceptions.RunningAsRootError(
            'Running as root may be harmful, aborting.'
            )
