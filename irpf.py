salariobruto = float(input("Insira o seu salário bruto:")) #Usuário fara a inserção do salário
base = salariobruto                                       #Salvo o salário informado pelo usuário
imposto = 0                                                #declaro as alíquotas e o imposto
inss1 = 100 - 7.5
inss2 = 100 - 9
inss3 = 100 - 12
inss4 = 100 - 14

#Insiro as condições para cada alíquota
if base <= 1045.00:
    descontadoinss = (base*inss1)/100
if base > 1045.00:
    descontadoinss = (base*inss2)/100
if base > 2089.60:
    descontadoinss = (base*inss3)/100
if base > 3134.40:
    descontadoinss = (base*inss4)/100

#Calculo dos dependentes
numerodependentes = int(input("Quantos dependentes você tem?"))
dependentesinseridos = numerodependentes
descontoporpendente = 189.59
descontototaldependentes = dependentesinseridos*descontoporpendente

#Resumo de qual a base que devo usar para o cálculo que é o salário bruto descontado o Inss e o valor dos dependentes
basecalculo = descontadoinss - descontototaldependentes

#As condições para aplicação de cada alíquota do imposto e suas respectivas parcelas a deduzir
if basecalculo <= 1903.05:
    imposto = 0
if basecalculo > 1903.05:
    imposto = basecalculo * (7.5/100) - 142.8
if basecalculo > 2826.65:
    imposto = basecalculo * (15/100) - 354.8
if basecalculo > 3751.06:
    imposto = basecalculo * (22.5/100) - 636.13
if basecalculo > 4664.68:
    imposto = basecalculo * (27.5/100) - 869.36

    #mostra o salário inserido e o imposto a ser pago
print(f"Salário: R${salariobruto:6.2f} Imposto a pagar: R${imposto:6.2f}")
