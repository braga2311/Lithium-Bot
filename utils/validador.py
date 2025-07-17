def validar_cpf(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    for i in range(9, 11):
        valor = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
        digito = ((valor * 10) % 11) % 10
        if digito != int(cpf[i]):
            return False
    return True
  
