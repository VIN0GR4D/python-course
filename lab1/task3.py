total_bytes = 1.44 * 1024 * 1024
bytes_for_book = 4 * 25 * 50 * 100

books_number = round(total_bytes / bytes_for_book)

print("Количество книг, помещающихся на дискету:", books_number)
