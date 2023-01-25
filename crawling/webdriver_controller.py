from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def run_webdriver(keyword):
    # selenium 참조 : https://coding-kindergarten.tistory.com/151
    # scheduler 참조 : https://coding-kindergarten.tistory.com/164

    # chromium in ubuntu 사용시
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("headless")
    driver_options.add_argument("--no-sandbox")
    driver_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options=driver_options)

    # for windows - chrome
    # driver = webdriver.Chrome() # webDriver = webdriver.Chrome(options=WEBDRIVER_OPTIONS, executable_path=WEBDRIVER_PATH)

    # 쿠팡 selenium crawling 방지 해제
    # driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})

    naver = "https://www.naver.com/"
    driver.get(naver)
    time.sleep(3)

    # 검색어 창을 찾아 search 변수에 저장 (css_selector 이용방식) (아래 세가지 모두 동작)
    search_box = driver.find_element(By.CSS_SELECTOR, "#query")
    # (구글 검색의 또다른 input)
    # search_box = driver.find_element(By.CSS_SELECTOR, 'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
    # search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    time.sleep(1)

    print(driver.window_handles)

    tab_css_selector = "#lnb > div.lnb_group > div > ul > li:nth-child(8) > a"
    for i in range(1, 10):
        tab_css_selector = "#lnb > div.lnb_group > div > ul > li:nth-child(%s) > a" % str(i)
        tab = driver.find_element(By.CSS_SELECTOR, tab_css_selector)
        if tab.text == "뉴스":
            tab.click()
            break

    time.sleep(2)

    click_option = driver.find_element(By.CSS_SELECTOR, "#snb > div.api_group_option_filter._search_option_simple_wrap > div > div.option_filter > a")
    click_option.click()
    time.sleep(1)

    click_1day = driver.find_element(By.CSS_SELECTOR, "#snb > div.api_group_option_sort._search_option_detail_wrap > ul > li.bx.term > div > div.option > a:nth-child(3)")
    click_1day.click()
    time.sleep(1)

    result = {
        "date": time.strftime("%Y-%m-%d", time.localtime(time.time())),
        "keyword": keyword,
        "news": []
    }

    news_page_list = driver.find_elements(By.CSS_SELECTOR, "a.info")

    if len(news_page_list) != 0:
        for article in news_page_list:
            if article.text == "네이버뉴스":
                article.click()
                time.sleep(3)

                driver.switch_to.window(driver.window_handles[1])

                try:
                    title = driver.find_element(
                        By.CSS_SELECTOR, "#title_area"
                    ).text
                except:
                    try:
                        title = driver.find_element(
                            By.CSS_SELECTOR, "h2.end_tit"
                        ).text
                    except:
                        title = driver.find_element(
                            By.CSS_SELECTOR, "h4.title"
                        ).text

                try:
                    media = driver.find_element(
                        By.CSS_SELECTOR,
                        "em.media_end_linked_more_point"
                    ).text
                except:
                    try:
                        media = driver.find_element(
                            By.CSS_SELECTOR,
                            "#link_news > h3"
                        ).text.split(" ")[0]
                    except:
                        media = driver.find_element(
                            By.CSS_SELECTOR,
                            "p.source"
                        ).text.split(" ")[1]

                try:
                    contents = driver.find_element(
                        By.CSS_SELECTOR,
                        "div#dic_area.go_trans._article_content"
                    ).text
                except:
                    try:
                        contents = driver.find_element(
                            By.CSS_SELECTOR,
                            "div#articeBody.article_body.font1.size3"
                        ).text
                    except:
                        contents = driver.find_element(
                            By.CSS_SELECTOR,
                            "div#newsEndContents.news_end.font1.size3"
                        ).text

                article_piece = {
                    "title": title,
                    "media": media,
                    "link": driver.current_url,
                    "contents": contents
                }
                result["news"].append(article_piece)

                print(article_piece["title"])
                time.sleep(2)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(2)

    return result




