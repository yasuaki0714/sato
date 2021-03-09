#スクレイピングに必要なモジュール
import requests
from bs4 import BeautifulSoup
#モジュールインポート
import sitelist

import time #sleep用
import sys  #エラー検知用
import re   #正規表現
import csv  #csv操作
import numpy    #csv操作

with open('result.csv', 'a', encoding="utf_8_sig") as csv_file:
    fieldnames = ['result', 'Rank', 'Waku', 'Horse_Name', 'Course', 'Distance', 'Ninki']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

for scraping_sitename in sitelist.SITE_URL:

    #攻撃とみなされないように時間を置く
    time.sleep(3)
    try:
        # スクレイピング対象の URL にリクエストを送り HTML を取得する
        res = requests.get(scraping_sitename)

        res.raise_for_status()  #URLが正しくない場合，例外を発生させる

        # レスポンスの HTML から BeautifulSoup オブジェクトを作る
        soup = BeautifulSoup(res.content, 'html.parser')

        # title タグの文字列を取得する
        title_text = soup.find('title').get_text()
        print(title_text)

        #順位のリスト作成
        Ranks = soup.find_all('div', class_='Rank')
        Ranks_list = []
        for Rank in Ranks:
            Rank = Rank.get_text()
            #リスト作成
            Ranks_list.append(Rank)
        print(Ranks_list)   #debug

        #馬名取得
        Horse_Names = soup.find_all('span', class_='Horse_Name')
        Horse_Names_list = []
        for Horse_Name in Horse_Names:
            #馬名のみ取得(lstrip()先頭の空白削除，rstrip()改行削除)
            Horse_Name = Horse_Name.get_text().lstrip().rstrip('\n')
            #リスト作成
            Horse_Names_list.append(Horse_Name)
        print(Horse_Names_list) #debug

        #人気取得
        Ninkis = soup.find_all('span', class_='OddsPeople')
        Ninkis_list = []
        for Ninki in Ninkis:
            Ninki = Ninki.get_text()
            #リスト作成
            Ninkis_list.append(Ninki)
        print(Ninkis_list)  #debug

        #枠取得
        Wakus = soup.find_all('td', class_=re.compile("Num Waku"))
        Wakus_list = []
        for Waku in Wakus:
            Waku = Waku.get_text().replace('\n','')
            #リスト作成
            Wakus_list.append(Waku)
        print(Wakus_list)

        #コース,距離取得
        Distance_Course = soup.find_all('span')
        Distance_Course = re.search(r'.[0-9]+m', str(Distance_Course))
        Course = Distance_Course.group()[0]
        Distance = re.sub("\\D", "", Distance_Course.group())
        print(Course)   #debug
        print(Distance) #debug

        with open('result.csv', 'a', encoding="utf_8_sig") as csv_file:
            fieldnames = ['result', 'Rank', 'Waku', 'Horse_Name', 'Course', 'Distance', 'Ninki']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            #writer.writeheader()
            #順位-馬名-人気のリスト作成(CSVへ書き込み)
            for Rank_list, Waku_list, Horse_Name_list, Ninki_list in zip(Ranks_list, Wakus_list, Horse_Names_list, Ninkis_list):
                #3位以内に入ったなら正解ラベル(result = 1)を振る
                if Rank_list == "1" or Rank_list == "2" or Rank_list == "3":
                    result = 1
                else:
                    result = 0
                print(result, Rank_list, Waku_list, Horse_Name_list, Course, Distance, Ninki_list)
                writer.writerow({'result': result, 'Rank': Rank_list, 'Waku': Waku_list, 'Horse_Name': Horse_Name_list, 'Course': Course, 'Distance': Distance, 'Ninki': Ninki_list})


    except:
        print(sys.exc_info())
        print("サイト取得エラー")