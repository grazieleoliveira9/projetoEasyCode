 
cliente01 = ['João Paulo', 'Niteroi', '57']
cliente02 = ['May Ortega', 'Sao Paulo', '30']
cliente03 = ['Fabricio Lemos', 'Pernambuco', '19']


print (f"Nome:  {cliente01[0]}, Cidade:  {cliente01[1]}, Idade: {cliente01[2]}")
print (f"Nome:  {cliente02[0]}, Cidade:  {cliente02[1]}, Idade: {cliente02[2]}")
print (f"Nome:  {cliente03[0]}, Cidade:  {cliente03[1]}, Idade: {cliente03[2]}")


produtoCasa = ['Geladeira', 'Armario', 'Mesa']
produtoBanheiro = ['Pia', 'Chuveiro', 'Espelho']
produtoEletronico = ['Caixa de Som', 'Televisão', 'Computador']


ContaApagar01 = int(300)
ContaApagar02 = 700
ContaApagar03 = 400

totalCliente01 = (f'Cliente Pedido Total: {cliente01[0]} , Produto Pedido: {produtoCasa[2]}, Total a pagar: {ContaApagar01 - 10}') #desconto de cliente novo 
print(totalCliente01)



totalCliente02 = (f'Cliente Pedido Total: {cliente02[0]} , Produto Pedido: {produtoEletronico[1]}, Total a pagar: {ContaApagar02 + 50}') #Valor com Frete
print(totalCliente02)

totalCliente03 = (f'Cliente Pedido Total: {cliente03[0]} , Produto Pedido: {produtoBanheiro[0]}, Total a pagar: {ContaApagar03}')
print(totalCliente03)