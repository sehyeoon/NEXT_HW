from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv
from datetime import datetime
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

now = datetime.now()

# Chrome WebDriver 경로 지정
chromedriver_path = 'C:/Users/USER/Downloads/next/chromedriver-win64/chromedriver.exe'
user_data_dir = "C:/Users/USER/Downloads/next/"

chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")
service = Service(executable_path=chromedriver_path)

# ChromeDriver에 사용자 데이터 디렉토리와 함께 옵션 전달
driver = webdriver.Chrome(service=service, options=chrome_options)

# 인스타그램 웹페이지 접속하기
driver.get('https://www.instagram.com/imwinter/followers/')
time.sleep(10)

# 팔로워 목록 가져오기
follower_list = []
for i in range(1, 11):
    xpath = f"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span"
    try:
        follower = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        follower_list.append(follower.text)
    except TimeoutException:
        print(f"Timeout occurred while waiting for follower {i}")
    
# 인스타그램 웹페이지 접속하기
driver.get('https://www.instagram.com/imwinter/following/')
time.sleep(5)

# 팔로잉 목록 가져오기
following_list = []
for i in range(1, 5):
    xpath = f"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[{i}]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span"
    try:
        following = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        following_list.append(following.text)
    except TimeoutException:
        print(f"Timeout occurred while waiting for following {i}")

# CSV 파일 경로
csv_file_path = f"{now.strftime('%Y%m%d')}_instagram.csv"

# CSV 파일 열기 및 팔로워 목록 기록
with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
    # CSV writer 생성
    csv_writer = csv.writer(csvfile)
    
    # 헤더 추가
    csv_writer.writerow(["Type", "Index", "Username"])
    
    # 모든 팔로워를 CSV 파일에 기록
    for index, follower_text in enumerate(follower_list, start=1):
        csv_writer.writerow(["Follower", index, follower_text])
        
    # 모든 팔로잉을 CSV 파일에 기록 
    for index, following_text in enumerate(following_list, start=1):
        csv_writer.writerow(["Following", index, following_text])

print("CSV 파일에 팔로워와 팔로잉 목록이 성공적으로 저장되었습니다.")

