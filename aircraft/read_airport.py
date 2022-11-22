import csv
from airport import Airport


class Read_airport:
    all_airports = {}
    all_country_currency = {}  # full->short
    currency_name = {}  # bdt-> dollar

    def __init__(self):
        self.load_airport('./airports.csv')

    def load_airport(self, fileName):

        with open('./country_currency.csv', 'r', encoding="utf-8") as country_currency_file:
            lines = csv.reader(country_currency_file)
            try:
                for line in lines:
                    self.all_country_currency[line[0]] = line[1]

            except KeyError as ke:
                print(ke)

        with open('./currency.csv', 'r', encoding="utf-8")as fileReader:
            lines = csv.reader(fileReader)
            for line in lines:
                try:
                    self.currency_name[line[1]] = line[3]
                except KeyError as ke:
                    print(ke)

        with open(fileName, 'r',  encoding="utf-8")as fileReader:
            lines = csv.reader(fileReader)
            for line in lines:
                try:
                    country_currency = self.all_country_currency[line[3]]
                    currency_convert = self.currency_name[country_currency]
                    self.all_airports[line[4]] = Airport(
                        line[0], line[1], line[2], line[3], line[4], line[6], line[7], currency_convert)
                except KeyError as ke:
                    print(ke)


all_load_data = Read_airport()
print(all_load_data.all_airports)