import fog_api

url = 'http://192.168.2.15/fog/management/index.php'

this = fog_api.Fog()

status,msg = this.open(url)
if not status:
	print msg
	exit()

status,msg = this.login('fog','password')
if not status:
	print msg
	exit()

status, msg = this.deploy('DirtyBox')
if not status:
	print msg
	exit()

status, msg = this.logout()
if not status:
	print msg
	exit()


