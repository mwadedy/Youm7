import requests
import csv
from lxml import html

def scrape_page(url):
    # Function to fetch the webpage content using the provided URL
    response = requests.get(url)
    if response.status_code == 200:
        return html.fromstring(response.text)
    else:
        return None

def extract_data(tree):
    # Function to extract data (Title, Link, Date, Synopsis) from the webpage's HTML tree using XPath
    titles = tree.xpath('/html/body/section/div[3]/div/div/div/div/div[1]/div[3]/div/h3/a/text()')
    links = tree.xpath('/html/body/section/div[3]/div/div/div/div/div[1]/div[3]/div/h3/a/@href')
    dates = tree.xpath('//*[@id="paging"]/div[3]/div/span/text()')
    synopses = tree.xpath('//*[@id="paging"]/div[3]/div/p/text()')
    return zip(titles, links, dates, synopses)

def save_to_csv(data):
    # Function to save the extracted data to a CSV file named "youm7.csv"
    with open("youm7.csv", mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        # Write header row to the CSV file
        writer.writerow(["Title", "Link", "Date", "Synopsis"])
        # Write each row of data to the CSV file
        writer.writerows(data)

def main():
    base_url = "https://www.youm7.com/Section/%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF-%D9%88%D8%A8%D9%88%D8%B1%D8%B5%D8%A9/297/"
    start_page = 1
    end_page = 7466

    all_data = []

    # Loop through the range of pages to scrape data from each page
    for page_num in range(start_page, end_page + 1):
        url = base_url + str(page_num)
        tree = scrape_page(url)
        if tree is not None:
            # Extract data from the page and add it to the 'all_data' list
            data = extract_data(tree)
            all_data.extend(data)

    # Save all the extracted data to the CSV file
    save_to_csv(all_data)

if __name__ == "__main__":
    main()
