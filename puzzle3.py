import numpy as np

def key_rotation(key, direction):
    """
    Takes a list (key) and the direction the key is facing and rotates it 90
    degrees clockwise with the new direction
    """
    directions = ['N', 'E', 'S', 'W', 'N']
    r = np.array(key)  # converts to array so can be rotated in numpy
    key1 = np.rot90(r, 3)
    direction1 = directions[directions.index(direction) + 1]
    return key1, direction1


def key_fitcheck(key, stone, y, x):
    """
    Takes two lists (key, stone) and the x and y coordinates of how far the key
    has shifted on the stone, and checks if key fits the stone
    """
    # Checks if key is bigger than stone or moved off edges
    if len(key[0]) + x > len(stone[0]) or len(stone) < len(key) + y:
        return False
    
    # Checks if all key's raised parts fit in the stone's holes
    for j in range(len(key)):  # vertical length
        for i in range(len(key[0])):  # horizontal length
            if key[j][i] == '*' and stone[j + y][i + x] == '#':
                return False
    return True


def third_lock(key, stone):
    """
    Takes two lists (key and stone) and determines the top most, left most 
    and least rotated possible position of the key so that it fits on the
    given stone and returns None if not possible
    """
    x, y = 0, 0  # coordinates on stones to shift the key by
    direction = 'N'  # default beginning direction of key
    
    # Keep shifting and rotating key to fit stone until the key moves off edge
    # as off the edge in one rotation may not true for other orientation
    while y< len(stone)+ len(key):        
        # Check if the key fits 
        for num in range(0, 4):
            if key_fitcheck(key, stone, y, x):
                return y, x, direction
            # Rotate the key to check again
            else:
                key, direction = key_rotation(key, direction)
                
        # Shifts the key if no rotations work on that position of the stone
        if x < len(stone[0]) + len(key[0]):
            x += 1
        else:
            x = 0
            y += 1
