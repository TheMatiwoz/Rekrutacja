def postcodes_generator(first, second):
    try:
        first_int = int(first.replace("-", ""))  # create five-digit number
        second_int = int(second.replace("-", ""))
        postcodes = []
        for codes in range(min(first_int, second_int)+1, max(first_int, second_int)):
            postcodes.append("-".join([str(codes)[:2], str(codes)[2:]]))
        return postcodes
    except ValueError:
        return "Wrong Value!"


print(postcodes_generator("79-900", "80-155"))


def missing_elements(numbers_list, max_range):
    try:
        # wersja jednolinijkowa - dluzszy czas dzialania
        # return [number for number in range(1, max_range+1) if number not in numbers_list]

        #wersja bardziej rozbudowana - optymalniejsze rozwiazanie
        range_set = set(range(1, max_range+1))
        numbers_set = set(numbers_list)
        return list(range_set - numbers_set)
    except ValueError:
        return "Wrong Value!"


print(missing_elements([1, 2, 5, 6, 7], 10))


from decimal import *


def decimal_numbers():
    try:
        decimals = []
        for natural in range(2, 6):
            decimals.append(Decimal(natural))
            decimals.append(Decimal(natural) + Decimal(0.5))
        return decimals
    except Exception as e:
        print(e)


print(decimal_numbers())
