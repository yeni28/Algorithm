def calculate_digit_sum(number):
    sumation = sum(map(int, str(number)))
    while sumation >= 10:
        sumation = sum(map(int, str(sumation)))
    return sumation

while True:
    number = int(input())
    if number == 0:
        break
    else:
        result = calculate_digit_sum(number)
        print(result)