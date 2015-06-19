import os


class Core(object):
    """
        The core of the Romaine, provides BDD test API.
    """
    # All located features
    features = []
    instance = None

    def __init__(self):
        """
            Initialise Romaine core.
        """
        self.steps = {}
        Core.instance = self

    def locate_features(self, path):
        """
            Locate any features given a path.

            Keyword arguments:
            path -- The path to search for features, recursively.

            Returns:
            List of features located in the path.
        """
        walked_paths = os.walk(path)

        feature_candidates = []

        for walked_path in walked_paths:
            base_directory, sub_directories, feature_files = walked_path
            for feature_file in feature_files:
                feature_candidates.append(
                    os.path.join(
                        base_directory,
                        feature_file
                        )
                    )

        self.features.extend(feature_candidates)

        return feature_candidates
