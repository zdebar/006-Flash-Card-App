import logging
import json
import csv

"Extract Data From txt files and conver to json and csv"

INPUT_FILE = "CZENG.txt"
OUTPUT_JSON_FILE = "data.json"
OUTPUT_CSV_FILE = "data.csv"

# INPUT_FILE = "Test.txt"
# OUTPUT_JSON_FILE = "test.json"
# OUTPUT_CSV_FILE = "test.csv"


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
data_json = {}
data_csv = []


# Open the text file for reading
with open(INPUT_FILE, 'r', encoding='utf-8') as file:
    # Read each line in the file
    while True:
        lines = [file.readline().strip() for _ in range(3)]
        if not any(lines):
            break
        logging.debug(lines)
        czech_word = lines[0].split("<")[0].strip("\".")
        # czech_word = lines[0].strip("<br>\"")
        logging.debug(czech_word)

        try:
            word_info = lines[1].replace("(",")").split(")")[1]
            logging.debug(word_info)
        except IndexError:
            word_info = ""

        english_word = lines[1].split("\t")[1].split("<br>")[0].strip("[]'\"")
        logging.debug(english_word)

        try:
            english_pronunciation = lines[2].replace("[", "]").split("]")[1]
        except IndexError:
            english_pronunciation = ""
        logging.debug(english_pronunciation)

        data_json[czech_word] = [english_word, english_pronunciation, word_info]
        data_csv.append([czech_word, english_word, english_pronunciation, word_info])

# Write data to CSV file
print(data_csv)
file_path_csv = OUTPUT_CSV_FILE
with open(file_path_csv, mode='w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    for row in data_csv:
        writer.writerow(row)

# Write data do JSON file
file_path = OUTPUT_JSON_FILE
with open(file_path, mode='w', newline='', encoding="utf-8") as file:
    json.dump(data_json, file)
