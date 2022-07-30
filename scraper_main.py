import re
import os
import requests
import string
from bs4 import BeautifulSoup


def get_info(url):
    if url.find("title") == -1:
        print("Invalid movie page!")
    else:
        response = requests.get(url, headers={'Accept-Language': 'en-US,en,q=0.5'})
        info = {}
        soup = BeautifulSoup(response.content, "html.parser")
        title = {"title": list(soup.find_all("h1"))[0].text}
        info.update(title)
        description = {"description": list(soup.find_all("span", {'data-testid': 'plot-l'}))[0].text}
        info.update(description)
        print(info)


def save(url):
    with open("source.html", "wb") as file_save:
        response = requests.get(url).content
        file_save.write(response)
    print("\nContent saved.")


def main_work(number_of_page, article_need):
    N = 1
    for url in f_pages(number_of_page):
        response = BeautifulSoup(requests.get(url).content, "html.parser")
        soup_article = list(response.find_all("article"))
        os.mkdir(f"Page_{N}")
        os.chdir(f"Page_{N}")
        N += 1
        for article in soup_article:
            type_news = article.find("span", {"data-test": "article.type"}).text.replace("\n", "")
            if type_news == str(article_need):
                link = article.find("a", {"data-track-action": "view article"})
                file_name = str(link.text).rstrip(string.punctuation).replace(" ", "_")
                with open(f"{file_name}.txt", "w", encoding="utf-8") as file_news:
                    text_news = "https://www.nature.com" + link.get("href")
                    cite_text_news = BeautifulSoup(requests.get(text_news).content, "html.parser")
                    text_of_news = cite_text_news.find("div", {"class": re.compile(".+body.+")}).text.replace("\n", "")
                    file_news.write(text_of_news)
        os.chdir(os.path.dirname(os.getcwd()))


def f_pages(number_of_page):
    lst_url = []
    for page in range(1, number_of_page + 1):
        pages = {}
        dict.setdefault(pages, "page", page)
        url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020"
        cite = requests.get(url, params=pages)
        lst_url.append(cite.url)
    return lst_url


main_work(int(input()), str(input()))
