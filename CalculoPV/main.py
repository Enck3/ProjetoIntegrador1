print("\n\n===================================\n")
print("<<<<<<<< CADASTRO DE PRODUTO >>>>>>>>>>")
print("\n\n===================================\n")
Cod_Prod = int(input("CODIGO: "))
Nome_Prod = input("NOME: ")
Desc_Prod = input("DESCRIÇÃO: ")
CP = float(input("CUSTO DE AQUISIÇÃO: "))
CF = float(input("CUSTO FIXO: "))
CV = float(input("COMISSÃO DE VENDAS: "))
IV = float(input("IMPOSTO (SOBRE VENDA): "))
ML = float(input("MARGEM DE LUCRO: "))


PV = CP / (1 - ((CF + CV + IV + ML)/100))
Perc_CP = (100*CP)/PV
Rec_Bruta = PV-CP
Perc_Rec_Bruta = (100*Rec_Bruta)/PV 
Valor_CF = (PV*CF)/100
Valor_CV = (PV*CV)/100
Valor_IV = (PV*IV)/100
Outros_Custos = Valor_CF + Valor_CV + Valor_IV
Perc_Outros_Custos = (100*Outros_Custos)/PV
Rent = Rec_Bruta - Outros_Custos
Perc_Rent = Perc_Rec_Bruta - Perc_Outros_Custos


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


