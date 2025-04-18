import time
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end = time.perf_counter_ns()
        elapsed_ns = end - start
        
        if elapsed_ns < 1_000:
            time_str = f"{elapsed_ns} ns"
        elif elapsed_ns < 1_000_000:
            time_str = f"{elapsed_ns / 1_000:.3f} µs"
        elif elapsed_ns < 1_000_000_000:
            time_str = f"{elapsed_ns / 1_000_000:.3f} ms"
        else:
            time_str = f"{elapsed_ns / 1_000_000_000:.3f} s"
        
        print(f"Performance: {func.__name__}: {time_str}")
        return result
    print("measure-new (util) loaded into global scope.")
    return wrapper
