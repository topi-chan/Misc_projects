import requests, sys, json, csv

class WeatherForecast():
    '''Allows you to forecast rain probability from API, write results into file'''

    def __init__(self):
        self.forecast_dict = {}
        self.forecast_date = None
        self.forecast_file_dict = {}
        self.list = []

    def main(self, api_key, forecast_date):
        querystring = {"lat":"50","lon":"19","unit_system":"si",
        "start_time":forecast_date,
        "end_time":forecast_date,
        "fields":"precipitation_probability",
        "apikey":api_key}
        response = requests.request("GET",
        "https://api.climacell.co/v3/weather/forecast/daily", params=querystring)
        self.forecast_date = forecast_date
        api_response_list = []
        for line in response.json():
            api_response_list.append(line)
        return_list = api_response_list[0]
        rain_list = return_list['precipitation_probability']
        rain = rain_list['value']
        if rain == 0:
            print("Nie będzie padać")
            self.forecast_dict[forecast_date] = "Nie będzie padać"
        elif rain <= 50:
            print("Nie wiem")
            self.forecast_dict[forecast_date] = "Nie wiem"
        else:
            print("Będzie padać")
            self.forecast_dict[forecast_date] = "Będzie padać"

    def csv_save(self, file_name):
        datafile = open(file_name)
        for line in datafile:
            if self.forecast_date in line:
                return self.dict_save(file_name)
        with open(file_name, "a+", newline="") as file:
            writer = csv.writer(file, delimiter=',', lineterminator="\r")
            writer.writerow(self.forecast_dict.keys())
            writer.writerow(self.forecast_dict.values())
        self.dict_save(file_name)

    def dict_save(self, file_name):
        with open(file_name) as f:
            for line in f:
                line = line.rstrip()
                self.list.append(line)
        it = iter(self.list)
        self.forecast_file_dict = dict(zip(it, it))

    def items(self):
        for item in self.forecast_file_dict.items():
            yield item

    def __getitem__(self, key):
        return self.forecast_file_dict[key]


wf = WeatherForecast()
wf.main("{}".format(sys.argv[1]), "{}".format(sys.argv[2]))
wf.csv_save("dates.csv")
for item in wf.items():
    print(item)
print(wf["2020-12-16"])
