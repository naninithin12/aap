def is_beautiful_number(number):
    str_num = str(number)
    half_length = len(str_num) // 2
    first_half = list(map(int, str_num[:half_length]))
    second_half = list(map(int, str_num[half_length:]))

    return sum(first_half) == sum(second_half)

def find_beautiful_numbers_in_interval(start, end):
    beautiful_numbers = []
    for num in range(start, end + 1):
        if is_beautiful_number(num):
            beautiful_numbers.append(num)
    return beautiful_numbers

# Example interval
start_range = 1000
end_range = 1500

beautiful_nums = find_beautiful_numbers_in_interval(start_range, end_range)
print(f"Beautiful numbers between {start_range} and {end_range}:")
print(beautiful_nums)
