# 1. 
import time

# Should take ~4 seconds
start = time.time()

def get_movie_tickets():
    time.sleep(3)
    print('tickets secured')
    
def like_ig():
    time.sleep(1)
    print('Pic liked')
    
def main():
    get_movie_tickets()
    like_ig()

main()

end = time.time()
print('Execution time', end - start)  
