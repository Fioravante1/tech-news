from tech_news.database import find_news
import datetime


# Requisito 6
def search_by_title(title):
    result = find_news()
    list_title_url = []
    for notice in result:
        if notice["title"].lower() == title.lower():
            list_title_url.append((notice["title"], notice["url"]))
    return list_title_url


# Requisito 7
def search_by_date(date):
    result = find_news()
    list_title_url = []
    try:
        datetime.date.fromisoformat(date)
        for notice in result:
            if notice["timestamp"].find(date) == 0:
                list_title_url.append((notice["title"], notice["url"]))
        return list_title_url
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
