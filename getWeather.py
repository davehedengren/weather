import datetime
import requests
import json

apikey = ""
cdoHeaders = {"token":apikey}

electionDates = []
electionDates.append(datetime.date(1981,3,18))
electionDates.append(datetime.date(1982,9,8))
electionDates.append(datetime.date(1981,10,10))

#r = requests.get("http://www.ncdc.noaa.gov/cdo-web/api/v2/", headers=cdoHeaders)

coverageArea="47.5204,-122.2047,47.6139,-122.1065"
startDate=datetime.date(2004,1,1)
endDate=datetime.date(2012,1,1)
r = requests.get("http://www.ncdc.noaa.gov/cdo-web/api/v2/stations?datasetid=GHCND&datatypeid=TMAX&datatypeid=TMIN&datatypeid=TPCP&extent="+coverageArea+"&startdate="+str(startDate)+"&enddate="+str(endDate)+"&sort=datacoverage&sortorder=desc",headers=cdoHeaders)
id = r.json()['results'][0]['id']
r = requests.get("http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=TPCP&datatypeid=TMAX&datatypeid=TMIN&stationid="+id+"&startdate="+str(startDate)+"&enddate="+str(endDate),headers=cdoHeaders)
