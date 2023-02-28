def second_lock(gems):
    """
   Takes a list of gems(numbers) and checks if they can be moved to destination
   in ascending order by storing numbers that are not to be moved next. If True
   also returns the largest amount of numbers stored in the store at any time
    """
    store, destination = [], []
    slen = len(store)
    
    
    for gem in reversed(gems):
        # if the gem is the smallest then move to destination otherwise store
        if store == []:  # to avoid index error later if store empty
            if gem == min(gems):
                destination.append(gems.pop())
            else:
                store.append(gems.pop())
                
        # if the gem is now the smallest in store and source then move to 
        # destination
        elif (gem<store[-1]) and (gem == min(gems)):
            destination.append(gems.pop())
            
        # if the last gem in store is the smallest including source then 
        # move to destination
        elif store[-1]<gem and store[-1] < min(gems):
            destination.append(store.pop())
        else:
            store.append(gems.pop())
            
        # ensures the largest store length stays assigned to slen
        if len(store)>slen:
            slen = len(store)
            
    # move gems from store to destination if greater than gem in destination
    if len(store) != 0:
        for num in reversed(store):
            if num>destination[-1]:
                destination.append(store.pop())
                
    # if store cannot be emptied then unsolvable otherwise return slen as well
    if len(store) == 0:
        return tuple([True, slen])
    else:
        return tuple([False, -1])
