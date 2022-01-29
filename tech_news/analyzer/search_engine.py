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
# https://www.w3schools.com/python/python_datetime.asp
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
    result = find_news()
    list_title_url = []
    for notice in result:
        for fonte in notice["sources"]:
            if fonte.upper() == source.upper():
                list_title_url.append((notice["title"], notice["url"]))
    return list_title_url


# Requisito 9
def search_by_category(category):
    result = find_news()
    list_title_url = []
    for notice in result:
        for categoria in notice["categories"]:
            if categoria.upper() == category.upper():
                list_title_url.append((notice["title"], notice["url"]))
    return list_title_url
