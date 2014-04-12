import pyFog

this = pyFog.pyFog()

status,msg = this.open('http://192.168.2.15/fog/management/index.php')
if not status:
	print msg
	exit()

status,msg = this.login('fog','password')
if not status:
	print msg
	exit()

status, msg = this.upload('ClientWin1')
if not status:
	print msg
	exit()

status, msg = this.wol('ClientWin1','2014/08/17 15:25')
if not status:
	print msg
	exit()

status, msg = this.wol('ClientWin1',)
if not status:
	print msg
	exit()	

status, msg = this.deploy('ClientWin1')
if not status:
	print msg
	exit()

status, msg = this.logout()
if not status:
	print msg
	exit()