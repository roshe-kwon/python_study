# Section02-4
# 파이썬 크롤링 기초
# lxml 사용 기초 스크랩핑(2)

import requests
from lxml.html import fromstring, tostring
from requests.sessions import session
# import에 전체를 가져오는 것은 좋지 않다.
# fromstring : 웹에서 가져온 정보를 string으로 바꿔주는 것
# tostring : 우리가 중간에 코드를 확인할 수 있도록 바꿔주는 것


def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인 함수
    """

    # 세션 사용 권장
    session = requests.Session()

    # 스크랩핑 대상 URL
    response = session.get("https://www.naver.com")  # Get, Post

    # 신문사 링크 리스트 획득
    newspaper_name = scrape_newspaper_name(response)  # 신문사 이름
    newspaper_url = scrape_newspaper_urls(response)  # 신문사 URL

    # 딕셔너리 생성
    news_dic = {name: value for name, value in zip(
        newspaper_name, newspaper_url)}

    # 결과 출력
    for name, url in news_dic.items():
        print(name, url)


def scrape_newspaper_name(response):
    newspaper_name = []

    # 태그 정보 문자열 저장
    root = fromstring(response.content)

    # 신문사명
    for a in root.xpath('//div[@class="thumb_area"]/div[@class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"]/a[@class="thumb"]'):
        # a 구조 확인
        # print(a)

        # a 문자열 출력
        # print(tostring(a, pretty_print=True))

        name = a.xpath("./img")[0].get("alt")

        newspaper_name.append(name)

    return newspaper_name


def scrape_newspaper_urls(response):
    # URL 리스트 선언
    newspaper_urls = []
    # 태그 정보 문자열 저장
    root = fromstring(response.content)

    # 문서내 경로 절대 경로 변환
    # root.make_links_absolute(response.url)

    for a in root.cssselect('.thumb_box > .popup_wrap > a.btn_popup'):
       # 링크
        url = a.get('href')
        # class 중복으로 인한 # 제거방법
        if len(url) >= 2:
            # 리스트 삽입
            newspaper_urls.append(url)
        else:
            pass
    return newspaper_urls


# 스크랩핑 시작
if __name__ == "__main__":
    main()
