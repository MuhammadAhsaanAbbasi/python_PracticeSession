from typing import Any
import time

class ExecutionTimer():
    def __init__(self,func):
        self.func = func
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        start = time.perf_counter()
        result = self.func(*args, **kwds)
        end = time.perf_counter()
        print(f"Execution time {(end-start)*1000:.4f} ms")
        return result

class SumValues():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result