# Section02-3
# 파이썬 크롤링 기초
# lxml 사용 기초 스크랩핑(1)
# 초기 설치
# pip install lxml
# pip install requests
# pip install cssselect
# https://www.w3schools.com/cssref/trysel.asp

import requests
import lxml.html
from requests.models import Response


def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인함수
    """

    # 스크랩핑 대상 URL
    response = requests.get("https://www.naver.com")  # get, post

    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)

    # 결과 출력
    for url in urls:
        #  url 출력
        print(url)


def scrape_news_list_page(response):
    # URL 리스트 선언
    urls = []

    # 태그 정보 문자열 저장
    # print(response.content)
    root = lxml.html.fromstring(response.content)
    # print(root)  # 출력값 <Element html at 0x2447fe24c70>

    for a in root.cssselect('.thumb_box > .popup_wrap > a.btn_popup'):
       # 링크
        url = a.get('href')
        # class 중복으로 인한 # 제거방법
        if len(url) >= 2:
            # 리스트 삽입
            urls.append(url)
        else:
            pass
    return urls


# 스크랩핑 시작
if __name__ == "__main__":
    main()
