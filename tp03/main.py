import traceback


def f():
    print('avant')
    raise Exception('Erreur')
    print('après')


def main():
    f()

def main01():
    try:
        a=2
        # b=int(input('Valeur de b:'))
        b=2
        c=a/b

        f()

    except ZeroDivisionError as e:
        print("erreur",e)
        traceback.print_exc()
    except TypeError as e:
        print("erreur",e)
        traceback.print_exc()
    except ValueError as e:
        print("erreur",e)
        traceback.print_exc()
    except Exception as e:
        print("erreur",e)
        traceback.print_exc()
    else:
        print("pas d'erreurs !")

    print("Après")

# ZeroDivisionError:UpperCamelCase
# zeroDivisionError:camelCase
# zero_division_error:snake
# zero-division-error:kebab



if __name__=='__main__':
    main()
