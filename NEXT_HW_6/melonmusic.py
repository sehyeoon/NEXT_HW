from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime # datetime 모듈 추가
from openpyxl import Workbook # openpyxl 모듈 추가

#원하는 url 입력
url='https://www.melon.com/new/index.htm'

try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    #응답 상태 코드 확인
    if response.status_code == 200:
        html_text = response.text
        
        #step5. beautifulsoup 패키지로 피싱 후, 'soup' 변수에 저장
        soup = bs(response.text, 'html.parser')
        
        #제목
        titles = soup.select('.ellipsis.rank01 > span > a')
        titles = [title.text.strip() for title in titles]
        print(titles)
        
        artists = soup.select('.ellipsis.rank02 > span > a')
        artists = [artist.text.strip() for artist in artists]
        print(artists)
        
        # openpyxl Workbook 객체 생성
        wb = Workbook()
        ws = wb.active
        
        # 첫 번째 행에 제목 추가
        ws.append(["번호", "제목", "아티스트"])
        
        # 데이터 쓰기
        for i, (title, artist) in enumerate(zip(titles, artists), start=1):
            ws.append([i, title, artist])
        
        # 오늘 날짜를 'YYYYMMDD' 형식으로 포맷팅
        today = datetime.now().strftime('%Y%m%d')
        
        #엑셀 파일로 저장
        filename = f'melon_chart_{today}.xlsx'
        wb.save(filename)
        print(f"엑셀 파일 저장 완료: {filename}")
        
    else:
        print(f"Error: HTTP 요청 실패. 상태 코드: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    # requests 관련 예외 처리
    print(f"Error: 요청 중 오류 발생. 오류 메세지: {e}")
    