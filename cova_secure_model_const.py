MODEL_IMPORT_MAPS = {
    'ols' : 'linear_model',
    'ridge': 'linear_model',
    'lasso': 'linear_model',
    'elastic_net': 'linear_model',
    'log_reg': 'linear_model',
    'kernel_ridge': 'kernel_ridge',
    'svc' : 'svm',
    'svr' : 'svm',
    'GaussianNB' : 'naive_bayes',
    'BernoulliNB' : 'naive_bayes',
    'MultinomialNB' : 'naive_bayes',
	'dec_treeC' : 'tree',
	'dec_treeR' : 'tree',
	'rfc' : 'ensemble',
	'rfr' : 'ensemble',
	'MLPC' : 'neural_network',
	'MLPR' : 'neural_network',
	'KMeans' : 'cluster',
	'MiniBatchKMeans' : 'cluster',
	'AffinityPropagation' : 'cluster',
	'MeanShift' : 'cluster',
	'Spectral_Clustering' : 'cluster',
	'Hierarchical_Clustering' : 'cluster',
	'DBSCAN' : 'cluster',
	'Birch' : 'cluster',
	'GaussianMixture' : 'mixture',
	'BayesianGaussianMixture' : 'mixture'
}
MODEL_IMPORT_MAPS2 = {
    'ols' : 'LinearRegression',
    'ridge': 'Ridge',
    'lasso': 'Lasso',
    'elastic_net': 'ElasticNet',
    'log_reg': 'LogisticRegression',
    'kernel_ridge': 'KernelRidge',
    'svc' : 'SVC',
    'svr' : 'SVR',
    'GaussianNB' : 'GaussianNB',
    'BernoulliNB' : 'BernoulliNB',
    'MultinomialNB' : 'MultinomialNB',
	'dec_treeC' : 'DecisionTreeClassifier',
	'dec_treeR' : 'DecisionTreeRegressor',
	'rfc' : 'RandomForestClassifier',
	'rfr' : 'RandomForestRegressor',
	'MLPC' : 'MLPClassifier',
	'MLPR' : 'MLPRegressor',
	'KMeans' : 'KMeans',
	'MiniBatchKMeans' : 'MiniBatchKMeans',
	'AffinityPropagation' : 'AffinityPropagation',
	'MeanShift' : 'MeanShift',
	'Spectral_Clustering' : 'SpectralClustering',
	'Hierarchical_Clustering' : 'AgglomerativeClustering',
	'DBSCAN' : 'DBSCAN',
	'Birch' : 'Birch',
	'GaussianMixture' : 'GaussianMixture',
	'BayesianGaussianMixture' : 'BayesianGaussianMixture'
}
S3_BUCKET_PATH = 's3/path/to/encrypted/dataset'
DOCKER_VOLUME_PATH = '/home/docker_vol/'
