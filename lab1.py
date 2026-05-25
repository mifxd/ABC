
def main():
    bin_num = bin(int(input("Введите число: ")))[2:]

    print(f'Число{" не " if bin_num != bin_num[::-1] else " "}является палиндромом')

if __name__ == "__main__":
    main()