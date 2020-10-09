import selenium.webdriver
dirves=selenium.webdriver.Chrome(r"D:\chromedriver.exe")
dirves.get(r"http://192.168.2.16:8089/ZHYW//res/mainui/page/index.html?fromForm=a8login")
user_name=dirves.find_element_by_id("user")