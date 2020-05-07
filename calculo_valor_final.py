from calculadora_ir import calcula_inss
from calculadora import enquadramento_aliquota

def calculo_final(salario_bruto):
    salario_base = calcula_inss(salario_bruto)
    aliquota = enquadramento_aliquota(salario_base)
    if(aliquota == 0):
        valor_total = salario_base
    elif(aliquota == 7.5):
        valor_total = (salario_base - 142.80) * 7.5
    elif(aliquota == 15):
        valor_total = (salario_base - 354.80) * 15
    elif(aliquota == 22.5):
        valor_total = (salario_base - 636.13) * 22.5
    elif(aliquota == 27.5):
        valor_total = (salario_base - 869.36) * 27.5
        
    return valor_total
