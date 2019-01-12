# 
# https://projecteuler.net/problem=109
#
import logging
logger = logging.getLogger('p109')

def update_dict(mydict, k, v):
    if k in mydict:
        mydict[k].add(v)
    else:
        mydict[k] = set([v])

def main(args):

    dart_s = list(range(1,21)) + [25]
    dart_mul = dict(S=1, D=2, T=3)
    bull_eye = 25

    checkout = dict()

    # 1 double checkout
    for d in dart_s:
        myset = "D{:02d}".format(d)
        score = d*2
        update_dict(checkout, score, myset)
    logger.debug(checkout[6])
    
    # 2 dart checkout
    for d2 in dart_s:
        dset = ["D{:02d}".format(d2)]
        for d1 in dart_s:
            for k, v in dart_mul.items():
                if v == 3 and d1 == bull_eye:
                    continue
                myset = ["{}{:02d}".format(k, d1)] + dset
                score = d2*2 + d1*v
                update_dict(checkout, score, " ".join(myset))

    # 3 dart checkout
    for d3 in dart_s:
        dset = ["D{:02d}".format(d3)]
        for d2 in dart_s:
            for k2, v2 in dart_mul.items():
                if v2 == 3 and d2 == bull_eye:
                    continue
                for d1 in dart_s:
                    for k1, v1 in dart_mul.items():
                        if v1 == 3 and d1 == bull_eye:
                            continue
                        myset = ["{}{:02d}".format(k1, d1), "{}{:02d}".format(k2, d2)]
                        myset.sort()
                        myset += dset
                        score = d1*v1 + d2*v2 + d3*2
                        update_dict(checkout, score, " ".join(myset))

    logger.debug(checkout[6])
    logger.debug("distinct ways to checkout on a score of 6: {}".format(len(checkout[6])))

    answer = 0
    tot = 0
    for k, v in checkout.items():
        tot += len(v)
        if k < 100:
            answer += len(v)

    logger.debug("distinct ways to checkout: {}".format(tot))

    logger.info("answer: {}".format(answer))