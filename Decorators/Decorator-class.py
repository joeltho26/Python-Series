class Decorator:
    def decorator(func):
        def wrapper(*args,**kwargs):
            print("Initializing...!")
            result = func(*args,**kwargs)
            print("Terminating...!")
            return result
        return wrapper

@Decorator.decorator
def print_name(name):
    print(f"Hello! My name is {name}")

if __name__ == '__main__':
    print_name('Alex')