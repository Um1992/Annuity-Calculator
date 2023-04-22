while True:
    try:
        x = int(input("Hello, are you want to calculate:\n"
          "1-) What your future value will be\n"
          "2-) What should you pay for your goal future value?\n"))
        if x==1 or x==2:
            break
    except ValueError:
        print("Please write number")
        continue


if x==1:
    a = int(input("Please wrote what will you invest monthly:\n"))
    i = (float(input("Please wrote yearly interest rate:\n")) / 100)
    n = int(input("Please wrote how many year you would invest:\n"))
    S = a * (((1+i/12)**(n*12)-1)/(i/12))
    print("After "+str(n)+ " year payment, your invesment will be " +str(round(S,2)) +" units")
elif x==2:
    S = int(input("Please wrote what is your goal investment amount?\n"))
    i = (float(input("Please wrote yearly interest rate:\n")) / 100)
    n = int(input("Please wrote how many year you would invest:\n"))
    a = S / (((1+i/12)**(n*12)-1)/(i/12))
    print("You need to pay "+str(a)+" monthly for your goal.")
