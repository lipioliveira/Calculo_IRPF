salarioBruto = float(input("Insira o seu salário bruto:")) #Usuário fara a inserção do salário
base = salarioBruto                                       #Salvo o salário informado pelo usuário
imposto = 0                                                #declaro as alíquotas e o imposto
inss1 = 100 - 7.5
inss2 = 100 - 9
inss3 = 100 - 12
inss4 = 100 - 14

#Insiro as condições para cada alíquota
if base <= 1045.00:
    descontaDoInss = (base*inss1)/100
if base > 1045.00:
    descontaDoInss = (base*inss2)/100
if base > 2089.60:
    descontaDoInss = (base*inss3)/100
if base > 3134.40:
    descontaDoInss = (base*inss4)/100

#Calculo dos dependentes
numeroDependentes = int(input("Quantos dependentes você tem?"))
dependentesInseridos = numeroDependentes
descontoPorDependente = 189.59
descontoTotalDependentes = dependentesInseridos*descontoPorDependente

#Resumo de qual a base que devo usar para o cálculo que é o salário bruto descontado o Inss e o valor dos dependentes
baseCalculo = descontaDoInss - descontoTotalDependentes

#As condições para aplicação de cada alíquota do imposto e suas respectivas parcelas a deduzir
if baseCalculo <= 1903.05:
    imposto = 0
if baseCalculo > 1903.05:
    imposto = baseCalculo * (7.5/100) - 142.8
if baseCalculo > 2826.65:
    imposto = baseCalculo * (15/100) - 354.8
if baseCalculo > 3751.06:
    imposto = baseCalculo * (22.5/100) - 636.13
if baseCalculo > 4664.68:
    imposto = baseCalculo * (27.5/100) - 869.36

    #mostra o salário inserido e o imposto a ser pago
print(f"Salário: R${salarioBruto:6.2f} Imposto a pagar: R${imposto:6.2f}")
