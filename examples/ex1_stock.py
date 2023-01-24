from urllib.request import urlopen
from bs4 import BeautifulSoup
from pymongo import MongoClient

def stock_crawling(code):
    root_url = "https://finance.naver.com/item/main.naver?code="
    url = root_url + code  # 삼성전자
    html = urlopen(url)
    bs_obj = BeautifulSoup(html, "html.parser", from_encoding="cp949")
    print(bs_obj)

    date1 = bs_obj.find("em", {"class":"date"})
    # print(type(date1))
    # print(date1.text)
    # print(type(date1.text))

    try:
        date = date1.text.replace('.', '/').split()
        date = date[0]
        # print(date)

    except:
        print("해당 코드로 종목찾기에 실패하였습니다. 입력코드를 재확인 해주시기 바랍니다.")
        return {"code": "None"}

    table1 = bs_obj.find("div", {"class":"rate_info"})
    table1 = table1.text.split()
    # print(table1)

    corp_name = table1[0]
    cur_price = int(table1[2].replace(',', ''))

    try:
        prv_price = int(table1[23].replace(',', ''))
        highest_price = int(table1[26][0:len(table1[26])//2].replace(',', ''))
        lowest_price = int(table1[36][0:len(table1[36])//2].replace(',', ''))

    except:
        prv_price = int(table1[21].replace(',', ''))
        highest_price = int(table1[24][0:len(table1[24])//2].replace(',', ''))
        lowest_price = int(table1[34][0:len(table1[34])//2].replace(',', ''))

    # print(lowest_price)

    table2 = bs_obj.find("div", {"class":"aside_invest_info"}).text.split()
    # print(table2)

    try:
        total_stocks = int(table2[12].replace(',', ''))
        fgn_owned = int(table2[21].replace(',', ''))

    except:
        total_stocks = int(table2[11].replace(',', ''))
        fgn_owned = int(table2[20].replace(',', ''))

    # fgn_own_ratio = float(fgn_own) / float(total_stocks)
    # print("외국인 보유 비율: %.2f %%" % (fgn_own_ratio * 100 ))

    # print(per, pbr)

    total_info = {
        "code": code,
        "corp name": corp_name,
        "date": date,
        "privous price": prv_price,
        "current price": cur_price,
        "highest price": highest_price,
        "lowest price": lowest_price,
        "total stocks": total_stocks,
        "foreign owned": fgn_owned,
    }

    return total_info

def code_input():
    while True:
        print("종목 코드 6자리를 입력해주시기 바랍니다. (ex. 삼성전자 : 005930)")

        try:
            code = str(input()).replace('[', '').replace("'", "").replace(']', '')

            if len(code) != 6:
                print("유효하지 않은 입력입니다. 다시 시도해 주십시오")
            else:
                return code

        except Exception as e:
            print("유효햐지 않은 입력입니다. 다시 시도해 주십시오")

def input_email():
    while True:
        print("자료를 받으실 메일 주소를 입력해 주십시오.")
        email = input()
        print("입력하신 메일 주소 : ", email)
        print("맞으면 y 틀리면 아무키나 눌러주십시오")
        confirm = input()
        if confirm == 'y' or confirm == 'Y':
           return email

def mongodb(email, total_info):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["py"]





if __name__ == "__main__":
    while True:
        print("원하시는 서비스 번호를 선택해 주십시오")
        print("1. 서비스 받을 메일 주소 입력    0. 서비스 종료")
        order1 = input()
        if order1 == '1':
            email = input_email()

            while True:
                print("원하시는 서비스 번호를 선택해 주십시오")
                print("1. 종목 추가    2. 종목 삭제    3. 해당 e-mail 서비스 삭제    0. 전단계")

                order2 = input()
                if order2 == '1':
                    code = code_input()
                    total_info = stock_crawling(code)
                    print(total_info)

                elif order2 == '2':
                    code = code_input()

                elif order2 == '3':
                    continue

                elif order2 == '0':
                    break
                else:
                    print("유효하지 않은 키를 입력하셨습니다.")

        elif order1 == '0':
            print("서비스를 종료 합니다.")
            exit(0)

        else:
            print("유효하지 않은 키를 입력하셨습니다.")



