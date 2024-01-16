import functools
class Decorator:
    def repeat(num_times):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kwargs):
                print("Initializing...!")
                for _ in range(num_times):
                    result = func(*args,**kwargs)
                print("Terminating...!")
                return result
            return wrapper
        return decorator
        
@Decorator.repeat(num_times=5)
def print_name(name):
    print(f"Hello! My name is {name}")

if __name__ == '__main__':
    print_name('Alex')