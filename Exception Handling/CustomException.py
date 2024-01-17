class Error(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value
        
class HighValueError(Error):
    def print_message(self):
        print(f"{self.message}" + f"{self.value}")
        
class LowValueError(Error):
    def print_message(self):
        print(f"{self.message}" + f"{self.value}")
        
def test_divide(number):
    if 100 >= number >= 50:
        val = "The value recorded is within limits!" + str(number)
        print(val)
    elif number < 50:
        raise LowValueError("The error is due low value! ",number)
    elif number > 100:
        raise HighValueError("The error is due high value!",number)        
        
if __name__ == '__main__':
    try:
        number = int(input("Enter the number..."))
        print(number)
        test_divide(number)
    except HighValueError as e:
        e.print_message()
    except LowValueError as e:
        e.print_message()