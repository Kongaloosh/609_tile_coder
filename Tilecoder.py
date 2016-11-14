numTilings = 8

def inputs_to_index(in1, in2):
    return (in1/6.) + (10* (in2/6.))


def tilecode(in1,in2,tileIndices):
    # write your tilecoder here (5 lines or so)
    # for each of the tilings, return the active feature
    for i in range(numTilings):
        shift = i*(numTilings/6.)
        print(11**2 * i)
        tileIndices[i] = inputs_to_index(in1+shift, in2+shift) + (11**2 * i)
    
def printTileCoderIndices(in1,in2):
    tileIndices = [-1]*numTilings
    tilecode(in1,in2,tileIndices)
    print('Tile indices for input (',in1,',',in2,') are : ', tileIndices)

printTileCoderIndices(0.1,0.1)
# printTileCoderIndices(4.0,42.0)
# printTileCoderIndices(5.99,5.99)
# printTileCoderIndices(4.0,2.1)
    
