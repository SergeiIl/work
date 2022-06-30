import time


def test_time (fn):
    def wrapper (*args, **kwargs):
        st = time.time()
        fn(*args, **kwargs)
        dt = time.time() - st
        print(f"Время работы: {dt} сек")

    return wrapper
