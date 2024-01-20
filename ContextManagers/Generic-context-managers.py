class ManagedFile:
    def __init__(self, filename):
        print('init', filename)
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('Exception has been handled')
        print('exit')
        return True

with ManagedFile('./ContextManagers/notes.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
print('continuing...')

with ManagedFile('./ContextManagers/notes2.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
    f.do_something()
print('continuing...')