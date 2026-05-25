import struct


def float_to_bits(f: float) -> int:
    return struct.unpack("I", struct.pack("f", f))[0]


def main():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: введено не число.")
        return

    bits1 = float_to_bits(num1)
    bits2 = float_to_bits(num2)

    print("\nБитовое представление (IEEE 754):")
    print(f"Число 1: {bits1:032b} ({num1})")
    print(f"Число 2: {bits2:032b} ({num2})")

    if bits1 == bits2:
        print("Числа идентичны побитово.")
    else:
        print("Числа различаются.")

        diff = bits1 ^ bits2
        print(f"Маска различий: {diff:032b}")

        diff_count = diff.bit_count()

        print(f"Количество несовпадающих бит: {diff_count}")


if __name__ == "__main__":
    main()