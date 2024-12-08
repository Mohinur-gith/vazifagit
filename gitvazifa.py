binary_number = input("Ikkilik sonni kiriting: ")
try:
    decimal_number = int(binary_number, 2)
    hexadecimal_number = hex(decimal_number)[2:].upper()
    print(f"Ikkilik son {binary_number} o'nlikda {decimal_number} va o'n oltilikda {hexadecimal_number}")
except ValueError:
    print("Iltimos, faqat 0 va 1 raqamlaridan tashkil topgan to'g'ri ikkilik son kiriting.")
