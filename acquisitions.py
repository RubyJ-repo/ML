import numpy as np
from scipy.stats import norm

# Functional Structure


def probability_improvement(X: np.ndarray, X_sample: np.ndarray,
                            gpr: object, xi: float = 0.01) -> np.ndarray:
    """
    Probability improvement acquisition function.

    Computes the PI at points X based on existing samples X_sample using
    a Gaussian process surrogate model

    Arguments:
    ----------
        X: ndarray of shape (m, d)
            The point for which the expected improvement needs to be computed.

        X_sample: ndarray of shape (n, d)
            Sample locations

        gpr: GPRegressor object.
            Gaussian process trained on previously evaluated hyperparameters.

        xi: float. Default 0.01
            Exploitation-exploration trade-off parameter.

    Returns:
    --------
        PI: ndarray of shape (m,)
    """
    # TODO Q2.4
    # Implement the probability of improvement acquisition function

    # FIXME
    mean, std = gpr.predict(X, return_std = True)
    mean_sample = gpr.predict(X_sample)
    fx_ = np.max(mean_sample)
    Z = (mean - fx_ - xi) / std

    output = norm.cdf(Z).ravel()
    return output


def expected_improvement(X: np.ndarray, X_sample: np.ndarray,
                         gpr: object, xi: float = 0.01) -> np.ndarray:
    """
    Expected improvement acquisition function.

    Computes the EI at points X based on existing samples X_sample using
    a Gaussian process surrogate model

    Arguments:
    ----------
        X: ndarray of shape (m, d)
            The point for which the expected improvement needs to be computed.

        X_sample: ndarray of shape (n, d)
            Sample locations

        gpr: GPRegressor object.
            Gaussian process trained on previously evaluated hyperparameters.

        xi: float. Default 0.01
            Exploitation-exploration trade-off parameter.

    Returns:
    --------
        EI : ndarray of shape (m,)
    """

    # TODO Q2.4
    # Implement the expected improvement acquisition function

    # FIXME
    mean, std = gpr.predict(X, return_std=True)
    mean_sample = gpr.predict(X_sample)
    fx_ = np.max(mean_sample)
    Z = (mean - fx_ - xi) / std

    if np.all(std) == 0:
        return 0
    output = ((mean - fx_ - xi) * norm.cdf(Z) + std * norm.pdf(Z)).ravel()
    return output


