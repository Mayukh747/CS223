# https://www.askpython.com/python/examples/principal-component-analysis#:~:text=Steps%20to%20implement%20PCA%20in%20Python%201%201.,matrix%20...%206%206.%20Transform%20the%20data%20

# Importing required libraries
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# Generate a 2D dataset of integer numbers.
num_rows = 20   # The number of records (i.e., rows) in a dataset
num_cols = 5    # The number of parameters/features (i.e., cols) for each
lowest_int_num = 10
highest_int_num = 50    # Actually the value specified here is 1 more than the highest
num_of_nums_to_generate = 100
# NOTE: The reshape member fun will take the number of generated numbers as
# specified by num_of_nums_to_generate   and generates a 2D matrix of the generated numbers.
# This means the value of num_of_nums_to_generate  must =  num_rows * num_cols.
X = np.random.randint(lowest_int_num,
                      highest_int_num,
                      num_of_nums_to_generate).reshape(num_rows,num_cols)


# mean Centering the data
X_meaned = X - np.mean(X , axis = 0)

# calculating the covariance matrix of the mean-centered data.
cov_mat = np.cov(X_meaned , rowvar = False)

# Calculating Eigenvalues and Eigenvectors of the covariance matrix
eigen_values , eigen_vectors = np.linalg.eigh(cov_mat)

# Sort the eigenvalues in descending order
sorted_index = np.argsort(eigen_values)[::-1]
sorted_eigenvalue = eigen_values[sorted_index]

# Similarly sort the eigenvectors
sorted_eigenvectors = eigen_vectors[:,sorted_index]

# Select the first n eigenvectors, n is desired dimension
# of our final reduced data.
n_components = 2 # You can select any number of components.
eigenvector_subset = sorted_eigenvectors[:,0:n_components]

# Transform the data
X_reduced = np.dot(eigenvector_subset.transpose(),X_meaned.transpose()).transpose()

print("X_reduced:\n", X_reduced)
#import sys
#sys.exit()

def PCA(X , num_components):

    # Step-1
    X_meaned = X - np.mean(X , axis = 0)

    # Step-2
    cov_mat = np.cov(X_meaned , rowvar = False)

    # Step-3
    eigen_values , eigen_vectors = np.linalg.eigh(cov_mat)

    # Step-4
    sorted_index = np.argsort(eigen_values)[::-1]
    sorted_eigenvalue = eigen_values[sorted_index]
    sorted_eigenvectors = eigen_vectors[:,sorted_index]

    # Step-5
    eigenvector_subset = sorted_eigenvectors[:,0:num_components]

    # Step-6
    X_reduced = np.dot(eigenvector_subset.transpose() , X_meaned.transpose() ).transpose()

    return X_reduced



# Get the IRIS dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
data = pd.read_csv(url, names=['sepal length','sepal width','petal length','petal width','target'])

# prepare the data
x = data.iloc[:,0:4]

# prepare the target
target = data.iloc[:,4]

# Applying it to PCA function
mat_reduced = PCA(x , 2)
#print("mat_reduced:\n", mat_reduced)


# Creating a Pandas DataFrame of reduced Dataset
principal_df = pd.DataFrame(mat_reduced , columns = ['PC1','PC2'])

# Concat it with target variable to create a complete Dataset
principal_df = pd.concat([principal_df , pd.DataFrame(target)] , axis = 1)

plt.figure(figsize = (6,6))
sb.scatterplot(data = principal_df , x = 'PC1',y = 'PC2' , hue = 'target' , s = 60 , palette= 'icefire')
plt.show()








