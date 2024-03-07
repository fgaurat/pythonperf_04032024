def make_incrementor(init_value):

    def inc(value):
        return init_value+value

    def mult(value):
        return init_value*value

    return f,mult


def main():
    do_inc,do_mult = make_incrementor(10)
    i = do_inc(2)
    print(i) # 12
if __name__=='__main__':
    main()
