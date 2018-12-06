# coding:utf-8

from numpy import log

def calc_aic_im(n_t, n_p, n_all):
    """
        calculate an aic of an independint model.
        Args:
            n_t : the number of True
            n_p : the number of Positive
            n_all : the number of All
            n_elem : the number of Feature Variables
    """

    n_f = n_all - n_t
    n_n = n_all - n_p

    lh = 0
    for n in [n_t,n_f,n_p,n_n]:
        if n == 0:
            continue
        else:
            lh += n * log(n / n_all)
    aic = -2 * lh + 2*2 # degree of freedom = 2
    return aic

def calc_aic_dm(n_tp, n_t, n_p, n_all):
    """
        calculate an aic of a dependint model.
        Args:
            n_tp : the number of TruePositive
            n_t : the number of True
            n_p : the number of Positive
            n_all : the number of All
            n_elem : the number of Feature Variables
    """

    n_fp = n_p - n_tp
    n_tn = n_t - n_tp
    n_fn = n_all - n_t - n_p + n_tp

    lh = 0
    for n in [n_tp, n_fp, n_tn, n_fn]:
        if n == 0:
            continue
        else:
            lh += n * log(n / n_all)
    aic = -2 * lh + 2*3 # degree of freedom = 3
    return aic

def calc_diff_aic(n_tp, n_t, n_p, n_all):
    return calc_aic_dm(n_tp, n_t, n_p, n_all) - calc_aic_im(n_t, n_p, n_all)

if __name__ == '__main__':
    print(calc_aic_dm(353, 657, 519, 927))
    print(calc_aic_im(657, 519, 927))
    print(calc_diff_aic(353, 657, 519, 927))
    # print(calc_diff_aic(0, 100, 100, 1000))
