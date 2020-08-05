# Your code here

cache = {}

def expensive_seq(x, y, z):
    # Your code here

    # base case
    if x <= 0:
        return y + z

    if x not in cache:
        # store in cache
        cache[x] = {'1': expensive_seq(x-1,y+1,z), '2': expensive_seq(x-2,y+2,z*2), '3': expensive_seq(x-3,y+3,z*3)}

    print(cache[x], ' is cache of x')
    return cache[x]['1'] + cache[x]['2']+ cache[x]['3']

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
