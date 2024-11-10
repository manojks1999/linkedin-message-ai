# from linkedin_scraper import Person, actions
from linkedin_api import Linkedin
# from selenium import webdriver

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time

class LinkedIn:

    def __init__(self):
        # self.__driver = webdriver.Chrome()
        self.__email = os.environ.get('LINKEDIN_EMAIL')
        self.__password = os.environ.get('LINKEDIN_PASSWORD')

    def login(self, email, password):
        self.__linkedin = Linkedin(self.__email, self.__password)
        # actions.login(self.__driver, self.__email, self.__password)

    def get_person(self, url):
        pass
        # url = 'https://www.linkedin.com/in/manoj-k-s-bb2704182/'
        # person = Person(url, driver=driver)
        # profile = api.get_profile('manoj-k-s-bb2704182')
        # posts = api.get_user_posts('username')
        # return posts
        # options = webdriver.ChromeOptions()
        # options.add_argument("--start-maximized")  # Optional: Start maximized
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # driver.get("https://www.linkedin.com/login")
        # time.sleep(2)
        # driver.find_element(By.ID, "username").send_keys(self.__email)
        # driver.find_element(By.ID, "password").send_keys(self.__password)
        # driver.find_element(By.XPATH, "//button[text()='Sign in']").click()
        # time.sleep(5)
        # driver.get("https://www.linkedin.com/in/manoj-k-s-bb2704182/")
        # time.sleep(3)
        # try:
        #     profile_name = driver.find_element(By.CLASS_NAME, "text-heading-xlarge").text
        #     print(f"Profile Name: {profile_name}")
        # except Exception as e:
        #     print(f"Error: {e}")
        
        # posts = driver.find_elements(By.XPATH, "//div[contains(@class, 'feed-shared-update-v2')]")
        # for post in posts:
        #     try:
        #         post_content = post.find_element(By.XPATH, ".//span[contains(@class, 'break-words')]").text
        #         print(post_content)
        #     except Exception as e:
        #         print("Error fetching post:", e)