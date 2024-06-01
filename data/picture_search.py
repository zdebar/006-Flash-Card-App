from icrawler.builtin import GoogleImageCrawler, BingImageCrawler
import csv

"""
    Automated searching for keyword images
"""

search_engine_dict = {
    1: GoogleImageCrawler,
    2: BingImageCrawler
}


def read_first_column(csv_file_path):
    first_column_list = []
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row:  # Ensure the row is not empty
                first_column_list.append(row[0])
    return first_column_list


def download_images(search_engine, key):
    # Create a ImageCrawler object
    google_crawler = search_engine(storage={'root_dir': f"./images/{key}"})
    # Define search filters
    filters = {
        "size": "large",
        "license": "commercial,modify"
    }
    # Search and download images
    google_crawler.crawl(keyword=key, max_num=5, filters=filters)


if __name__ == "__main__":

    keyword_list = read_first_column("testing_data/example.csv")
    print(keyword_list)

    for word in keyword_list[6:7]:
        print(word)
        download_images(search_engine_dict[2], word)

