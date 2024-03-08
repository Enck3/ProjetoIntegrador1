
print("\n\n===================================\n")
print("<<<<<<<< CADASTRO DE PRODUTO >>>>>>>>>>")
print("\n\n===================================\n")

# INPUT DE INFORMAÇÕES

Cod_Prod = int(input("CODIGO: "))            # receber o código do produto
Nome_Prod = input("NOME: ")                  # receber o nome do produto
Desc_Prod = input("DESCRIÇÃO: ")             #receber a descrição do produto
CP = float(input("CUSTO DE AQUISIÇÃO: "))    # receber custo do produto em reais
CF = float(input("CUSTO FIXO: "))            # receber custo fixo em porcentagem
CV = float(input("COMISSÃO DE VENDAS: "))    # receber comissao de venda em porcentagem
IV = float(input("IMPOSTO (SOBRE VENDA): ")) # receber imposto em porcentagem
ML = float(input("MARGEM DE LUCRO: "))       # receber a margem de lucro em porcentagem

# CÁLCULOS NECESSÁRIOS

PV = CP / (1 - ((CF + CV + IV + ML)/100))        # cálculo do preço de venda
Perc_CP = (100*CP)/PV                            # cálculo percentual do custo de aquisição
Rec_Bruta = PV-CP                                # calculo da receita bruta 
Perc_Rec_Bruta = (100*Rec_Bruta)/PV              # calculo do percentaul da receita bruta
Valor_CF = (PV*CF)/100                           # calculo do valor de custo fixo
Valor_CV = (PV*CV)/100                           # calculo do valor de comissão de venda
Valor_IV = (PV*IV)/100                           # calculo do valor de imposto sobre venda
Outros_Custos = Valor_CF + Valor_CV + Valor_IV   # calculo do valor de outros custos
Perc_Outros_Custos = (100*Outros_Custos)/PV      #calculo do percental de outros custos
Rent = Rec_Bruta - Outros_Custos                 #calculo do valor de rentabilidade
Perc_Rent = Perc_Rec_Bruta - Perc_Outros_Custos  # calculp do percentual de rentabilidade


# DEVOLUÇÃO DAS INFORMAÇÕES

print("\n\n==============================================\n")
print("PREÇO DE VENDA:     ", format(PV, "5.2f"), "      100%")
print("CUSTO DE AQUISIÇÃO: ", format(CP, "5.2f"), "      ", Perc_CP, "%")
print("RECEITA BRUTA:      ", format(Rec_Bruta, "5.2f"), "      ", Perc_Rec_Bruta, "%")
print("CUSTO FIXO:         ", format(Valor_CF, "5.2f"), "      ", CF, "%")
print("COMISSÃO DE VENDAS: ", format(Valor_CV, "5.2f"), "      ", CV, "%")
print("IMPOSTOS:           ", format(Valor_IV, "5.2f"), "      ", IV, "%")
print("OUTROS CUSTOS:      ", format(Outros_Custos, "5.2f"), "      ", Perc_Outros_Custos, "%")
print("RENTABILIDADE:      ", format(Rent, "5.2f"), "      ", Perc_Rent, "%")
print("\n\n==============================================\n")


