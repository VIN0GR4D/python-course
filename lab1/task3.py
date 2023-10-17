BYTES_ONE_CHAR = 4
pages = 100
lines = 50
chars = 25

bytes_for_book = pages * lines * chars * BYTES_ONE_CHAR
total_bytes = 1.44 * 1024 * 1024
books_number = int(total_bytes // bytes_for_book)

print("Количество книг, помещающихся на дискету:", books_number)
