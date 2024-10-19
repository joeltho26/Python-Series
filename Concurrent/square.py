from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed
values = [2,3,4,5]
def square(n):
   return n * n
def main():
   with ProcessPoolExecutor(max_workers = 3) as executor:
      results = executor.map(square, values)
   for result in results:
      print(result)
if __name__ == '__main__':
   main()