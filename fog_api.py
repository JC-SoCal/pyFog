import mechanize
import cookielib

class Fog:
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
		for link in self.br.links():
			if link.url == '?node=home':
				self.br.follow_link(link)

	def findAndFollowLink(self, arg, linktype='url'):
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
		try: 
			self.br.open(url)
			return True, 'Success'
		except Exception as e:
			return False, e

	def login(self, user, password):
		#select the fog login form, and apply creds
		self.br.select_form(nr=0)
		self.br.form['uname'] = user
		self.br.form['upass'] = password

		self.br.submit()  
		if self.br.title().split()[0] == 'Dashboard':
			return True, 'Success'
		else:
			return False, 'Could not login'

	def logout(self):
		for link in self.br.links():
			if link.url == "?node=logout":
				self.br.follow_link(link)
		if self.br.title().split()[0] == 'Login':
			return True, 'Success'
		else:
			return False, 'Could not logout'

	def upload(self, hostname):
		try:
			if not self.findAndFollowLink("?node=host"):
				raise Exception('Error navigating site')

			if not self.findAndFollowLink("/fog/management/index.php?node=host&sub=list"):
				raise Exception('Error navigating site')

			if not self.findAndFollowLink(hostname, 'text'):
				raise Exception('Hostname not found', hostname)

			if not self.findAndFollowLink('Basic Tasks', 'text'):
				raise Exception('Error navigating site')

			if not self.findAndFollowLink('[IMG]Upload', 'text'):
				raise Exception('Error navigating site')			

			self.br.select_form(nr=0)
			self.br.submit()

			self.returnHome()

			return True, 'Success'

		except Exception as e:
			return False, e

	def deploy(self, hostname):
		try:
			if not self.findAndFollowLink("?node=host"):
				raise Exception('Error navigating site')

			if not self.findAndFollowLink("/fog/management/index.php?node=host&sub=list"):
				raise Exception('Error navigating site')

			if not self.findAndFollowLink(hostname, 'text'):
				raise Exception('Hostname not found', hostname)

			if not self.findAndFollowLink('Basic Tasks', 'text'):
				raise Exception('Error navigating site')

			if not self.findAndFollowLink('[IMG]Deploy', 'text'):
				raise Exception('Error navigating site')			

			self.br.select_form(nr=0)
			self.br.submit()

			self.returnHome()

			return True, 'Success'

		except Exception as e:
			return False, e			

	def wol(self, hostname):
		try:
			if not self.findAndFollowLink("?node=host"):
				raise Exception('Error navigating site')

			if not self.findAndFollowLink("/fog/management/index.php?node=host&sub=list"):
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
			self.br.submit()

			self.returnHome()

			return True, 'Success'

		except Exception as e:
			return False, e		