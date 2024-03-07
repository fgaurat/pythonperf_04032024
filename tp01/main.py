# import lemodule

def main():
    to_find = 41
    is_found=False
    for i in range(10):
        print(i)
        if i==to_find:
            is_found=True
            break
    else:
        print("not found")
    
    print("ok" if is_found else "ko") # is_found?"ok":"ko"


if __name__=='__main__':
    main()
