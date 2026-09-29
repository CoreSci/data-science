"""scikit-learn in five lines: train a classifier on handwritten digits.

Problem: show the basic estimator API (``fit`` / ``predict``) end to end on a
real dataset.

How it works: fit an RBF support-vector classifier (gamma=0.001, C=100) on all
of the 8x8 digit images except the last one, then predict that held-out image.

Data: scikit-learn's bundled ``digits`` dataset (1,797 images of 8x8 pixels).

Adapted from: scikit-learn documentation, "An introduction to machine learning
with scikit-learn" tutorial.

Run: ``python sklearn_digits_quickstart.py``
"""
from sklearn import datasets, svm

if __name__ == "__main__":
    digits = datasets.load_digits()
    print("data shape:", digits.data.shape, "| classes:", sorted(set(digits.target)))
    print("first image (8x8 grey levels):\n", digits.images[0])

    # learning and predicting
    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(digits.data[:-1], digits.target[:-1])
    prediction = clf.predict(digits.data[-1:])

    print("model:", clf)
    print("predicted digit for the held-out image:", prediction[0], "| true label:", digits.target[-1])
