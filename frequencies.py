"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        item = str(item)
        if item in frequencies.keys():
            frequencies[item] = frequencies[item] + 1
        else:
            frequencies[item] = 1;
    return frequencies

print(frequencies(['0', 4,4,'4','d','d','e',0,'a','d','4']))