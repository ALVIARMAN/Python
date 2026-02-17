class NumberOutOfRange(Exception):
    pass

def start_code():
    try:
        n = int(input("Enter a number (0-50): "))
    finally:
        pass
    try:
        # user defined exception
        if n < 0 or n > 50:
            raise NumberOutOfRange("Number must be between 0 and 50")

        d = 50 / n
        print("Result:", d)

    except ZeroDivisionError:
        print("Division Error (Cannot divide by zero)")

    except NumberOutOfRange as e:
        print("Custom Error:", e)

    finally:
        print("Always run")


if __name__ == "__main__":
    start_code()