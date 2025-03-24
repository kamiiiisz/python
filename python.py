idade = int(input('qual sua idade?'))

if(idade<16):
  print('nao precisa votar!')
elif(idade == 16 or idade > 65) :
    print('voto nao obrigatorio')
else:
    print('voto obrigatorio')
