﻿#China Air Quality Data - 366 Cities

###Data Source
https://www.aqistudy.cn/historydata/index.php

###Usage
For daily data:

**python crawl_api.py**

For monthly data:

**python crawl_api_monthly.py**

###months.txt
List of months to be crawled, by default, ranging from "2013-01" to "2017-01"

###city.txt
List of cities [in Chinese] to be crawled.

###Outputs
Outputs will be written to the subfolder \data

Each city will has a .csv file with the following columns:

City[in Chinese],Date,AQI,AQI Range,Air Quality Level[in Chinese],PM2.5,PM10,SO2,CO,NO2,O3,Rank

###Disclaimer
Use as-is without warranties. Please adhere to terms of service of the data source if applicable.
