import time
start = time.time()
def fetch_file():
    print ('starting file fetch')
    time.sleep(1)
    print('file fetch completed')
    
def main():
    print('Starting main')
    fetch_file()
    fetch_file()
    fetch_file
    print('Main completed')
    
main()

end = time.time()
print('Execution time:', (end - start))