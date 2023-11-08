import os
from subprocess import STDOUT, check_output
from pathlib import Path
from zipfile import ZipFile 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def execute_command(cmd):
    output = check_output(cmd, stderr=STDOUT, timeout=15)
    print("execute command success")
    return output.decode('ascii')
    
if not Path("/tmp/headless-chromium").is_file():
    # loading the temp.zip and creating a zip object 
    with ZipFile("./binaries/headless-chromium.zip", 'r') as zObject: 
        zObject.extractall(path="/tmp/") 
    execute_command(["chmod",
                     "777",
                     "/tmp/headless-chromium",])

if not Path("/tmp/chromedriver").is_file():    
    os.system("cp ./binaries/chromedriver /tmp/chromedriver")
    execute_command(["chmod",
                     "777",
                     "/tmp/chromedriver",
                     ])
    
os.system("cp -R ./lib/* /tmp/")

def handler(event, context):
    options = Options()
    options.page_load_strategy = 'normal'
    options.binary_location = '/tmp/headless-chromium'
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--no-sandbox")
    options.add_argument("--no-zygote")
    options.add_argument("--disable-gpu")
    options.add_argument("--single-process")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")

    service = Service(
                      executable_path="/tmp/chromedriver",
                      log_output=STDOUT,
                      service_args=["--verbose"],
                      )

    driver = webdriver.Chrome(service=service, options=options)

    driver.get('https://www.google.cl')
    body = f"Headless Chrome Initialized, Page title: {driver.title}"

    driver.close()
    driver.quit()

    response = {
        "statusCode": 200,
        "body": body,
    }

    return response