import time
# import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from handle_chart import SkuChart
# print(sys.argv[1])
sku_chart = SkuChart('1FR-2669SKU-BBK0718.xlsx')

options = webdriver.ChromeOptions()
# 设置浏览器不会关闭
options.add_experimental_option('detach', True)

# 打开浏览器
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.amazon.fr')
time.sleep(1)

# 修改归属地
driver.find_element(by=By.ID, value='nav-global-location-popover-link').click()
time.sleep(1)
driver.find_element(by=By.ID, value='GLUXZipUpdateInput').send_keys('42500')
time.sleep(1)
driver.find_element(by=By.XPATH, value="//span[@id='GLUXZipUpdate']/span/input").click()
time.sleep(2)

sku_asin = {}
sku_title = {}
# sku_list = ['8719883709475', '8718475885344', '8718475885351']
count = 0
for sku in sku_chart.get_ean_list():
# for sku in sku_list:
    # 搜索商品
    driver.find_element(by=By.ID, value='twotabsearchtextbox').clear()
    driver.find_element(by=By.ID, value='twotabsearchtextbox').send_keys(str(sku))
    time.sleep(1)
    driver.find_element(by=By.ID, value='nav-search-submit-button').click()
    time.sleep(1)
    # 获取asin
    asin = driver.find_element(by=By.XPATH, value="//div[@class='s-main-slot s-result-list s-search-results sg-row']/div[2]").get_attribute('data-asin')
    title = ''
    try:
        title = driver.find_element(by=By.XPATH, value="//div[@class='s-main-slot s-result-list s-search-results sg-row']/div[2]/div/div/div/div/div[2]/div/h2/a/span").text
    except Exception as e:
        print(e)
    print(asin)
    print(title)
    sku_asin.setdefault(sku, asin)
    sku_title.setdefault(sku, title)
    count += 1
    if count > 0 and count % 300 == 0:
        sku_chart.handle_asin_chart(sku_asin, sku_title)
sku_chart.handle_asin_chart(sku_asin, sku_title)