# Cuboid layers
# Problem 126

# https://projecteuler.net/problem=126

import logging
logger = logging.getLogger('p126')

def CuboidLayers(dim, layer):
    # Input:
    #   dim: the start dimention
    #   layer: the layer number
    x, y, z = dim
    if layer == 1:
        return (x*y+y*z+z*x)*2
    else:
        return (x*y+y*z+z*x)*2+(x+y+z)*(layer-1)*4+(layer-2)*(layer-1)*4

def main(args):

    Cn = {}

    if args.test:
        cnt = 10
        max_dim =200
        for l in range(1,5):
            logger.debug("3x2x1 layer {}: {}".format(l, CuboidLayers((3,2,1), l)))

        logger.debug("5x1x1 layer 1: {}".format(CuboidLayers((5,1,1), 1)))
        logger.debug("5x3x1 layer 1: {}".format(CuboidLayers((5,3,1), 1)))
        logger.debug("7x2x1 layer 1: {}".format(CuboidLayers((7,2,1), 1)))
        logger.debug("11x1x1 layer 1: {}".format(CuboidLayers((11,1,1), 1)))
    else:
        cnt = 1000
        max_dim = cnt*50

    
    for x in range(1, max_dim//2):
        for y in range(1, x+1):
            if x*y > max_dim:
                break
            for z in range(1, y+1):
                for l in range(1, max_dim):
                    mycn = CuboidLayers((x,y,z), l)
                    if mycn > max_dim:
                        break
                    if mycn in Cn:
                        Cn[mycn] += 1
                    else:
                        Cn[mycn] = 1

    for n in [22, 46, 78, 118, 154]:
        logger.debug("C({})={}".format(n, Cn[n]))    

    for n in sorted(list(Cn.keys())):
        if Cn[n] == cnt:
            answer = n
            break

    logger.info("answer: {}".format(answer))
