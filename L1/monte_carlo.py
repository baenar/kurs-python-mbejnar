import random as rdm

def monte_carlo(n : int):
    hits = 0
    for i in range(n):
        x, y = rdm.random(), rdm.random()
        if ((x**2 + y**2)**(1/2) <= 1):
            hits += 1
    return 4 * hits / n

N = 1000000
print(monte_carlo(N))
