def fib_mod(n, m):
    def fib(x):
        fvl0,fvl1,i=0,1,2
        if x==1:
            fvl=1
        else:
            while i<=x:
                fvl=fvl0+fvl1
                fvl0,fvl1=fvl1,fvl
                i+=1
        return fvl

    def fib_digit(x):
        a0,a1,i=0,1,2
        if x==1:
            a2=1
        else:
            while i<=x:
                a2=(a0+a1)%10
                a0,a1=a1,a2
                i+=1
        return a2

    fib_last_digit_list,mod_list,i=[0,1],[0,1],2
    temp_fib_digit=fib_digit(i)
    fib_last_digit_list.append(temp_fib_digit)
    mod_list.append(temp_fib_digit%m)

    while mod_list[:2] != mod_list[-2:]:
        i+=1
        temp_fib_digit=fib(i)
        fib_last_digit_list.append(temp_fib_digit)
        mod_list.append(temp_fib_digit%m)

    Pizanto_period=len(mod_list)-2
    elem_number=n%Pizanto_period
    fibo=fib(elem_number)
    answer=fibo%m

    # return fib_last_digit_list, mod_list, Pizanto_period, elem_number, fibo, answer
    return answer

def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
