import random
def generate_random_numbers(start, end, count=10):
    return[random.randint(start, end) for _ in range(count)]
