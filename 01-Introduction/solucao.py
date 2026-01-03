def check_weirdness(n):
    if n % 2 != 0:
        return "Weird"
    else:
        if n in range(2, 6):
            return "Not Weird"
        elif n in range(6, 21):
            return "Weird"
        elif n > 20:
            return "Not Weird"

if __name__ == '__main__':
    n = int(input("Digite um número: ").strip())
    result = check_weirdness(n)
    print(result)