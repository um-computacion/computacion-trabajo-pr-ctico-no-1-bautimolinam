def decimal_to_roman(number):
    if not 1 <= number <= 3999:
        raise ValueError("El número debe estar entre 1 y 3999")

    roman_numerals = [
        (1000, 'M'), (900, 'CM'),
        (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'),
        (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'),
        (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = ""
    for value, numeral in roman_numerals:
        while number >= value:
            result += numeral
            number -= value

    return result