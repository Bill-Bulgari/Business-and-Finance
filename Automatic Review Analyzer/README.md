# Automatic Review Analyzer

Automatic Review Analyzer is a machine learning project for binary sentiment classification of product reviews. The project implements linear classifiers from scratch and applies them to text data represented with bag-of-words features. The goal is to classify each review as either positive or negative using simple, interpretable machine learning methods.

## Project Overview

This project studies three linear classification algorithms:

- Perceptron
- Average Perceptron
- Pegasos

The notebook builds the full workflow step by step:

- Load product-review data.
- Convert review text into bag-of-words feature vectors.
- Train linear classifiers.
- Compare training and validation accuracy.
- Tune hyperparameters.
- Evaluate the selected model on held-out test data.
- Inspect the most explanatory word features.
- Compare different Feature Engineering choices.

## Repository Structure

```text
Automatic Review Analyzer/
├── README.md
├── Automatic Review Analyzer.ipynb
└── source/
    ├── core.py
    ├── utils.py
    └── data/
        ├── reviews_train.tsv
        ├── reviews_val.tsv
        ├── reviews_test.tsv
        ├── toy_data.tsv
        └── stopwords.txt
```

## Files

- `Automatic Review Analyzer.ipynb` contains the full project notebook with explanations, mathematical background, experiments, plots, results, and conclusions.
- `source/core.py` contains the implementations of the classifiers, feature extraction, prediction, and accuracy functions.
- `source/utils.py` contains helper functions for loading data, plotting, tuning hyperparameters, and finding explanatory word features.
- `source/data/` contains the review datasets, toy dataset, and stopword list.

## Methods

The project uses a binary bag-of-words representation. Each review is converted into a feature vector whose coordinates indicate whether a word appears in the review. For a feature vector $x \in \mathbb{R}^d$, the classifiers use a linear score

$$
s(x) = \theta \cdot x + \theta_0.
$$

The predicted label is

$$
\hat y(x) =
\begin{cases}
+1, & \theta \cdot x + \theta_0 > 0, \\
-1, & \theta \cdot x + \theta_0 \leq 0.
\end{cases}
$$

The notebook compares the behavior of Perceptron, Average Perceptron, and Pegasos under the same feature representation.

## Feature Engineering

The project includes Feature Engineering experiments that compare:

- the original bag-of-words dictionary,
- stopword removal,
- binary word-presence features,
- count-based word-frequency features.

The results show that adding more information does not always improve performance. In this dataset, binary features can behave better than count features because count features may introduce irrelevant variation and overfitting.

## Installation

Create a Python environment and install the required packages:

```bash
pip install numpy matplotlib jupyter
```

## How to Run

Open:

```text
Automatic Review Analyzer.ipynb
```

Then run all cells from top to bottom. The notebook expects this relative folder structure to be preserved:

```text
source/
├── core.py
├── utils.py
└── data/
```

Do not move or rename the `source/` or `source/data/` folders unless you also update the paths in the notebook and source files.

## Notes on Reproducibility

The implemented classifiers are online learning algorithms, meaning that the order of the training examples affects the learned parameters. This project uses a deterministic update order so that results are reproducible within this repository. Small numerical differences may occur if the update order, preprocessing rules, or tuning procedure are changed.

## Reference

S. Shalev-Shwartz, Y. Singer, N. Srebro, A. Cotter - [*Pegasos: Primal Estimated sub-GrAdient SOlver for SVM*](https://home.ttic.edu/~nati/Publications/PegasosMPB.pdf)
