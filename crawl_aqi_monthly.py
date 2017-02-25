#encoding=utf-8
from bs4 import BeautifulSoup
import requests
import os
import time

base_url = 'https://www.aqistudy.cn/historydata/monthdata.php?city='

def get_city_set():
    str_file = r'city.txt'
    fp = open(str_file,'rb')
    city_set = list()
    for line in fp.readlines():
        city_set.append(str(line.strip())) #encoding='utf-8'
    return city_set

city_set = get_city_set()
no_data_city = []
# print city_set

if not os.path.isdir("data_month/"):
    os.mkdir("data_month/")

for city in city_set:
    if '\xef\xbb\xbf' in city:
        city = city.replace('\xef\xbb\xbf','')
    file_name = 'data_month/' + city.decode('utf8').encode('gbk') + '.csv'

    print time.ctime(), city.decode('utf8').encode('gbk'),

    weburl = ('%s%s' % (base_url,city))
    response = None

    while response is None:
        try:
            response = requests.get(weburl).content
        except:
            pass

    soup = BeautifulSoup(response,'html.parser',from_encoding='utf-8')
    result = soup.find_all('td',attrs={'align':'center'},recursive=True)

    if len(result) == 6:
        print("No Data")
        no_data_city.append(city)
    else:
        with open(file_name, 'w') as fp:
            # UTF-8 encoded BOM
            # https://docs.python.org/2/library/codecs.html#encodings-and-unicode
            fp.write('\xEF\xBB\xBF')

            result = filter(lambda x: 'style' not in x.attrs, result)

            if(len(result)%11 != 0):
                print "# of Column Error",
            else:
                print len(result)/11, "months",

            for j in range(0,len(result),11):
                # 11 columns per day
                # 日期,AQI,范围,质量等级,PM2.5,PM10,SO2,CO,NO2,O3,排名
                records = []
                for r in range(11):
                    records.append(result[j + r].get_text().strip().encode('utf-8'))

                fp.write( ','.join([city] + records) + '\n')

            print('DONE')

print no_data_city
with open('data_month/no_data_city.txt','w') as fnodata:
    fnodata.write('\n'.join(no_data_city))