# ============================================================
# Programa: Sistema de Desconto Progressivo - Loja Online
# Arquivo: Jonathan_Ag6_DS_I.py
# ============================================================

# 1. Entrada de dados: solicita o valor total da compra ao usuário
entrada_usuario = input("Digite o valor total da compra (R$): ")

# Trata a entrada permitindo o uso de vírgula ou ponto como separador decimal
valor_compra = float(entrada_usuario.replace(",", "."))

# 2. Processamento: estrutura de decisão para definir o percentual de desconto
if valor_compra < 200.00:
    percentual_desconto = 5
elif valor_compra < 300.00:
    percentual_desconto = 10
else:
    percentual_desconto = 15

# 3. Cálculos: computação do valor do desconto (R$) e do valor final a pagar
valor_desconto = valor_compra * (percentual_desconto / 100)
valor_final = valor_compra - valor_desconto

# 4. Saída de dados: exibe os resultados formatados com duas casas decimais
print("\n--- RESUMO DA COMPRA ---")
print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {percentual_desconto}% (R$ {valor_desconto:.2f})")
print(f"Valor total a pagar: R$ {valor_final:.2f}")
input("\nPressione Enter para sair...")