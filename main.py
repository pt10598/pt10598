from flask import Flask
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
app = Flask(__name__)
chrome_options=Options()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(options=chrome_options)
driver.get("https:pay.taipei/v2/CheckBill/Index/2")

time.sleep(0.5)
serc2 = driver.find_element("name", "parameter2")
serc2.send_keys("AKL-9969")
time.sleep(0.5)
serc3=driver.find_element("xpath", '/html/body/article/main/form/div[3]/button')
serc3.click()
time.sleep(0.5)
serc4=driver.find_element("xpath", '/html/body/article/main/form/section/div[4]/button')
serc4.click()
time.sleep(0.5)
serc5=driver.find_element("xpath", '/html/body/article/main/form[1]/div[1]/div/span[2]')
print(serc5.text)

@app.route("/")
def home():
    return "<title>查詢</title>" \
           f"<p>金額{serc5.text}元<p1>"\

app.run(host="0.0.0.0",port=5000)