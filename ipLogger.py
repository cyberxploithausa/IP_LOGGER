import pygeoip

gip = pygeoip.GeoIP("GeoLiteCity.dat") #Download this file on github
res =  gip.record_by_addr('IP address') #Anan zaku shigar da IP address din target dinku

for k, v in res.items():
     print("%s : %s"  % (k, v))