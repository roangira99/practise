import time

# recursive countdown timer
def recur_countdown_timer(n):
    if n == 0: # when base case is reached (base case is 0) return it
        return n
    else:
        print(n)
        time.sleep(1) # delay of 1 second in displaying the countdown
        return recur_countdown_timer(n-1) # recursive call of the function, which will reduce the value of n by 1

# The iterative countdown timer below could be an alternative to the recursive countdown timer
def iter_countdown_timer(n):
    while n > 0:
        print(n)
        time.sleep(1) 
        n -= 1
    print(n)

z = 5 
print(f"Counting down from {z}:")
# iter_countdown_timer(z)
print(recur_countdown_timer(z))