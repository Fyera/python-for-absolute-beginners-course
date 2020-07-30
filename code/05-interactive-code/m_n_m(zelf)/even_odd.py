u_num_text = input("Gelieve een geheel getal in te geven[0 to cancel]: ")
u_num = int(u_num_text)

while u_num != 0:

    if u_num % 2 == 0:
        print(f"{u_num} is een even getal!")

    elif u_num % 2 > 0:
        print(f"{u_num} is geen geheel getal")

    u_num_text = input("Gelieve een geheel getal in te geven: ")
    u_num = int(u_num_text)

print("Einde programma")
