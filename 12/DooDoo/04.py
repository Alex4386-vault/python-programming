for i in range(0,3):
    try:
        result = 10 // i
        print(result, "------", i)
    except ZeroDivisionError as e:
        print("Can't divide by zero")
        print(e)
    finally:
        print("end")