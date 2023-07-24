import requests
import csv
from lxml import html

def scrape_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return html.fromstring(response.text)
    else:
        return None

def extract_data(tree):
    titles = tree.xpath('/html/body/section/div[3]/div/div/div/div/div[1]/div[3]/div/h3/a/text()')
    links = tree.xpath('/html/body/section/div[3]/div/div/div/div/div[1]/div[3]/div/h3/a/@href')
    dates = tree.xpath('//*[@id="paging"]/div[3]/div/span/text()')
    synopses = tree.xpath('//*[@id="paging"]/div[3]/div/p/text()')
    return zip(titles, links, dates, synopses)

def save_to_csv(data):
    with open("youm7.csv", mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Link", "Date", "Synopsis"])
        writer.writerows(data)

def main():
    base_url = "https://www.youm7.com/Section/%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF-%D9%88%D8%A8%D9%88%D8%B1%D8%B5%D8%A9/297/"
    start_page = 1
    end_page = 7466

    all_data = []

    for page_num in range(start_page, end_page + 1):
        url = base_url + str(page_num)
        tree = scrape_page(url)
        if tree is not None:
            data = extract_data(tree)
            all_data.extend(data)

    save_to_csv(all_data)

if __name__ == "__main__":
    main()
