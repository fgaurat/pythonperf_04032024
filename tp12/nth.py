import cProfile
import pstats

def is_prime(num):
    """
    is_prime
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def nth_prime(n):
    """
    nth_prime
    """
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1    

def main():
    # v = nth_prime(1000)
    # print(v)
    # cProfile.run('nth_prime(1000)')
    # cProfile.run('nth_prime(1000)',"nth_prim.pstat")
    
    stats = pstats.Stats("nth_prim.pstat")
    # print(stats.print_stats())
    stats.sort_stats(pstats.SortKey.TIME).print_stats(3)


if __name__ == '__main__':
    main()
    