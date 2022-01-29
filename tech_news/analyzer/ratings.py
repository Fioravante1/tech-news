from tech_news.database import find_news


# Requisito 10
# Consultei repositorio de Vitor cabrera
# assim que tive melhor entendimento do sort
def top_5_news():
    result = find_news()
    list_title_url = []

    result.sort(
        key=lambda x: x["shares_count"] + x["comments_count"], reverse=True
    )

    cinco_mais = result[:5]

    for notice in cinco_mais:
        list_title_url.append((notice["title"], notice["url"]))

    return list_title_url


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
