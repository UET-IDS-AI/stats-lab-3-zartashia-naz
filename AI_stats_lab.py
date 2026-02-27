"""
Prob and Stats Lab – Discrete Probability Distributions

Follow the instructions in each function carefully.
DO NOT change function names.
Use random_state=42 where required.
"""

import numpy as np
import math


# =========================================================
# QUESTION 1 – Card Experiment
# =========================================================

def card_experiment():
    
    total = 52
    aces = 4

    P_A = aces / total
    P_B = aces / total
    P_B_given_A = (aces - 1) / (total - 1)
    P_AB = P_A * P_B_given_A

    np.random.seed(42)
    deck = np.arange(52)
    ace_set = {0, 1, 2, 3}

    N = 200000
    count_A = 0
    count_AB = 0

    for _ in range(N):
        draw = np.random.choice(deck, 2, replace=False)
        A = draw[0] in ace_set
        B = draw[1] in ace_set

        if A:
            count_A += 1
            if B:
                count_AB += 1

    empirical_P_A = count_A / N
    empirical_P_B_given_A = count_AB / count_A

    absolute_error = abs(empirical_P_B_given_A - P_B_given_A)

    return (
        P_A,
        P_B,
        P_B_given_A,
        P_AB,
        empirical_P_A,
        empirical_P_B_given_A,
        absolute_error
    )


# =========================================================
# QUESTION 2 – Bernoulli
# =========================================================

def bernoulli_lightbulb(p=0.05):
    
    theoretical_P_X_1 = p
    theoretical_P_X_0 = 1 - p

    np.random.seed(42)
    samples = np.random.binomial(1, p, 100000)
    empirical_P_X_1 = np.mean(samples)

    absolute_error = abs(empirical_P_X_1 - theoretical_P_X_1)

    return (
        theoretical_P_X_1,
        theoretical_P_X_0,
        empirical_P_X_1,
        absolute_error
    )


# =========================================================
# QUESTION 3 – Binomial
# =========================================================

def binomial_bulbs(n=10, p=0.05):
    
    theoretical_P_0 = (1 - p) ** n

    theoretical_P_2 = (
        math.comb(n, 2)
        * (p ** 2)
        * ((1 - p) ** (n - 2))
    )

    theoretical_P_ge_1 = 1 - theoretical_P_0

    np.random.seed(42)
    samples = np.random.binomial(n, p, 100000)
    empirical_P_ge_1 = np.mean(samples >= 1)

    absolute_error = abs(empirical_P_ge_1 - theoretical_P_ge_1)

    return (
        theoretical_P_0,
        theoretical_P_2,
        theoretical_P_ge_1,
        empirical_P_ge_1,
        absolute_error
    )



# =========================================================
# QUESTION 4 – Geometric
# =========================================================

def geometric_die():

    p = 1 / 6

    theoretical_P_1 = p
    theoretical_P_3 = ((1 - p) ** 2) * p
    theoretical_P_gt_4 = (1 - p) ** 4

    np.random.seed(42)
    samples = np.random.geometric(p, 200000)
    empirical_P_gt_4 = np.mean(samples > 4)

    absolute_error = abs(empirical_P_gt_4 - theoretical_P_gt_4)

    return (
        theoretical_P_1,
        theoretical_P_3,
        theoretical_P_gt_4,
        empirical_P_gt_4,
        absolute_error
    )




# =========================================================
# QUESTION 5 – Poisson
# =========================================================

def poisson_customers(lam=12):

    theoretical_P_0 = math.exp(-lam)

    theoretical_P_15 = (
        math.exp(-lam)
        * (lam ** 15)
        / math.factorial(15)
    )

    theoretical_P_ge_18 = 1 - sum(
        math.exp(-lam)
        * (lam ** k)
        / math.factorial(k)
        for k in range(18)
    )
    
    np.random.seed(42)
    samples = np.random.poisson(lam, 100000)
    empirical_P_ge_18 = np.mean(samples >= 18)

    absolute_error = abs(empirical_P_ge_18 - theoretical_P_ge_18)

    return (
        theoretical_P_0,
        theoretical_P_15,
        theoretical_P_ge_18,
        empirical_P_ge_18,
        absolute_error
    )
