Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
    #####O(1) - no matter the buffer size, we don't add any more operations

2. What is the space complexity of your ring buffer's `append` function?
    #####O(1) - no new data structures are allocated
    
3. What is the runtime complexity of your ring buffer's `get` method?
    #####O(n) - function only loops once

4. What is the space complexity of your ring buffer's `get` method?
    #####O(1) - we copy the array using list comprehension before returning it

5. What is the runtime complexity of the provided code in `names.py`?
    #####O(n^2) - because of nested loops, both of them are n

6. What is the space complexity of the provided code in `names.py`?
    #####O(n)

7. What is the runtime complexity of your optimized code in `names.py`?
    #####O(n)

8. What is the space complexity of your optimized code in `names.py`?
    ##### O(n), using dictionary and list