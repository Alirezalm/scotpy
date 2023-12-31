from typing import List

from sklearn.datasets import make_classification

from scotpy.scotpy import (AlgorithmType,
                           ProblemType,
                           ScotModel,
                           ScotPy,
                           ScotSettings
                           )


def main():
    total_nodes = 4
    models: List[ScotModel] = []

    for rank in range(total_nodes):
        dataset, res = make_classification(
            n_samples=1000, n_features=50, n_redundant=0, n_repeated=0)
        scp = ScotModel(problem_name="logistic_regression", rank=rank,
                        kappa=5, ptype=ProblemType.CLASSIFICATION)
        scp.set_data(dataset, res, normalized_data=True)
        scp.create()
        models.append(scp)

    scot_settings = ScotSettings(
        relative_gap=1e-5,
        time_limit=10000,
        verbose=True,
        algorithm=AlgorithmType.DIPOA,
        ub=1e2
    )

    solver = ScotPy(models, scot_settings)
    objval, solution, execution_time = solver.run()
    print(f"Optimal Objective Value: {objval}")
    print(f"Optimal Solution: {solution}")
    print(f"Execution Time: {execution_time} seconds")


if __name__ == '__main__':
    main()
