from flask import Flask, request, render_template, redirect, url_for
from flask import Flask
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
app = Flask(__name__)

@app.route('/')
def formPage():
    return render_template('Form.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user = request.form['user']
        tte = request.form['user2']
        tte2 = request.form['user3']
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https:pay.taipei/v2/CheckBill/Index/2")
        time.sleep(0.5)
        serc2 = driver.find_element("name", "parameter2")
        serc2.send_keys(tte2)
        time.sleep(0.5)
        serc3 = driver.find_element("xpath", '/html/body/article/main/form/div[3]/button')
        serc3.click()
        time.sleep(0.5)
        serc4 = driver.find_element("xpath", '/html/body/article/main/form/section/div[4]/button')
        serc4.click()
        time.sleep(0.5)
        serc5 = driver.find_element("xpath", '/html/body/article/main/form[1]/div[1]/div/span[2]')
        print(serc5.text)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://ppstrq.nat.gov.tw/pps/pubQuery/PropertyQuery/propertyQuery.do")
        db1 = driver.find_element("xpath", '/html/body/div[3]/div[3]/div/form/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/input[2]')
        db1.click()
        db2 = driver.find_element("xpath", '/html/body/div[3]/div[3]/div/form/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/div[3]/div/input')
        db3 = driver.find_element("xpath", '/html/body/div[3]/div[3]/div/form/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/div[4]/div/input')
        db2.send_keys(user)
        db3.send_keys(tte)
        db4 = driver.find_element("xpath", '/html/body/div[3]/div[3]/div/form/div[1]/div[1]/div/div/div[2]/div[2]/div/input[2]')
        db4.click()
        db5 = driver.find_element("xpath", '/html/body/div[3]/div[3]/div/form/div/div[3]/div/div[2]/table/caption/font/span')
        print(db5.text)

        return redirect(url_for('success', name=db5.text,serc6=serc5.text))

@app.route('/success/<name>/<serc6>/')
def success(name,serc6):
    add2=int(serc6)
    return f"<h2>{name}</h2>"\
           f"<h2>應繳金額{add2}元</h2>"\
           "<h2><input type='button' value='返回首頁' onclick='history.back()' style='width:90px;height:40px;'/></h2>"\




if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)