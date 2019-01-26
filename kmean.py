'''
A simple demonstration of using the OpenCV k-means function
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt

if __name__ == '__main__':

    # Seed the random number generator used by np.random
    np.random.seed(seed=12345)

    # Generate random values from three different two-dimensional normal distributions.
    mean1 = np.array([1.0,7.0])
    cov1 = np.array([[3.5, 0.5],[0.5, 1.5]])
    values1 = np.random.multivariate_normal(mean1, cov1, 250)

    mean2 = np.array([5.0,1.0])
    cov2 = np.array([[2.5, 0.1],[0.1, 1.5]])
    values2 = np.random.multivariate_normal(mean2, cov2, 50)

    mean3 = np.array([12.0,8.0])
    cov3 = np.array([[2.5, 0.1],[0.1, 1.5]])
    values3 = np.random.multivariate_normal(mean3, cov3, 50)

    # Concatenate the values
    all_values = np.concatenate((values1, values2, values3)).astype(np.float32)

    # Specify the termination criteria, including the number of iterations and
    # an upper bound on the amount of change in the position of the center.
    num_clusters = 5   # this is K
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 1.0)
    num_reinitializations = 1
    # initialization_method = cv2.KMEANS_RANDOM_CENTERS
    initialization_method = cv2.KMEANS_PP_CENTERS
    ret, label, center = cv2.kmeans(all_values, num_clusters, None, criteria,
                                    num_reinitializations, initialization_method)
    print(center)

    for i in range(num_clusters):
        cluster = all_values[label.ravel() == i]
        x = cluster[:, 0]
        y = cluster[:, 1]
        print('Cluster %d: %d points' % (i, len(x)))
        c = np.random.random(3).reshape(1,3)
        plt.scatter(x, y, c=c)
    plt.scatter(center[:,0],center[:,1],s = 80,c = 'y', marker = 's')
    plt.axis('equal')
    plt.show()

