#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# comun.py
#
# Copyright (C) 2011 Lorenzo Carbonell
# lorenzo.carbonell.cerezo@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#

__author__ = 'Lorenzo Carbonell <lorenzo.carbonell.cerezo@gmail.com>'
__date__ ='$24/09/2011'
__copyright__ = 'Copyright (c) 2011 Lorenzo Carbonell'
__license__ = 'GPLV3'
__url__ = 'http://www.atareao.es'

import os
import locale
import gettext
import sys
######################################

def is_package():
    return __file__.find('src') < 0

######################################
PARAMS = {	'first-time':True,
			'version':'',
			'weather-service':'openweathermap',
			'main-location':True,
			'autolocation':False,
			'location':'',
			'latitude':0,
			'longitude':0,
			'show-temperature':True,
			'show-notifications':True,
			'second-location':False,
			'location2':'',
			'latitude2':0,
			'longitude2':0,
			'show-temperature2':True,
			'show-notifications2':True,
			'temperature':'C',
			'pressure':'mbar',
			'visibility':'km',
			'wind':'km/h',
			'snow':'cm',
			'rain':'mm',
			'24h':True,
			'refresh':1,
			'icon-light':True,
			'wwo-key':'',
			'wu-key':'',
			'widget1':False,
			'widget2':False,
			'onwidget1hide':False,
			'onwidget2hide':False,
			'onwidget1top':False,
			'onwidget2top':False,
			'showintaskbar1':False,
			'showintaskbar2':False,
			'onalldesktop1':True,
			'onalldesktop2':True,
			'skin1':'/usr/share/my-weather-indicator/skins/little',
			'skin2':'/usr/share/my-weather-indicator/skins/little',
			'wp1-x':0,
			'wp1-y':0,
			'wp2-x':0,
			'wp2-y':0
			}

APP = 'my-weather-indicator'
APP_CONF = APP + '.conf'
APPNAME = 'My-Weather-Indicator'
CONFIG_DIR = os.path.join(os.path.expanduser('~'),'.config')
CONFIG_APP_DIR = os.path.join(CONFIG_DIR, APP)
CONFIG_FILE = os.path.join(CONFIG_APP_DIR, APP_CONF)
#########################################

# check if running from source
if is_package():
	ROOTDIR = '/opt/extras.ubuntu.com/my-weather-indicator/share/'
	LANGDIR = os.path.join(ROOTDIR, 'locale-langpack')
	APPDIR = os.path.join(ROOTDIR, APP)
	LOGOSDIR = os.path.join(APPDIR, 'logos')  
	ICONDIR = os.path.join(APPDIR, 'icons') 
	IMAGESDIR = os.path.join(APPDIR, 'images')
	SOCIALDIR = os.path.join(APPDIR, 'social')
	WIMAGESDIR= os.path.join(APPDIR, 'wimages')
	CHANGELOG = os.path.join(APPDIR,'changelog')
	ICON = '/opt/extras.ubuntu.com/my-weather-indicator/share/pixmaps/my-weather-indicator.png'
	AUTOSTART = '/opt/extras.ubuntu.com/my-weather-indicator/share/my-weather-indicator/my-weather-indicator-autostart.desktop'
else:
	ROOTDIR = os.path.dirname(__file__)
	LANGDIR = os.path.normpath(os.path.join(ROOTDIR, '../template1'))
	APPDIR = ROOTDIR
	DATADIR = os.path.normpath(os.path.join(ROOTDIR, '../data'))
	LOGOSDIR = os.path.normpath(os.path.join(ROOTDIR, '../data/logos'))
	ICONDIR = os.path.normpath(os.path.join(ROOTDIR, '../data/icons'))
	IMAGESDIR = os.path.normpath(os.path.join(ROOTDIR, '../data/images'))
	SOCIALDIR = os.path.normpath(os.path.join(ROOTDIR, '../data/social'))
	WIMAGESDIR = os.path.normpath(os.path.join(ROOTDIR, '../data/wimages'))
	DEBIANDIR = os.path.normpath(os.path.join(ROOTDIR, '../debian'))
	CHANGELOG = os.path.join(DEBIANDIR,'changelog')
	ICON = os.path.join(IMAGESDIR,'my-weather-indicator.png')
	AUTOSTART = os.path.join(DATADIR,'my-weather-indicator-autostart.desktop')

f = open(CHANGELOG,'r')
line = f.readline()
f.close()
pos=line.find('(')
posf=line.find(')',pos)
VERSION = line[pos+1:posf].strip()
if not is_package():
	VERSION = VERSION + '-src'
HTML = os.path.join(APPDIR, 'openweathermap.html')
HTML_WAI = os.path.join(APPDIR, 'whereami.html')
HTML_GRAPH = os.path.join(APPDIR, 'graph.html')
GOOGLELOGO = os.path.join(LOGOSDIR, 'wgooglelogo.png')
UNDERGROUNDLOGO = os.path.join(LOGOSDIR, 'wundergroundlogo.png')   
UNDERGROUNDWEB = 'http://www.wunderground.com/?apiref=6563686488165a78'
YAHOOLOGO = os.path.join(LOGOSDIR, 'wyahoologo.png')   
YAHOOWEB = 'http://weather.yahoo.com/'
WOLRDWEATHERONLINE = os.path.join(LOGOSDIR, 'worldonlinelogo.png')   
WOLRDWEATHERONLINEWEB = 'http://www.worldweatheronline.com/'
OPENWEATHERMAPLOGO = os.path.join(LOGOSDIR, 'wopenweathermaplogo.png')   
OPENWEATHERMAPWEB = 'http://openweathermap.org/'
####
try:
	current_locale, encoding = locale.getdefaultlocale()
	language = gettext.translation(APP, LANGDIR, [current_locale])
	language.install()
	print(language)
	if sys.version_info[0] == 3:
		_ = language.gettext
	else:
		_ = language.ugettext
except Exception as e:
	print(e)
	_ = str
APPNAME = _(APPNAME)
if sys.version_info[0] == 3:	
	import urllib.request
	def read_from_url(url):
		try:
			url = url.replace(' ','%20')
			request = urllib.request.Request(url, headers={'User-Agent' : 'Magic Browser'})
			f = urllib.request.urlopen(request)
			json_string = f.read()
			f.close()
			return json_string
		except:
			return None

	def internet_on():
		try:
			response=urllib.request.urlopen('http://google.com',timeout=1)
			return True
		except:
			pass
		return False
	def fromunicode(cadena):
		return cadena

else:
	import urllib2
	import urllib	
	def read_from_url(url):
		try:
			url = url.replace(' ','%20')		
			request = urllib2.Request(url, headers={'User-Agent' : 'Magic Browser'})
			f = urllib2.urlopen(request)
			json_string = f.read()
			f.close()
			return json_string
		except:
			return None
		
	def internet_on():
		try:
			response=urllib2.urlopen('http://google.com',timeout=1)
			return True
		except:
			pass
		return False
	def fromunicode(cadena):
		if type(cadena) == unicode:
			ans = cadena.encode('utf-8')
			print(type(ans),ans)
			return ans
		return cadena
