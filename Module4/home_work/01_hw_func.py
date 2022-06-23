# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):

    ticket = str(ticket_number)
    number_quantity = len(ticket)

    if number_quantity % 2 == 0:
        mid = int(number_quantity / 2)
        lucky_test = [int(number) for number in ticket]
        if sum(lucky_test[:mid]) == sum(lucky_test[mid:]):
            return True
        else:
            return False
    else:
        mid = int(number_quantity / 2) + 1
        lucky_test = [int(number) for number in ticket]
        if sum(lucky_test[:mid - 1]) == sum(lucky_test[mid:]):
            return True
        else:
            return False
    pass


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
