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

	def deploy(self, hostname):
		try:
			for link in self.br.links():
				if link.url == "?node=host":
					self.br.follow_link(link)

			for link in self.br.links():
				if link.text == 'List All Hosts':
					self.br.follow_link(link)

			host_not_found = 1
			for link in self.br.links():
				if link.text == hostname:
					self.br.follow_link(link)
					host_not_found = 0
				
			if host_not_found:
				raise Exception('Hostname not found', hostname)

			for link in self.br.links():
				if link.text == 'Basic Tasks':
					self.br.follow_link(link)

			for link in self.br.links():
				if link.text == '[IMG]Deploy':
					self.br.follow_link(link)

			self.br.select_form(nr=0)
			self.br.submit()
			return True, 'Success'
		except Exception as e:
			return False, e
