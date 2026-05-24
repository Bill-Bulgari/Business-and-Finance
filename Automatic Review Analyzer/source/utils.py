import csv
import numpy as np
import matplotlib.pyplot as plt

from . import core
import sys

if sys.version_info[0] < 3:
    PYTHON3 = False
else:
    PYTHON3 = True

def load_toy_data(path_toy_data):
    """
    Loads the 2D toy dataset as numpy arrays.
    Returns the tuple (features, labels) in which features is an Nx2 numpy matrix and
    labels is a length-N vector of +1/-1 labels.
    """
    labels, xs, ys = np.loadtxt(path_toy_data, delimiter='\t', unpack=True)
    return np.vstack((xs, ys)).T, labels

def load_data(path_data, extras=False):
    """
    Returns a list of dict with keys:
    * sentiment: +1 or -1 if the review was positive or negative, respectively
    * text: the text of the review

    Additionally, if the `extras` argument is True, each dict will also include the
    following information:
    * productId: a string that uniquely identifies each product
    * userId: a string that uniquely identifies each user
    * summary: the title of the review
    * helpfulY: the number of users who thought this review was helpful
    * helpfulN: the number of users who thought this review was NOT helpful
    """

    global PYTHON3

    basic_fields = {'sentiment', 'text'}
    numeric_fields = {'sentiment', 'helpfulY', 'helpfulN'}

    data = []
    if PYTHON3:
        f_data = open(path_data, encoding="latin1")
    else:
        f_data = open(path_data)

    for datum in csv.DictReader(f_data, delimiter='\t'):
        for field in list(datum.keys()):
            if not extras and field not in basic_fields:
                del datum[field]
            elif field in numeric_fields and datum[field]:
                datum[field] = int(datum[field])

        data.append(datum)

    f_data.close()

    return data

def plot_toy_data(algo_name, features, labels, thetas):
    """
    Plots the toy data in 2D.
    Arguments:
    * features - an Nx2 ndarray of features (points)
    * labels - a length-N vector of +1/-1 labels
    * thetas - the tuple (theta, theta_0) that is the output of the learning algorithm
    * algorithm - the string name of the learning algorithm used
    """
    # plot the points with labels represented as colors
    plt.subplots()
    colors = ['b' if label == 1 else 'r' for label in labels]
    plt.scatter(features[:, 0], features[:, 1], s=40, c=colors)
    xmin, xmax = plt.axis()[:2]

    # plot the decision boundary
    theta, theta_0 = thetas
    xs = np.linspace(xmin, xmax)
    ys = -(theta[0]*xs + theta_0) / (theta[1] + 1e-16)
    plt.plot(xs, ys, 'k-')

    # show the plot
    algo_name = ' '.join((word.capitalize() for word in algo_name.split(' ')))
    plt.suptitle('Classified Toy Data ({})'.format(algo_name))
    plt.show()

def plot_tune_results(algo_name, param_name, param_vals, acc_train, acc_val):
    """
    Plots classification accuracy on the training and validation data versus
    several values of a hyperparameter used during training.
    """
    # put the data on the plot
    plt.subplots()
    plt.plot(param_vals, acc_train, '-o')
    plt.plot(param_vals, acc_val, '-o')

    # make the plot presentable
    algo_name = ' '.join((word.capitalize() for word in algo_name.split(' ')))
    param_name = param_name.capitalize()
    plt.suptitle('Classification Accuracy vs {} ({})'.format(param_name, algo_name))
    plt.legend(['train','val'], loc='upper right', title='Partition')
    plt.xlabel(param_name)
    plt.ylabel('Accuracy (%)')
    plt.show()

def tune(train_fn, param_vals, train_feats, train_labels, val_feats, val_labels):
    train_accs = np.ndarray(len(param_vals))
    val_accs = np.ndarray(len(param_vals))

    for i, val in enumerate(param_vals):
        theta, theta_0 = train_fn(train_feats, train_labels, val)

        train_preds = core.classify(train_feats, theta, theta_0)
        train_accs[i] = core.accuracy(train_preds, train_labels)

        val_preds = core.classify(val_feats, theta, theta_0)
        val_accs[i] = core.accuracy(val_preds, val_labels)

    return train_accs, val_accs

def tune_perceptron(*args):
    return tune(core.perceptron, *args)

def tune_avg_perceptron(*args):
    return tune(core.average_perceptron, *args)

def tune_pegasos(Ts, Ls, train_feats, train_labels, val_feats, val_labels):
    """
    Full grid search for Pegasos over all (T, L) pairs in Ts x Ls.

    Returns:
        train_accs: 2D array with shape (len(Ts), len(Ls))
        val_accs:   2D array with shape (len(Ts), len(Ls))
        best_T:     T giving the best validation accuracy
        best_L:     L giving the best validation accuracy
    """
    train_accs = np.zeros((len(Ts), len(Ls)))
    val_accs = np.zeros((len(Ts), len(Ls)))

    best_val_acc = -np.inf
    best_train_acc = -np.inf
    best_T = None
    best_L = None

    for i, T in enumerate(Ts):
        for j, L in enumerate(Ls):
            train_acc, val_acc = core.classifier_accuracy(
                core.pegasos,
                train_feats,
                val_feats,
                train_labels,
                val_labels,
                T=T,
                L=L
            )

            train_accs[i, j] = train_acc
            val_accs[i, j] = val_acc

            if val_acc > best_val_acc:
                best_val_acc = val_acc
                best_train_acc = train_acc
                best_T = T
                best_L = L
            elif val_acc == best_val_acc and train_acc > best_train_acc:
                best_train_acc = train_acc
                best_T = T
                best_L = L

    return train_accs, val_accs, best_T, best_L

def most_explanatory_word(theta, wordlist):
    """Returns the word associated with the bag-of-words feature having largest weight."""
    return [word for (theta_i, word) in sorted(zip(theta, wordlist))[::-1]]
