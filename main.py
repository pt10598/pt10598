from flask import Flask, request, render_template, redirect, url_for
from flask import Flask
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
app = Flask(__name__)

@app.route('/')
def formPage():
    return "TEST"


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)