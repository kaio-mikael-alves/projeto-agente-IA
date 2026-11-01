def ler_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return None
    return conteudo
texto = ler_arquivo("estu/teste.txt")
print(texto)
