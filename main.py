import minado

bombas = 9
linhas = 9
colunas = 9
campo = minado.criarCampoMinado(bombas, linhas, colunas)

print()
campo_temporario = minado.prepararCampo(campo)

minado.jogar(campo, campo_temporario)


