import urllib

from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2020, 3, 1)
end_date = date(2020, 3, 10)
for single_date in daterange(start_date, end_date):
    year = single_date.strftime("%Y")
    month = single_date.strftime("%-m")
    day = single_date.strftime("%-d")
    url = "https://d1k37mkoj29puy.cloudfront.net/nytimes.com/2020/"+month+"/"+day+"/14/2/screenshot.jpeg"
    urllib.urlretrieve(url, year+month+day+".jpeg")
