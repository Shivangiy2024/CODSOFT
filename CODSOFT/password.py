import random
import string
def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_charactor = lowercase+uppercase+digits+symbols

    password = ''.join(random.choice(all_charactor) for _ in range(length))

    return password
def main():
    print("Password Generator ")
    while True:
        try:
            length = int(input("enter the length of the passward you want to generate: "))
            if length <=0:
                print("Please enter a position integer.")
            else:
                break
        except ValueError:
            print("Please enter a volid integer.")
    password = generate_password(length)
    print(f"Generated password: {password}")

if _name=="main_":
    main()