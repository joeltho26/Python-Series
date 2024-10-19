import multiprocessing

# technique to start the child process in Python (Fork/Spawn/Forkserver)
print(multiprocessing.get_start_method())

# OS Platforms and default start methods
# Windows : spawn
# macOS : spawn
# Linux : Fork

print(multiprocessing.get_all_start_methods())
print(multiprocessing.get_context())