def f(x):
    import math
    return 200*math.e**(math.log(0.5)/14.1 * x)

def radiationExposure(start, stop, step):

    # base case
    if abs(stop - start - step) < .001:
        return f(start) * step
    # recursive step
    else:
        return (radiationExposure(start, stop - step, step) + f(stop - step) * step)

print radiationExposure(72, 96, 0.4)