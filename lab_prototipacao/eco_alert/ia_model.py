def classify_report(descricao):
    descricao = descricao.lower()
    if "fumaça" in descricao or "fogo" in descricao:
        return "Queimada", "Alto"
    elif "lixo" in descricao or "sujeira" in descricao:
        return "Descarte de Lixo", "Médio"
    elif "árvore" in descricao or "corte" in descricao:
        return "Desmatamento", "Alto"
    elif "água" in descricao or "óleo" in descricao:
        return "Poluição", "Médio"
    else:
        return "Outros", "Baixo"
