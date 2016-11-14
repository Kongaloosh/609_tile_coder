numTilings = 8

def inputs_to_index(in1, in2):

    # print(
    #     """
    #     inputs      {0}, {1}
    #     normalized  {2}, {3}
    #     """.format(in1, in2, (, ))
    return int(in1/6.) + 10 * int(in2 / (6/10.))


def tilecode(in1,in2,tileIndices):
    # write your tilecoder here (5 lines or so)
    # for each of the tilings, return the active feature
    for i in range(numTilings):
        shift = i*(6/10./numTilings)
        tileIndices[i] = inputs_to_index(in1+shift, in2+shift) + (11**2 * i)
    
def printTileCoderIndices(in1,in2):
    tileIndices = [-1]*numTilings
    tilecode(in1,in2,tileIndices)
    print('Tile indices for input (',in1,',',in2,') are : ', tileIndices)

printTileCoderIndices(0.1,0.1)
# printTileCoderIndices(4.0,42.0)
# printTileCoderIndices(5.99,5.99)
# printTileCoderIndices(4.0,2.1)
    
