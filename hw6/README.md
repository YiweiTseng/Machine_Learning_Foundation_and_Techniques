# Experiments with Decision Tree and Random Forest

14. (Lecture 209, *) First, let’s implement a simple C&RT algorithm without pruning using the Gini index as the impurity measure, as introduced in the class. For the decision stump used in branching, if you are branching with feature i, please sort all the x_n,i values to form (at most) N + 1 segments of equivalent θ, and then pick θ within the median of the segment. If multiple (i,θ) produce the best split, pick the one with the smallest i (and if there is a tie again, pick the one with the smallest θ).
Please run the algorithm on the following set for training:

    http://www.csie.ntu.edu.tw/~htlin/course/ml20fall/hw6/hw6_train.dat

    and the following file as our test data set for evaluating Eout:

    http://www.csie.ntu.edu.tw/~htlin/course/ml20fall/hw6/hw6_test.dat
               
    What is the Eout(g), where g is the unpruned decision tree returned from your C&RT algorithm and Eout is evaluated using the 0/1 error? Choose the closest    answer;   provide your code.

    [a] 0.08 [b] 0.13 [c] 0.18 [d] 0.23 [e] 0.28
