def calcular_folha(salario_base, anos_servico):
    trienios = anos_servico // 3
    adicional_trienio = salario_base * (0.03 * trienios)
    salario_bruto = salario_base + adicional_trienio

    desconto_inss = salario_bruto * 0.11

    desconto_irrf = (salario_bruto - desconto_inss) * 0.15

    salario_liquido = salario_bruto - desconto_inss - desconto_irrf

    return {
        "bruto": salario_bruto,
        "adicional": adicional_trienio,
        "inss": desconto_inss,
        "irrf": desconto_irrf,
        "liquido": salario_liquido
    }
