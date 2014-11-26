# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This program is part of maltfy. You can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##################################################################################

from MaltegoTransform import *
import sys
import json
import urllib2
import i3visiotools.darkfy.lib.processing as darkfy


def textToDeepWebSearch(text=None):
	''' 
		Method that performs a search on different deep web search engines. The output format is as follows:
 {
  "<text_to_be_looked_for>": {
    "i3visio.ahmia": [
      {
        "i3visio.date": [
          "Oct. 7, 2014, 5:12 p.m."
        ], 
        "i3visio.url": [
          " http://doxbinzqkeoso6sl.tor2web.fi/doxviewer.php?dox=Paula_Patr_cia"
        ], 
        "i3visio.text": [], 
        "i3visio.title": [
          " DOXBIN - POWERED BY PLAN9 FROM BELL LABS "
        ]
      }, 
...
}
		:param text:	text to be searched.

		:return:	None
	'''
	me = MaltegoTransform()

	jsonData = darkfy.searchTerms(words=[text])
	
	# Adding the data to the current resource. In this case, this is NOT needed
	#me.setDisplayInformation(json.dumps(jsonData, sort_keys=True, indent=2))
	# Results is a dict containing the different platforms.
	for text in jsonData.keys():
		results = jsonData[text]
		for platform in results.keys():
			resources = results[platform]
			for res in resources:
				# Note that ALL the results provided are a list!
				newEnt = me.addEntity("i3visio.text",res["i3visio.title"][0])
				newEnt.setDisplayInformation(json.dumps("<h3>" +res["i3visio.title"][0] + "</h3>\n" + str(res), sort_keys=True, indent=2))
				newEnt.addAdditionalFields("i3visio.platform", "i3visio.platform", True, platform)
				for field in res.keys():
					if field != "i3visio.title":
						try:
							newEnt.addAdditionalFields(field, field, True, res[field][0])
						except:
							pass
	# Returning the output text...
	me.returnOutput()

if __name__ == "__main__":
	textToDeepWebSearch(text=sys.argv[1])


