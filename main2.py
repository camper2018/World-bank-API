import wbdata as wb

countries = wb.get_country()
sources = wb.get_source()
topics = wb.get_topic()

# print all indicators for sources 1-63 by changing range to (5, 10) (10, 15), (15, 20) .....len(sources)
indicators = []
for i, ele in enumerate(sources[0: 5]):
    source = ele['id']
    indicator = wb.get_indicator(source="2")
    # print(indicator)
# for item in indicator:
#     prin

# for country in countries:
#     print(country)
data = wb.get_data('ENF.CONT.COEN.ATDR', country="PAK")
for val in data:
    print(data)

# print(wb.search_indicators("26_Portfolio investment assets"))
# print(wb.get_source(54))
# print(wb.get_indicator(source=54))
# selected_countries = [i['id'] for i in wb.get_country(incomelevel='HIC')]
# df = wb.get_dataframe(indicators={"Q.1C0.1C0.C.9A.ALL.PITT.1.ALL.MV.TO1.ALL": "26_Portfolio investment assets"},
#                       country=selected_countries, source=54, convert_date=True)
# print(df.describe())
# data = wb.get_data("Q.1C0.1C0.C.9A.ALL.PITT.1.ALL.MV.TO1.ALL", country="PAK", source=54)

# for country in countries:
#     print(country.keys())
# for source in sources:
#     print(source)
# for topic in topics:
#     print(topic)
# for item in wb.get_indicator(source=15):
#     print(item)
    # for topic in item['topics']:
    #     print(topic)








