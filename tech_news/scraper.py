import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
    except requests.exceptions.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)

    return selector.css("h3 > a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)

    return selector.css(".tec--btn::attr(href)").get()


# Requisito 4
# https://stackoverflow.com/questions/68746327/find-the-canonical-link-in-a-file-type-file-beautifulsoup
# https://stackoverflow.com/questions/56427277/how-to-extract-the-value-of-the-datetime-attribute-in-a-time-tag-using-xpath-or
def writer(selector):
    return selector.css(".z--font-bold ").css("*::text").get().strip()


def shares_count(selector):
    shares = selector.css(".tec--toolbar__item::text").get()

    if shares:
        return int((shares).strip().split(" ")[0])
    else:
        return 0


def comments_count(selector):
    count = selector.css("button.tec--btn::attr(data-count)").get()
    if count:
        return int(count)
    else:
        return 0


def summary(selector):
    return "".join(
        selector.css(
            "div.tec--article__body > p:nth-child(1) *::text"
        ).getall()
    )


def sources(selector):
    sources_text = selector.css(
        "div.z--mb-16 > div > a.tec--badge::text"
    ).getall()
    return [source.strip() for source in sources_text]


def categories(selector):
    categories_text = selector.css("div#js-categories > a::text").getall()
    return [category.strip() for category in categories_text]


def scrape_noticia(html_content):
    selector = Selector(html_content)

    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".tec--article__header__title::text").get(),
        "timestamp": selector.css("time::attr(datetime)").get(),
        "writer": writer(selector),
        "shares_count": shares_count(selector),
        "comments_count": comments_count(selector),
        "summary": summary(selector),
        "sources": sources(selector),
        "categories": categories(selector),
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    fetch_response = fetch(url)
    list_notice = scrape_novidades(fetch_response)
    results = []

    while len(list_notice) < amount:
        url_base = scrape_next_page_link(fetch_response)
        fetch_response = fetch(url_base)
        list_notice.extend(scrape_novidades(fetch_response))

    for notice_url in list_notice[0:amount]:
        fetch_response = fetch(notice_url)
        notice = scrape_noticia(fetch_response)
        results.append(notice)

    create_news(results)
    return results
