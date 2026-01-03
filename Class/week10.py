def one():
    try:
        x = int(input("Give me a number: "))
        print(x)
    except:
        print("Not a number")
    finally:
        print("Life is beautiful")

def practice1():
    try:
        myfile = open("numbers.txt", "r")
        numberslist = myfile.readlines()
        total = 0
        for num in numberslist:
            total += int(num.strip())
    except IOError:
        print("File is not there.")
    except ValueError:
        print("You need to have an integer.")
    finally:
        print(total)

def practice2():
    import random
    number = random.randint(1, 100)
    while True:
        try:
            guess = int(input("enter a number from 1 to 100: "))
            if guess > 100 or guess < 0:
                raise Exception("outside of range")
            if guess == number:
                print("You are correct!")
                break
            elif guess < number:
                print("guess higher")
            else:
                print("guess lower")
        except:
            print("not a valid guess")
practice2()