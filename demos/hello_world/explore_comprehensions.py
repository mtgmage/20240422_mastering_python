la_nums = range(0, 10)

la_double_nums_bad = []
for ln_num in la_nums:
    if ln_num % 2 == 0:
        la_double_nums_bad.append(ln_num * 2)

la_double_nums_good = [ln_num * 2 for ln_num in la_nums]
la_double_even_nums_good = [ln_num * 2 for ln_num in la_nums if ln_num % 2 == 0]

print(la_nums)
print(la_double_nums_bad)
print(la_double_nums_good)
print(la_double_even_nums_good)

# -- Dictionary comprehension
currencies = [("bitcoins", "BTC"), ("litecoin", "LTC"), ("etherium", "ETH")]
currencies_dict = {name: symbol for name, symbol in currencies}
print(currencies_dict)

# -- Set comprehension
nums = [1, 2, 1, 1, 3, 4]
print(nums)
num_set = {num for num in nums}
print(num_set)

# -- Generator comprehension
nums = list(range(0, 10))
double_nums = (num * 2 for num in nums)
print(double_nums)
for ln_num in double_nums:
    print(ln_num)
