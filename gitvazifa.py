binary_number = input("Ikkilik sonni kiriting: ")
try:
    decimal_number = int(binary_number, 2)
    print(f"Ikkilik son {binary_number} o'nlikda {decimal_number}")
except ValueError:
    print("Iltimos, faqat 0 va 1 raqamlaridan tashkil topgan to'g'ri ikkilik son kiriting.")
