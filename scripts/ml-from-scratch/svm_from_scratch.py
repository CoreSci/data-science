"""Linear support vector machine implemented from scratch with NumPy.

Problem: understand what an SVM optimiser actually does. It searches for the
smallest-norm weight vector ``w`` and a bias ``b`` such that every training point
satisfies ``y_i * (x_i . w + b) >= 1``.

How it works: a brute-force convex search. For each step size (coarse to fine),
``w`` shrinks along the diagonal while all four sign combinations of ``w`` and
a range of ``b`` values are tried. The feasible ``(w, b)`` with the smallest
``||w||`` wins. The result is plotted with the decision boundary and both
support-vector hyperplanes.

Data: two small hand-made 2-D classes, plus eight points to classify.

Adapted from: sentdex, "Practical Machine Learning with Python" tutorial series
(pythonprogramming.net), SVM-from-scratch parts.

Run: ``python svm_from_scratch.py`` (saves ``svm_from_scratch.png`` when no display is available).
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use("ggplot")

DataDict = dict[int, np.ndarray]


class Support_Vector_Machine:
    def __init__(self, visualization: bool = True) -> None:
        self.visualization = visualization
        self.colors = {1: "r", -1: "b"}
        if self.visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1, 1, 1)

    def fit(self, data: DataDict) -> None:
        """Search for the minimum-norm (w, b) that separates ``data`` ({label: points})."""
        self.data = data
        # { ||w||: [w,b] }
        opt_dict: dict[float, list] = {}

        transforms = [[1, 1],
                      [-1, 1],
                      [-1, -1],
                      [1, -1]]

        all_data = []
        for yi in self.data:
            for featureset in self.data[yi]:
                for feature in featureset:
                    all_data.append(feature)

        self.max_feature_value = max(all_data)
        self.min_feature_value = min(all_data)
        all_data = None

        # support vectors satisfy yi(xi.w+b) = 1
        step_sizes = [self.max_feature_value * 0.1,
                      self.max_feature_value * 0.01,
                      # point of expense:
                      self.max_feature_value * 0.001,
                      ]

        # b is searched on a coarser grid than w (it is far less sensitive)
        b_range_multiple = 2
        b_multiple = 5
        latest_optimum = self.max_feature_value * 10

        for step in step_sizes:
            w = np.array([latest_optimum, latest_optimum])
            # safe to walk w down monotonically because the problem is convex
            optimized = False
            while not optimized:
                for b in np.arange(-1 * (self.max_feature_value * b_range_multiple),
                                   self.max_feature_value * b_range_multiple,
                                   step * b_multiple):
                    for transformation in transforms:
                        w_t = w * transformation
                        found_option = True
                        # constraint check yi(xi.w+b) >= 1 for every point
                        # (the brute-force weak spot that SMO-style solvers avoid)
                        for i in self.data:
                            for xi in self.data[i]:
                                yi = i
                                if not yi * (np.dot(w_t, xi) + b) >= 1:
                                    found_option = False

                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t, b]

                if w[0] < 0:
                    optimized = True
                    print("Optimized a step.")
                else:
                    w = w - step

            norms = sorted([n for n in opt_dict])
            # ||w|| : [w,b]
            opt_choice = opt_dict[norms[0]]
            self.w = opt_choice[0]
            self.b = opt_choice[1]
            latest_optimum = opt_choice[0][0] + step * 2

        # functional margin of every training point (support vectors are ~1.0)
        for i in self.data:
            for xi in self.data[i]:
                yi = i
                print(xi, ":", yi * (np.dot(self.w, xi) + self.b))

    def predict(self, features: list[float]) -> float:
        """Classify one point as sign(x.w + b) and plot it as a star."""
        classification = np.sign(np.dot(np.array(features), self.w) + self.b)
        if classification != 0 and self.visualization:
            self.ax.scatter(features[0], features[1], s=200, marker="*", c=self.colors[classification])
        return classification

    def visualize(self) -> None:
        """Plot training points, the decision boundary (dashed) and both margins."""
        # bug fix: use the fitted data, not a module-level global
        [[self.ax.scatter(x[0], x[1], s=100, color=self.colors[i]) for x in self.data[i]] for i in self.data]

        # hyperplane value v = x.w + b  (v = 1: positive SV, -1: negative SV, 0: boundary)
        def hyperplane(x: float, w: np.ndarray, b: float, v: float) -> float:
            return (-w[0] * x - b + v) / w[1]

        datarange = (self.min_feature_value * 0.9, self.max_feature_value * 1.1)
        hyp_x_min = datarange[0]
        hyp_x_max = datarange[1]

        # (w.x+b) = 1 : positive support vector hyperplane
        psv1 = hyperplane(hyp_x_min, self.w, self.b, 1)
        psv2 = hyperplane(hyp_x_max, self.w, self.b, 1)
        self.ax.plot([hyp_x_min, hyp_x_max], [psv1, psv2], "k")

        # (w.x+b) = -1 : negative support vector hyperplane
        nsv1 = hyperplane(hyp_x_min, self.w, self.b, -1)
        nsv2 = hyperplane(hyp_x_max, self.w, self.b, -1)
        self.ax.plot([hyp_x_min, hyp_x_max], [nsv1, nsv2], "k")

        # (w.x+b) = 0 : decision boundary
        db1 = hyperplane(hyp_x_min, self.w, self.b, 0)
        db2 = hyperplane(hyp_x_max, self.w, self.b, 0)
        self.ax.plot([hyp_x_min, hyp_x_max], [db1, db2], "y--")

        self.ax.set_title("Linear SVM from scratch: boundary (dashed) and margins")
        self.ax.set_xlabel("feature 1")
        self.ax.set_ylabel("feature 2")
        if plt.get_backend().lower() == "agg":
            self.fig.savefig("svm_from_scratch.png", dpi=120, bbox_inches="tight")
        else:
            plt.show()


if __name__ == "__main__":
    data_dict: DataDict = {-1: np.array([[1, 7],
                                         [2, 8],
                                         [3, 8], ]),
                           1: np.array([[5, 1],
                                        [6, -1],
                                        [7, 3], ])}

    svm = Support_Vector_Machine()
    svm.fit(data=data_dict)

    predict_us = [[0, 10],
                  [1, 3],
                  [3, 4],
                  [3, 5],
                  [5, 5],
                  [5, 6],
                  [6, -5],
                  [5, 8]]

    for p in predict_us:
        print(p, "->", svm.predict(p))

    svm.visualize()
