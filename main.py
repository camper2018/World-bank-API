


import requests
import json
import pandas as pd
# from sodapy import Socrata
# url = "  http://api.worldbank.org/V2/incomeLevel/LIC/country?format=json"
# url2 = "http://api.worldbank.org/v2/en/sources/15/series/all/metadata?page=1&per_page=20000&format=json"
# url3 = " http://api.worldbank.org/v2/indicators/NY.GDP.MKTP.CD?format=json"
# url4 = "http://api.worldbank.org/v2/indicator/NY.GDP.MKTP.CD?source=11&format=json"
# url5 = "https://datacatalog.worldbank.org/node/94591.json"
# url6 = "https://databank.worldbank.org/source/joint-external-debt-hub?format=json"
import world_bank_data as wb
# pd.set_option('display.max_rows', 10)'
pd.set_option('display.max_columns', None)


def convert_dataframe_to_dictionary(dataframe):
    """
       param: dataframe
       return: dictionary
    """
    result = dataframe.to_json(orient="index")
    parsed = json.loads(result)
    return parsed


# get  sources
sources = wb.get_sources()
sources = convert_dataframe_to_dictionary(sources)
print(sources)

indicators = wb.get_indicators(source=1)
# indicators = convert_dataframe_to_dictionary(indicators)
print(indicators)
pakistan = wb.get_series(country="PAK", indicator="NY.GDP.MKTP.CD")

# print(pakistan.to_dict())
# result = sources.to_json(orient="index")
# parsed = json.loads(result)
# print(parsed)


# response = requests.get(url5)
# print(response.content)
# if response.ok:
#     data = json.loads(response.content)
#     print(f'The response contains {len(data)} properties')
#     print(data)
#     # for key in data:
#     #     print(f"{key}:{data[key]}")
# else:
#     response.raise_for_status()





