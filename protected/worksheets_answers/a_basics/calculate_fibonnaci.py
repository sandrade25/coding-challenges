


"""
given n,
find the corresponding fibonnaci number
dont use recersive method
"""

def fibonnaci(n):
    nacis = [0,1]
    for i in range(2,n+1):
        nacis.append(nacis[-1] + nacis[-2])

    return nacis[n]
    
