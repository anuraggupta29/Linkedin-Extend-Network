# connect python with webbrowser-chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def login():
	global driver

	try:
		driver.find_element_by_class_name("nav__button-secondary").click()
		time.sleep(3)
		username = driver.find_element_by_id("username") # Getting the login element
		username.send_keys("anuraggupta29@outlook.com") # Sending the keys for username
		password = driver.find_element_by_id("password") # Getting the password element
		password.send_keys("Agrox29@arun") # Sending the keys for password
		driver.find_element_by_class_name("btn__primary--large").click() # Getting the tag for submit button

	except:
		username = driver.find_element_by_id("session_key") # Getting the login element
		username.send_keys("anuraggupta29@outlook.com") # Sending the keys for username
		password = driver.find_element_by_id("session_password") # Getting the password element
		password.send_keys("Agrox29@arun") # Sending the keys for password
		driver.find_element_by_class_name("sign-in-form__submit-button").click() # Getting the tag for submit button

def goto_network():
	global driver
	time.sleep(7)
	driver.find_element_by_id("ember23").click()

def send_requests():
	global driver
	global current_count

	# Number of requests you want to send
	permission = input('Start sending Requests? (y/n) : ')

	n = int(input("Number of requests to send : "))

	while current_count != n:
		connectButtons = driver.find_elements_by_css_selector('button[data-control-name="people_connect"]')
		inviteButtons = driver.find_elements_by_css_selector('button[data-control-name="invite"]')
		allButtons = connectButtons + inviteButtons

		for btn in allButtons:
			if current_count == n:
				break
			try:
                btn.click()
                current_count += 1
            except:
                pass

		print('Connection requests sent : {}/{}'.format(current_count, n))
		print()

		driver.execute_script("window.scrollBy(0, 3000)")
		time.sleep(3)

	print("Finshed")

def main():
	global driver

	# url of LinkedIn
	url = "http://linkedin.com/"

	# url of LinkedIn network page
	network_url = "https://www.linkedin.com/login"

	# path to browser web driver
	print('Opening Linkedin sign in page...')
	driver.get(url)

	print('Signing in...')
	login()
	print('Opening network page...')
	goto_network()
	print()
	send_requests()

# Driver's code
if __name__ == '__main__':
	driver = webdriver.Chrome('chromedriver.exe')
	current_count = 0
	main()

"""
entityBoxes = driver.find_elements_by_class_name("discover-entity-type-card")
connectBtn1 = entity.find_element_by_css_selector('button[data-control-name="people_connect"]')
connectBtn2 = entity.find_element_by_css_selector('button[data-control-name="invite"]')
mutual = entity.find_element_by_class_name('member-insights__reason').text
headline = entity.find_element_by_class_name('discover-person-card__occupation').text
"""
