import requests as req
from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from random import choice, randint
import os
from tqdm.auto import tqdm
import shutil
from getpass import getpass
import platform
columns = shutil.get_terminal_size().columns


uagent = [
			'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/79.0.3945.73 Mobile/15E148 Safari/605.1',
			'Mozilla/5.0 (Linux; Android 8.0.0;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36',
			'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
			'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36', ##
			'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/72.0',
			'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/72.0',
			'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/72.0',
			'Mozilla/5.0 (Android 8.0.0; Mobile; rv:61.0) Gecko/61.0 Firefox/68.0',
			'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/21.0 Mobile/16B92 Safari/605.1.15'
		 ]
headers = {'User-Agent':choice(uagent)}


class color:

    # LIGHTBLACK_EX   = 90
    # LIGHTRED_EX     = 91
    # LIGHTGREEN_EX   = 92
    # LIGHTYELLOW_EX  = 93
    # LIGHTBLUE_EX    = 94
    # LIGHTMAGENTA_EX = 95
    # LIGHTCYAN_EX    = 96
    # LIGHTWHITE_EX   = 97

	def reset(self):
		return '\033[0m'

	def red(self):
		return '\033[91m'

	def green(self):
		return '\033[92m'

	def yellow(self):
		return '\033[93m'

	def blue(self):
		return '\033[94m'

	def magenta(self):
		return '\033[95m'

	def cyan(self):
		return '\033[96m'

	def white(self):
		return '\033[97m'

def ps(alf):
	for k in alf:
		time.sleep(0.03)
		print(k,end='',flush=True)

def colors(color):
	if platform.system() == 'Linux':
		print(color,end='')
	else:
		pass
	return ''

class mega_insta:

	def __init__(self):
		global driver,uname,url,fore
		fore = color()
		opt = Options()
		opt.add_argument('--incognito')
		opt.add_argument('--headless')
		loc = 'drivers/chromedriver'
		ps('Input Username : ')
		uname = str(input('%s@'%(colors(fore.cyan()))))
		print()
		url = 'https://www.instagram.com/%s'%(uname)

		driver = wd.Chrome(loc,options=opt)
		driver.get(url)
		time.sleep(3)
		try:
			ko = driver.find_element_by_xpath('//*[@id="main-message"]/h1/span').text
			if 'No internet' in ko:
				print('Check Your Connection And Try Again!')
				driver.quit()
				exit()
		except:
			try:
				ko = driver.find_element_by_xpath('//*[@id="main-message"]/h1/span').text
				if 'This site can’t be reached' in ko:
					driver.refresh()
			except:
				pass



	def is_private(self):
		driver.get(url)
		time.sleep(2)
		try:
			ment = driver.find_element_by_class_name('rkEop').text
			if 'This Account is Private' in ment:
				return 'Yes'
		except:
			return 'No'
		

	def login(self):
		login_url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
		driver.implicitly_wait(30)
		driver.get(login_url)

		while True:
			ps('%s ↳ Your Username : '%(colors(fore.yellow()))) #
			uname = str(input('%s'%(colors(fore.cyan()))))
			ps('%s   Your Password : '%(colors(fore.yellow()))) #
			passw = getpass('')
			elem = driver.find_element_by_xpath('//input[@name="username"]')
			elem.send_keys(uname)
			elem = driver.find_element_by_xpath('//input[@name="password"]')
			elem.send_keys(passw)
			elem.send_keys(Keys.RETURN)
			time.sleep(1.5)
			try:
				check = driver.find_element_by_id('slfErrorAlert').text
				if "username you entered doesn't belong" in check:
					ps('%s   ↳ [×] account not found, try again!\n'%(colors(fore.red())))
				elif 'your password was incorrect.' in check:
					ps('%s   ↳ [×] password incorrect, try again!\n'%(colors(fore.red())))
				driver.refresh()
				time.sleep(1.5)
			except:
				ps('%s   ↳ [ ✓ ] Login Success\n'%(colors(fore.green())))
				break
		driver.get(url)

	def account_info(self):
		global info
		x = driver.find_elements_by_class_name('g47SY')
		info = []
		for k in x:
			info.append(k.text)
		try:
			ment = driver.find_element_by_class_name('rkEop').text
			if 'This Account is Private' in ment:
				info.append('Yes')
			else:
				info.append('Yes')
		except:
			info.append('No')
		return info

	def scrool(self):
		for i in range(1):
		    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		    time.sleep(2)

	def get_link(self,file,amount):
		global alinks
		alf = []
		alinks = []
		i = 1
		driver.execute_script('window.open("https://www.instagram.com"), "new window"')
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(3)
		last_height = driver.execute_script("return document.body.scrollHeight")

		while True:
			alf1 = []
			elem = driver.find_elements_by_tag_name('a')
			for data in elem:
				data = data.get_attribute('href')
				if '/p/' in data and data[25:] not in alf:
					fix = data[25:]
					alf.append(fix)
					alf1.append(fix)
			driver.switch_to.window(driver.window_handles[1])
			for data in alf1:
				push = 'https://www.instagram.com%s?__a=1'%(data)
				driver.get(push)
				time.sleep(0.5)
				elem = driver.find_element_by_tag_name('pre').text
				if file == 1:
					cut = '"display_url":"'
					dif = '"video_url":"'
				elif file == 2:
					cut = '"video_url":"'
					if cut not in elem:
						continue
				dump = elem.split('"__typename":"')[1:]
				for part in dump:
					slash = part.split('"')[0]
					if file == 1 and 'GraphVideo' in slash:
						continue
					elif file == 2 and 'GraphVideo' not in slash:
						continue
					base = part.split(cut)[1].split('"')[0]
					
					if base not in alinks:
						alinks.append(base)
						if amount >= 9999:
							ps('%s/All '%(i))
						else:
							ps('%s/%s '%(i,amount))
						i+=1
					if len(alinks) == amount:
						break
				if len(alinks) == amount:
					break
			if len(alinks) == amount:
				driver.quit()
				break
			else:
				driver.switch_to.window(driver.window_handles[0])
				self.scrool()
				new_height = driver.execute_script("return document.body.scrollHeight")
				if last_height == new_height:
					driver.quit()
					break
				last_height = new_height
		print()
		return alinks

	def mkdirs(self,tipe):
		global fold
		if tipe == 1:
			fold = 'Picture'
		elif tipe == 2:
			fold = 'Video'
		try:
			os.mkdir('mega-insta')
			os.mkdir('mega-insta/%s'%(uname))
			os.mkdir('mega-insta/%s/%s'%(uname,fold))
		except:
			try:
				try:
					os.mkdir('mega-insta/%s'%(uname))
					os.mkdir('mega-insta/%s/%s'%(uname,fold))
				except:
					os.mkdir('mega-insta/%s/%s'%(uname,fold))
			except:
				pass
				

	def save(self,tipe):
		self.mkdirs(tipe)
		same = []
		if tipe == 1:
			ex = '.jpg'
		elif tipe == 2:
			ex = '.mp4'
		i = 1
		for i in tqdm(range(len(alinks)),desc='Downloading',unit_scale=True):
			dl = req.get(alinks[i],headers=headers).content
			rename = alinks[i].split('=')[-1:][0]+ex
			if dl not in same:
				same.append(dl)
				with open('mega-insta/%s/%s/%s'%(uname,fold,rename),'wb+') as f:
					f.write(dl)
					f.close()
		print()

	def quit(self):
		driver.quit()

	def get(self,link):
		driver.get(link)

def main():

	fore = color()
	print(colors(fore.yellow()))
	print('| [mega-insta] - Instagram Scraper |'.center(columns,'-'))
	print()
	alfa = mega_insta()
	alfa.account_info()
	print(colors(fore.yellow()),end='')
	print(' [Account Info] '.center(columns,'-'))
	print(colors(fore.cyan()),end='')
	ps('username  : @%s\n'%(uname))
	ps('posts     : %s\n'%(info[0]))
	ps('followers : %s\n'%(info[1]))
	ps('following : %s\n'%(info[2]))
	ps('private   : %s\n'%(info[3]))

	try : 
		if info[3] == 'Yes':
			print('%s↳ [!] Account Is Private, Please Login For Next Step!'%(colors(fore.red())))
			print(colors(fore.yellow()),end='')
			print(' [Login] '.center(columns,'-'))
			alfa.login()
			if alfa.is_private() == 'Yes':
				print('%s ↳ You Must Accepted By Owner First'%(colors(fore.red())))
				alfa.quit()
				exit()
			print()
		print(colors(fore.yellow()),end='')
		print(' [Menu] '.center(columns,'-')+'\n')
		print('1. Download Image | 2. Download Video'.center(columns))

		ps('Choice : ')
		tipe = int(input('%s'%(colors(fore.cyan()))))
		if tipe < 1 or tipe > 2:
			ps('Just 1 or 2!%s\n'%(colors(fore.red())))
			alfa.quit()
			exit()

		ps('%s ↳ Amount (all = 99999) : '%(colors(fore.yellow())))
		n = int(input('%s'%(colors(fore.cyan()))))
		print()

		ps(colors(fore.yellow()))
		print(' [Scanning Profile] '.center(columns,'-')+'\n')

		ps(colors(fore.cyan()))
		alfa.get_link(tipe,n)
		
		print('\nFound %s Images\n'%(len(alinks)))
		
		ps(colors(fore.yellow()))
		print(' [Downloading] '.center(columns,'-'))
		ps(colors(fore.cyan())+'\n')
		
		time.sleep(2)
		alfa.save(tipe)

		ps(colors(fore.green()))
		print(' [RAMPUNG LURRRR] '.center(columns,'-'))
		ps(colors(fore.reset()))
		print()

	except req.exceptions.ConnectionError:
		print('Connection Error! Try Again')

if __name__  == '__main__':
	main()
