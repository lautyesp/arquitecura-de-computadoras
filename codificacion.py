# Binario a Decimal
def binario_a_decimal(binario):
    return int(binario, 2)

# Decimal a Binario
def decimal_a_binario(decimal):
    return bin(decimal)[2:]

# Decimal con fracción a Binario
def decimal_fraccionario_a_binario(numero, precision=10):
    parte_entera = int(numero)
    parte_fraccionaria = numero - parte_entera
    bin_entera = bin(parte_entera)[2:]
    bin_fraccionaria = ""
    while precision > 0 and parte_fraccionaria != 0:
        parte_fraccionaria *= 2
        bit = int(parte_fraccionaria)
        bin_fraccionaria += str(bit)
        parte_fraccionaria -= bit
        precision -= 1
    return f"{bin_entera}.{bin_fraccionaria}"

# Complemento a Uno
def complemento_a_uno(binario):
    return ''.join('1' if b == '0' else '0' for b in binario)

# Complemento a Dos
def complemento_a_dos(binario):
    comp1 = complemento_a_uno(binario)
    comp2 = bin(int(comp1, 2) + 1)[2:]
    return comp2.zfill(len(binario))

# Ejemplos
print("Binario a Decimal:", binario_a_decimal("1011"))           # 11
print("Decimal a Binario:", decimal_a_binario(11))               # '1011'
print("Decimal con fracción a Binario:", decimal_fraccionario_a_binario(10.625))  # '1010.101'
print("Complemento a Uno:", complemento_a_uno("0101"))           # '1010'
print("Complemento a Dos:", complemento_a_dos("0101"))           # '1011'
