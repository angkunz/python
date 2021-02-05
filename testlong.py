def sum_phone(phone_number) :
    total = 0
    for x in phone_number :
        total += int(x)
        return total

print(sum_phone('123'))