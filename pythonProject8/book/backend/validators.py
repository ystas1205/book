from django.core.exceptions import ValidationError


def validate_isbn(isbn):

    if not isinstance(isbn, str):
        raise ValidationError("ISBN должен быть строкой")
    isbn = isbn.replace("-", "").replace(" ", "")
    if len(isbn) != 13:
        raise ValidationError("ISBN должен состоять из 13 цифр")
    try:
        isbn.isdigit()
    except ValueError:
        raise ValidationError("ISBN должен быть числовой строкой")

    # Проверяем структуру ISBN
    ean_code = isbn[:3]
    publisher_code = isbn[3:4]
    publisher_number = isbn[4:7]
    publication_number = isbn[7:12]
    control_digit = isbn[12]

    # Проверяем корректность EAN кода
    if ean_code not in ["978", "979"]:
        raise ValidationError("Некорректный EAN код")

    # Проверяем корректность номера издателя
    if not publisher_code.isdigit() or not publisher_number.isdigit():
        raise ValidationError("Некорректный номер издателя")

    # Проверяем корректность номера публикации
    if not publication_number.isdigit():
        raise ValidationError("Некорректный номер публикации")

    # Вычисляем контрольную сумму
    sum = 0
    for i, digit in enumerate(isbn):
        digit = int(digit)
        if i % 2 == 0:
            sum += digit
        else:
            sum += digit * 3
    if sum % 10 != 0:
        raise ValidationError("Неправильная контрольная сумма ISBN")