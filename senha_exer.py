import random
import string


def gerar_senha(tamanho=12):
    """Gera uma senha segura com o tamanho especificado."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


# Pergunta ao usuário o tamanho da senha
while True:
    try:
        tamanho = int(input("Digite o tamanho da senha desejada: "))
        if tamanho < 6:
            print("A senha deve ter pelo menos 6 caracteres.")
            continue
        break
    except ValueError:
        print("Por favor, insira um número válido.")

# Gera e exibe a senha
senha_gerada = gerar_senha(tamanho)
print(f"Sua senha segura é: {senha_gerada}")
