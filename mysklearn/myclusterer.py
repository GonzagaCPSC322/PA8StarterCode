from mysklearn import myutils

class MyKMeansClusterer:
    """Represents a k-means clusterer.

    Attributes:
        n_clusters(int): The number of clusters to form
        init(list of list): List of initial cluster centers (default None)
            If not None, it should be of shape (n_clusters, n_features)
        X_train(list of list of obj): The list of training instances (samples)
                The shape of X_train is (n_train_samples, n_features)
        cluster_centers_(list of list): The generated cluster centers AKA centroids
            (in order cluster #0, #1, #n_clusters-1)
        labels_(list of int): The cluster number each instance belongs to (parallel to X_train)
        inertia_(float): Sum of squared distances of samples to their closest cluster center

    Notes:
        Loosely based on Sci-kit Learn's KMeans:
            https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
        Terminology: instance = sample = row and attribute = feature = column
    """
    def __init__(self, n_clusters=8, init=None, random_state=None):
        """Initializer for MyKMeansClusterer.

        Args:
            n_clusters(int): The number of clusters to form
                (8 if a value is not provided and the default number of clusters should be used)
            init(list of list): List of initial cluster centers (default None)
                If not None, it should be of shape (n_clusters, n_features)
            random_state(int): integer used for seeding a random number generator for reproducible results
        """
        self.n_clusters = n_clusters
        self.init = init
        self.random_state = random_state
        self.X_train = None
        self.cluster_centers_ = None
        self.labels_ = None
        self.inertia_ = None

    def fit(self, X_train):
        """Fits a k-means clusterer to X_train.

        Args:
            X_train(list of list of obj): The list of training instances (samples).
                The shape of X_train is (n_train_samples, n_features)

        Notes:
            Store the generated cluster centers (AKA centroids) in cluster_centers_
            Store the X_train instance cluster number assignments (0-based) in labels_
            Store the total cluster TSS in inertia_
        """
        self.X_train = X_train
        pass # TODO: fix this

    def print_clusters(self):
        """Prints the instances belonging to each cluster, showing cluster numbers,
        original instance indexes, and instance values.

        """
        pass # TODO: fix this
