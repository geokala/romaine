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
            # Each element in the walked paths is:
            # base_directory, [list of dirs], [list of files]
            for feature_file in walked_path[2]:
                feature_candidates.append(
                    os.path.join(
                        walked_path[0],
                        feature_file
                        )
                    )

        self.features.extend(feature_candidates)

        return feature_candidates
