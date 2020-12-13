import requests
import xmltodict

response = requests.get("https://graphical.weather.gov/xml/SOAP_server/\
        ndfdXMLclient.php?whichClient=NDFDgen&lat=41.87&lon=+-87.65&\
        product=glance")
parsed_dict = xmltodict.parse(response.text)
layout_key = parsed_dict['dwml']['data']['time-layout'][0]['layout-key']
forecast_temp = parsed_dict['dwml']['data']['parameters']['temperature']\
        [0]['value'][0]
print(layout_key)
print(forecast_temp)
