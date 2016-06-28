#! /usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import re
import thread
import pdb

class   Wathereather_Spider_Model:
  def __init__(self):
    self.ok = False
  def getHtml(self,url):
    page=urllib.urlopen(url)
    html=page.read()
    page.close()
    return html
  def getWeather(self,url):
    html = self.getHtml(url)
    #网页源代码样例
    #<dl><dt><a title="长沙天气预报" href="http://www.weather.com.cn/weather/101250101.shtml" target="_blank">
    #长沙</a></dt><dd><a href="http://www.weather.com.cn/static/html/legend.shtml" target="_blank">
    #<img alt="小雨" src="/m2/i/icon_weather/21x15/d07.gif" />
    #<img alt="小雨" src="/m2/i/icon_weather/21x15/n07.gif" /></a>
    #<a href="http://baike.weather.com.cn/index.php?doc-view-1148.php" target="_blank">
    #<span>19℃</span></a>/<a href="http://baike.weather.com.cn/index.php?doc-view-1386.php" 
    #target="_blank"><b>15℃</b></a></dd></dl><dl><dt>
    reg='<dl><dt><a title=.*?>(.*?)</a></dt><dd><a href=.*?><img alt=\"(.*?)\".*?><.*?></a><a href=.*?><span>(.*?)</span></a>(.*?)<a href=.*?><b>(.*?)</b></a></dd></dl>'
    self.weatherList=re.compile(reg).findall(html)
    self.ok=True
    #return weatherList
  def start(self,pydaihao):
    #http://www.weather.com.cn/html/province/beijing.shtml
    url = "".join(["http://www.weather.com.cn/html/province/",pydaihao,".shtml"])
    print url
    thread.start_new_thread(self.getWeather,(url,))

    
weatherModel = Wathereather_Spider_Model()
pydaihao ="hunan"
weatherModel.start(pydaihao)
print "now getting weather of ",pydaihao
while True:
  if weatherModel.ok:  
    for weather in weatherModel.weatherList:
      print ""
      #pdb.set_trace()
      for li in weather:
        print str(li),#.decode('utf-8').encode('gb2312'),
    weatherModel.ok=False
    break