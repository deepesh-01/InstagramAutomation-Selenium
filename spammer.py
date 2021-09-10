user_id = str(input("Enter your instagram id : "))
user_password = str(input("Enter your password : "))
target_id = str(input("Enter target id : "))
msg = str(input("Enter message you want to send : "))
no_of_times = int(input("Enter the no of times you wnat message to be sent : "))


from selenium import webdriver
driver = webdriver.Chrome()
import time




driver.get("https://www.instagram.com")
time.sleep(1)
id = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
id.send_keys(user_id)
password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys(user_password)
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
login.click()
time.sleep(1)

try :
    max_lim = driver.find_element_by_xpath('//*[@id="slfErrorAlert"]')
    print("YOU HAVE MAXED LOGIN ATTEMPTS  PLEASE WAIT")
except :
    time.sleep(3)

    nnow = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
    if(nnow):
        nnow.click()

    time.sleep(3)

    turn_on_post_noti = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
    if(turn_on_post_noti):
        turn_on_post_noti.click()

    time.sleep(3)

search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys(target_id)
time.sleep(3)

target = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
target.click()
time.sleep(5)

message_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
message_box.click()
time.sleep(3)

chat_box = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

for a in range(no_of_times):
    chat_box.send_keys(msg)
    send_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
    send_button.click()
    time.sleep(1)

driver.close()

print("Program Ended successfully")

