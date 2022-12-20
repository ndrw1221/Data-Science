import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


def simple_linear_regression_fit(
    x_train: np.ndarray, y_train: np.ndarray
) -> np.ndarray:
    """
    Inputs:
    x_train: a (num observations by 1) array holding the values of the predictor variable
    y_train: a (num observations by 1) array holding the values of the response variable

    Returns:
    beta_vals:  a (num_features by 1) array holding the intercept and slope coeficients
    """
    x_train_avg = np.average(x_train)
    y_train_avg = np.average(y_train)
    # numerator = 0
    # denominator = 0

    # for i, x in enumerate(x_train):
    #     numerator += (x[0] - x_train_avg) * (y_train[i] - y_train_avg)
    #     denominator += (x[0] - x_train_avg) ** 2

    beta_1 = np.sum((x_train - x_train_avg) * (y_train - y_train_avg)) / np.sum(
        (x_train - x_train_avg) ** 2
    )
    beta_0 = y_train_avg - beta_1 * x_train_avg

    return np.array([beta_0, beta_1])


def main():
    # 1. (1)
    x_train = np.array([1, 2, 3])
    y_train = np.array([2, 2, 4])

    # 1. (2)
    x_train_plus_one = np.expand_dims(x_train, axis=1)
    print("1. 2)")
    print("Size of x_train: " + str(x_train_plus_one.shape))
    print("Size of y_train: " + str(y_train.shape))

    # 1. (3)
    plt.scatter(x_train, y_train)
    plt.savefig("./Lab09_b - 1-1.png", dpi=400)
    plt.show()

    # 2. (2)
    [beta_0, beta_1] = simple_linear_regression_fit(x_train, y_train)
    print("2. 2)")
    print(f"[beta_0, beta_1]: [{beta_0}, {beta_1}]")

    # 2. (3)
    x = np.linspace(1, 3, 1000)
    y = beta_0 + beta_1 * x
    plt.plot(x, y)
    plt.scatter(x_train, y_train)
    plt.savefig("./Lab09_b - 2-3.png", dpi=400)
    plt.show()

    # 3. (1)
    reg = linear_model.LinearRegression()
    reg.fit(x_train_plus_one, y_train)
    beta_0_sklearn, beta_1_sklearn = reg.intercept_, reg.coef_
    print("3. 1)")
    print(f"[beta_0, beta_1]: [{beta_0_sklearn}, {beta_1_sklearn}]")

    # 3. (2)
    # Yes.

    # 3. (3)
    y_sklearn = beta_0_sklearn + beta_1_sklearn * x
    plt.plot(x, y)
    plt.plot(x, y_sklearn)
    plt.scatter(x_train, y_train)
    plt.savefig("./Lab09_b - 3-3.png", dpi=400)
    plt.show()


if __name__ == "__main__":
    main()
