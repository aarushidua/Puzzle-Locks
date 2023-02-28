def first_lock(gems):
    """
    Takes a list of gems and returns a sorted list of most common gems 
    in the list to determine what buttons to press
    """
    prevcount = 0
    buttonlst = []  # most common buttons will be added to this list
    for gem in gems:
        
        # First we test if the frequency of new gem is higher than prev ones
        # The list will be cleared to add highest frequency gems
        
        if gems.count(gem)>prevcount:
            prevcount = gems.count(gem)
            buttonlst = []
            buttonlst.append(gem)
            
        # We also add any new gems with the same freq (highest) to the list
        
        elif gems.count(gem)==prevcount:
            if gem not in buttonlst:
                buttonlst.append(gem)
                
    return sorted(buttonlst)
