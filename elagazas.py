def eldont():
    elsoSzo=input("\tKérek egy szót!: ")
    masodikSzo=input("\tKérek egy másik szót!: ")
    print("I/A.")
    if len(elsoSzo) > len(masodikSzo):
        print(f"\tA hosszabb szó: {elsoSzo}")
    elif len(elsoSzo) < len(masodikSzo):
        print(f"\tA hosszabb szó: {masodikSzo}")
    else:
        print("\tA szavak egyforma hosszúak")

    print("I/D.")
    print(f"\tA szavak hosszának különbsége: {abs(len(elsoSzo)-len(masodikSzo))}")

def egy():
    eldont()