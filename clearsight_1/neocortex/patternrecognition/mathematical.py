import math
import collections

def counterCosineSimilarity(l1, l2):
    c1 = collections.Counter(l1)
    c2 = collections.Counter(l2)

    # Get all the terms
    terms = set(c1).union(c2)

    # Compute dot product
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)

    # Compute magnitudes
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))

    # Return the dot product divided by the product of the magnitudes.
    return dotprod / (magA * magB)
