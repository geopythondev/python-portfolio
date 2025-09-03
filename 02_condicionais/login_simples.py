# Exemplo 02 - Login simples em Python

# Solicita o nome do usuário
usuario = input("Digite seu nome de usuário: ")

# Solicita a senha
senha = input("Digite sua senha: ")

# Condicional para verificar login
if usuario == "geovane" and senha == "1234":
    print(f"✅ Login bem-sucedido! Bem-vindo, {usuario}!")
else:
    print("❌ Usuário ou senha incorretos.")
