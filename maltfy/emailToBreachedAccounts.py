# !/usr/bin/python
# -*- coding: cp1252 -*-
#
##################################################################################
#
#	This program is part of apify. You can redistribute it and/or modify
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
import i3visiotools.apify.haveibeenpwned as HIBP

def emailToBreachedAccounts(email=None):
	''' 
		Method that checks if the given email is stored in the HIBP website.

		:param email:	email to verify.

	'''
	me = MaltegoTransform()

	jsonData = HIBP.checkIfHackedInHIBP(email=email)

	# This returns a dictionary like:
	# [{"Title":"Adobe","Name":"Adobe","Domain":"adobe.com","BreachDate":"2013-10-4","AddedDate":"2013-12-04T00:12Z","PwnCount":152445165,"Description":"The big one. In October 2013, 153 million Adobe accounts were breached with each containing an internal ID, username, email, <em>encrypted</em> password and a password hint in plain text. The password cryptography was poorly done and <a href=\"http://stricture-group.com/files/adobe-top100.txt\" target=\"_blank\">many were quickly resolved back to plain text</a>. The unencrypted hints also <a href=\"http://www.troyhunt.com/2013/11/adobe-credentials-and-serious.html\" target=\"_blank\">disclosed much about the passwords</a> adding further to the risk that hundreds of millions of Adobe customers already faced.","DataClasses":["Email addresses","Password hints","Passwords","Usernames"]}]

	#print json.dumps(entities, indent=2)
	for breach in jsonData:
		newEnt = me.addEntity("i3visio.breach",breach["Title"])
		newEnt.setDisplayInformation("<h3>" + breach["Title"] +"</h3><p>" + json.dumps(breach, sort_keys=True, indent=2) + "!</p>");
		for field in breach.keys():
			if field != "Title":
				pass
				# [TO-DO] Appending all the information from the json:
				#newEnt.addAdditionalFields(field,field,True,breach[field])

	# Returning the output text...
	me.returnOutput()

if __name__ == "__main__":
	emailToBreachedAccounts(email=sys.argv[1])


