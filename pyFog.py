#!/usr/bin/env python
#
# pyFog.py
#
# pyFog is a simple API which uses mechanize to complete tasks through the FOG web interface.
# Copyright (C) 2014 John Carruthers, @JC_SoCal

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import mechanize
import cookielib

class pyFog:
	def __init__(self):

		self.br = mechanize.Browser()
		self.cj = cookielib.LWPCookieJar()
		self.br.set_cookiejar(self.cj)

		self.br.set_handle_equiv(True)
		self.br.set_handle_redirect(True)
		self.br.set_handle_referer(True)
		self.br.set_handle_robots(False)
		self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

	def returnHome(self):
		"Returns browser back to the home screen"
		for link in self.br.links():
			if link.url == '?node=home':
				self.br.follow_link(link)

	def findAndFollowLink(self, arg, linktype='url'):
		"Searches the page for either the text or url pieces of a link and follows it"
		success = False
		if linktype == 'url':
			for link in self.br.links():
					if link.url == arg:
						self.br.follow_link(link)
						success = True

		elif linktype == 'text':
			for link in self.br.links():
					if link.text == arg:
						self.br.follow_link(link)
						success = True						
		return success

	def open(self, url):
		"Opens the webpage for the first time"
		try: 
			self.br.open(url)
			return True, 'Success'
		except Exception as e:
			return False, e

	def login(self, user, password):
		"Logs into the fog webpage"
		self.br.select_form(nr=0)
		self.br.form['uname'] = user
		self.br.form['upass'] = password

		self.br.submit()  
		if self.br.title().split()[0] == 'Dashboard':
			return True, 'Success'
		else:
			return False, 'Could not login'

	def logout(self):
		"Logs out of the fog webpage"
		for link in self.br.links():
			if link.url == "?node=logout":
				self.br.follow_link(link)
		if self.br.title().split()[0] == 'Login':
			return True, 'Success'
		else:
			return False, 'Could not logout'

	def upload(self, hostname):
		"Upload will pull an image from a client computer (hostname) that will be saved on the server."
		try:
			if not self.findAndFollowLink("?node=host"):
                raise Exception('Error navigating site: did not find host button')

			if not self.findAndFollowLink("/fog/management/index.php?node=host&sub=list"):
                raise Exception('Error navigating site: did not find host-list button')

			if not self.findAndFollowLink(hostname, 'text'):
				raise Exception('Hostname not found', hostname)

			if not self.findAndFollowLink('Basic Tasks', 'text'):
                raise Exception('Error navigating site: did not find basic tasks button')

			if not self.findAndFollowLink('[IMG]Upload', 'text'):
                raise Exception('Error navigating site: did not find upload button')			

			self.br.select_form(nr=0)
			self.br.submit()

			self.returnHome()

			return True, 'Success'

		except Exception as e:
			return False, e

	def deploy(self, hostname):
		"Deploy action will send an image saved on the FOG server to the client computer (hostname) with all included snapins. "
		try:
			if not self.findAndFollowLink("?node=host"):
                raise Exception('Error navigating site: did not find host button')

			if not self.findAndFollowLink("/fog/management/index.php?node=host&sub=list"):
                raise Exception('Error navigating site: did not find host list button')

			if not self.findAndFollowLink(hostname, 'text'):
				raise Exception('Hostname not found', hostname)

			if not self.findAndFollowLink('Basic Tasks', 'text'):
                raise Exception('Error navigating site: did not find basic tasks button')

			if not self.findAndFollowLink('[IMG]Deploy', 'text'):
                raise Exception('Error navigating site: did not find Download button')			

			self.br.select_form(nr=0)
			self.br.submit()

			self.returnHome()

			return True, 'Success'

		except Exception as e:
			return False, e			

	def wol(self, hostname, schedule=''):
		"Wake Up will attempt to send the Wake-On-LAN packet to the computer (hostname) to turn the computer on. In switched environments, you typically need to configure your hardware to allow for this (iphelper)."
		try:
			if not self.findAndFollowLink("?node=host"):
				raise Exception('Error navigating site')

			if not self.findAndFollowLink("/fog/management/index.php?node=host&sub=list"):
				raise Exception('Error navigating site')

			if not self.findAndFollowLink(hostname, 'text'):
				raise Exception('Hostname not found', hostname)

			if not self.findAndFollowLink('Basic Tasks', 'text'):
				raise Exception('Error navigating site')

			if not self.findAndFollowLink('[IMG]Advanced', 'text'):
				raise Exception('Error navigating site')

			if not self.findAndFollowLink('[IMG]Wake Up', 'text'):
				raise Exception('Error navigating site')								

			self.br.select_form(nr=0)	
			if schedule:
				self.br.find_control("singlesched").items[0].selected=True
				self.br.form["singlescheddate"] = schedule

			response = self.br.submit()
			if "Failed to schedule task." in response.read():
				raise Exception("Failed to schedule task. Datetime is either invalid or the task already exists.")

			self.returnHome()
			return True, 'Success'

		except Exception as e:
			return False, e		
