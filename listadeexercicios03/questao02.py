usuário= input('digite o seu nome de usuário: ')
senha= input('digite a sua senha: ')
while usuário == senha:
    print('ERRO: O usuário e a senha não pode ser iguais')
    usuário= input('digite o seu usuário: ')
    senha= input('digite a sua senha: ')
    print('Usuário: ',usuário)
    print('Senha:', senha)
