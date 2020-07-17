from time import time


def timing(f):
    def wrap(*args, **kwargs):
        start = time()
        ret = f(*args, **kwargs)
        end = time()
        print("{:s} function took {:.3f} ms".format(f.__name__, (end - start) * 1000.0))

        return ret

    return wrap
