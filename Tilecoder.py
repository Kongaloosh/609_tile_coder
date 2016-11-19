numTilings = 8

def inputs_to_index(in1, in2):

    # print(
    #     """
    #     inputs      {0}, {1}
    #     normalized  {2}, {3}
    #     values      {4}, {5}
    #     returned    {6}
    #     """.format(in1, in2, (in1/ (6./10)), 11 * (in2 / (6/10.)), int(in1/ (6./10)), 11 * int(in2 / (6/10.)), int( in2 / (6/10.)) + int(in1/ (6./10)) + 11 * int( in2 / (6/10.))))
    return int(in1/ (6./10)) + 11 * int( in2 / (6/10.))


def tilecode(in1,in2,tileIndices):
    # write your tilecoder here (5 lines or so)
    # for each of the tilings, return the active feature
    for i in range(numTilings):
        # shift = i*(6/10./numTilings)
        shift = i*(0.6/numTilings)
        tileIndices[i] = inputs_to_index(in1+shift, in2+shift) + (11**2 * i)
    return tileIndices

def printTileCoderIndices(in1, in2):
    tileIndices = [-1] * numTilings
    tilecode(in1, in2, tileIndices)
    print('Tile indices for input (', in1, ',', in2,') are : ', tileIndices)

printTileCoderIndices(0.1, 0.1)
printTileCoderIndices(4.0, 2.0)
printTileCoderIndices(5.99, 5.99)
printTileCoderIndices(4.0, 2.1)

