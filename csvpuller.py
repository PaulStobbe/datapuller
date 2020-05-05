import pandas as pd
import io
import requests

#url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
url="https://opendata.ecdc.europa.eu/covid19/casedistribution/csv"
s=requests.get(url).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')))
print(c)