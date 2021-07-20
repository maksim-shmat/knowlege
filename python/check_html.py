import csv
import bs4

def read_html(filename):
    with open(filename) as html_file:
        html = html_file.read()
        return html

def parse_html(html):
    bs = bs4.BeautifulSoup(html, "html.parser")
    lsbels = [x.text for x in bs.select(".forecast-label")]
    forecasts = [x.text for x in bs.select(".forecast-text")]

    return list(zip(labels, forecasts))

def write_to_csv(data, outfilename):
    csv.writer(open(outfilename, "w")).writerows(data)

if __name__ == '__main__':
    html = read_html("forecast.html")
    values = parse_html(html)
    write_to_csv(values, "forecast.csv")
    print(values)

