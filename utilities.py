def combinations(items, n):
    
    sequences = ['']
    
    for i in range(n):
        
        newseqs = []
        
        for seq in sequences:
            
            for it in items:
                
                newseqs.append(seq + it)
                
        sequences = newseqs.copy()
        
    return sequences