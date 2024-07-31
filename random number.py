import random_generator

def main():
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        if start >end:
            raise ValueError('start range must be less than end range')

        random_numbers = random_generator.generate_random_numbers(start,end)
        print(f"list of random numbers : {random_numbers}")
    except ValueError as e:
        print(f"invalid input :{e}")

if __name__ == "__main__":

    main()