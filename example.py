import fog_api

url = 'http://localhost/fog/management/index.php'

this = fog_api.Fog()

status,msg = this.open(url)
if not status:
	print msg
	exit()

status,msg = this.login('fog','password')
if not status:
	print msg
	exit()

status, msg = this.deploy('Demo')
if not status:
	print msg
	exit()

status, msg = this.logout()
if not status:
	print msg
	exit()


