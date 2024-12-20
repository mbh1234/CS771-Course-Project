import numpy as np
import sklearn
from scipy.linalg import khatri_rao

from sklearn.linear_model import LogisticRegression
# You are allowed to import any submodules of sklearn that learn linear models e.g. sklearn.svm etc
# You are not allowed to use other libraries such as keras, tensorflow etc
# You are not allowed to use any scipy routine other than khatri_rao

# SUBMIT YOUR CODE AS A SINGLE PYTHON (.PY) FILE INSIDE A ZIP ARCHIVE
# THE NAME OF THE PYTHON FILE MUST BE submit.py

# DO NOT CHANGE THE NAME OF THE METHODS my_fit, my_map etc BELOW
# THESE WILL BE INVOKED BY THE EVALUATION SCRIPT. CHANGING THESE NAMES WILL CAUSE EVALUATION FAILURE

# You may define any new functions, variables, classes here
# For example, functions to calculate next coordinate or step length

################################
# Non Editable Region Starting #
################################
def my_fit( X_train, y_train ):
################################
#  Non Editable Region Ending  #
################################

	# Use this method to train your model using training CRPs
	# X_train has 32 columns containing the challeenge bits
	# y_train contains the responses
	
	# THE RETURNED MODEL SHOULD BE A SINGLE VECTOR AND A BIAS TERM
	# If you do not wish to use a bias term, set it to 0
	
	#now, X-train has 32 columns. Y-train has 1 column. From X-train(of 32 columns, we should create a 528 column feature vector)
	#hence giving X-train as input, we need to get feature vectors from my_map() fucntion
	features = my_map(X_train)

	model = LogisticRegression()

	# Fit the model to the training data
	model.fit(features, y_train)

	# Print the coefficients and intercept of the model
	w = model.coef_
	b = model.intercept_

	return w[0], b


################################
# Non Editable Region Starting #
################################
def my_map( X ):
################################
#  Non Editable Region Ending  #
################################

	# Use this method to create features.
	# It is likely that my_fit will internally call my_map to create features for train points
	#we are taking an input of 32 features and now we need to return a 528 column feature
	#the inputs are [c0, c1,........., c31]
	#d-vector is formed as [1-2c0, 1-2c1,............,1-2c31]= [do,d1,d2,.....,d31]
	#now we first decide the features as x0,x1,x2,.........,x31,xixj
	#we first form the x-vector [x0,x1,x2,............,x31]
	#xi = d31.d30.....di
	#next, we form the xixj vector from xi vector
	# Step 1: Create columns d_i as 1 - 2 * c_i for each column c_i
    d_columns = 1 - 2 * X 

    # Step 2: Create columns x_i as the product of d_31 * d_30 * ... * d_i
    x_columns = np.zeros_like(d_columns) 
    for i in range(32):
        x_columns[:, i] = np.prod(d_columns[:, i:], axis=1)

    # Step 3: Create columns x_ix_j where i < j
    x_ix_j_columns = np.zeros((x_columns.shape[0], 496))
    idx = 0
    for i in range(32):
        for j in range(32):  # Adjusted loop to include all combinations
            if i < j:
                x_ix_j_columns[:, idx] = x_columns[:, i] * x_columns[:, j]
                idx += 1

    # Concatenate x_columns and x_ix_j_columns along the column axis
    total_feature_vector = np.concatenate((x_columns, x_ix_j_columns), axis=1)
    return total_feature_vector

