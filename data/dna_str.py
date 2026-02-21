import random

def shortestDna():
    return ''.join(random.choices(['A', 'C', 'G', 'T'], k=4))

def shortDna():
    return ''.join(random.choices(['A', 'C', 'G', 'T'], k=8))

def longDna():
    return ''.join(random.choices(['A', 'C', 'G', 'T'], k=40))

def longerDna():
    return ''.join(random.choices(['A', 'C', 'G', 'T'], k=100))

def longestDna():
    return ''.join(random.choices(['A', 'C', 'G', 'T'], k=400))  