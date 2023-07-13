import webview, os

class Api:
	def __init__(self):
		self.cancel_heavy_stuff_flag = False

	def runner(self):
		os.system('lib\\my_rusty_program.exe')
		return {'exit': 1}

if __name__ == '__main__':
	api = Api()
	window = webview.create_window('Appity', 'lib/index.html', js_api=api)
	webview.start(user_agent='{OSGIAPPSERVICE}')
