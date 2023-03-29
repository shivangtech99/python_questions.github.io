n = int(input("ENTER YOUR NUMBER: "))
g = n/2
t = 0.0001


def findRoot(x):
    if ((x*x > n - t) and (x*x <= n + t)):
        return x
    x = (x + n/x)/2
    return findRoot(x)


r = findRoot(g)

print("ROOT OF {} IS {}".format(n, r))
