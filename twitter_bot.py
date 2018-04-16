#-*- coding:utf-8 -*-
import twitter
import threading
import datetime
import urllib

from bs4 import BeautifulSoup

api = twitter.Api(consumer_key="your_key",
                  consumer_secret="your_secret",
                  access_token_key="your_key",
                  access_token_secret="your_secret")

link_notice = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/db.cgi?page=DBView&did=357"
link_modify_timetable = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/db.cgi?page=DBView&did=391"
link_nolec = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/db.cgi?page=DBView&did=361"
link_addlec = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/db.cgi?page=DBView&did=363"
link_call = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/db.cgi?page=DBView&did=393"
link_modifylec = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/db.cgi?page=DBView&did=364"
link_scholarship = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/db.cgi?page=DBView&did=367"
link_concentration = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/db.cgi?page=DBView&did=379"
link_aboard = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/db.cgi?page=DBView&did=372"

class Task:

    refresh_time = 30
    previous_notice_id = ""
    previous_timetable_id = ""
    previous_nolec_id = ""
    previous_addlec_id = ""
    previous_call_id = ""
    previous_scholarship_id = ""

    def __init__(self):
        pass

    def noticeTimer(self):
        print("Getting data from Internet...")
        html_doc = urllib.request.urlopen(link_notice).read()
        soup = BeautifulSoup(html_doc,'html.parser')
        title = soup.find(class_="record-value-7")
        title_text = title.text
        post_id = title.attrs['id'][15:]
        date = soup.find(class_="record-value-4").text
        faculty = soup.find(class_="record-value-109").text
        grade = soup.find(class_="record-value-111").text
        link = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/db.cgi?page=DBRecord&did=357&qid=all&vid=24&rid=" + post_id
        if post_id != self.previous_notice_id:
            post = "#Prokumaの掲示板BOT\n" + "お知らせ（学生向け） No." + str(post_id) + "\n" + str(title_text) + "\n投稿日：" + str(date) + "\n対象：" + str(faculty) + str(grade) + "\n" + str(link)
            status = api.PostUpdate(post)
            self.previous_notice_id = post_id
        threading.Timer(self.refresh_time, self.noticeTimer).start()

    def timetableTimer(self):
        print("Getting data from Internet...")
        html_doc = urllib.request.urlopen(link_modify_timetable).read()
        soup = BeautifulSoup(html_doc,'html.parser')
        title = soup.find(class_="record-value-116")
        title_text = title.text
        post_id = title.attrs['id'][17:]
        subject = soup.find(class_="record-value-203").text
        professor = soup.find(class_="record-value-204").text
        date = soup.find(class_="record-value-4").text
        time = soup.find(class_="record-value-200").text
        type_notice = soup.find(class_="record-value-201").text
        before = soup.find(class_="record-value-205").text
        after = soup.find(class_="record-value-206").text
        faculty = soup.find(class_="record-value-6").text
        grade = soup.find(class_="record-value-109").text
        link = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/db.cgi?page=DBRecord&did=391&qid=all&vid=24&rid=" + post_id
        if post_id != self.previous_timetable_id:
            post = "#Prokumaの掲示板BOT\n" + "時間割・講義室変更 No." + str(post_id) + "\n" + str(title_text) + "\n科目：" + str(subject) + "\n担当教員：" + str(professor) + "\n変更日：" + str(date) + str(time) + "\n対象：" + str(faculty) + str(grade) + "\n変更以前：" + str(before) + "\n変更以降：" + str(after) + "\n" + str(link)
            status = api.PostUpdate(post)
            self.previous_timetable_id = post_id
        threading.Timer(self.refresh_time, self.timetableTimer).start()

    def nolecTimer(self):
        print("Getting data from Internet...")
        html_doc = urllib.request.urlopen(link_nolec).read()
        soup = BeautifulSoup(html_doc,'html.parser')
        title = soup.find(class_="record-value-7")
        title_text = title.text
        time = soup.find(class_="record-value-94").text
        professor = soup.find(class_="record-value-8").text
        post_id = title.attrs['id'][15:]
        date = soup.find(class_="record-value-4").text
        faculty = soup.find(class_="record-value-109").text
        grade = soup.find(class_="record-value-111").text
        link = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/db.cgi?page=DBRecord&did=361&qid=all&vid=24&rid=" + post_id
        if post_id != self.previous_nolec_id:
            post = "#Prokumaの掲示板BOT\n" + "休講通知 No." + str(post_id) + "\n科目：" + str(title_text) + "\n担当教員：" + str(professor) + "\n休講日：" + str(date) + str(time) + "\n対象：" + str(faculty) + str(grade) + "\n" + str(link)
            status = api.PostUpdate(post)
            self.previous_nolec_id = post_id
        threading.Timer(self.refresh_time, self.nolecTimer).start()

    def addlecTimer(self):
        print("Getting data from Internet...")
        html_doc = urllib.request.urlopen(link_addlec).read()
        soup = BeautifulSoup(html_doc,'html.parser')
        title = soup.find(class_="record-value-7")
        title_text = title.text
        time = soup.find(class_="record-value-94").text
        professor = soup.find(class_="record-value-8").text
        post_id = title.attrs['id'][15:]
        date = soup.find(class_="record-value-4").text
        faculty = soup.find(class_="record-value-109").text
        grade = soup.find(class_="record-value-111").text
        link = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/db.cgi?page=DBRecord&did=363&qid=all&vid=24&rid=" + post_id + "&Head=&hid=&sid=n&rev=0&ssid=3-2490-3953-g31"
        if post_id != self.previous_addlec_id:
            post = "#Prokumaの掲示板BOT\n" + "補講通知 No." + str(post_id) + "\n科目：" + str(title_text) + "\n担当教員：" + str(professor) + "\n補講日：" + str(date) + str(time) + "\n対象：" + str(faculty) + str(grade) + "\n" + str(link)
            status = api.PostUpdate(post)
            self.previous_addlec_id = post_id
        threading.Timer(self.refresh_time, self.addlecTimer).start()

    def callTimer(self):
        print("Getting data from Internet...")
        html_doc = urllib.request.urlopen(link_call).read()
        soup = BeautifulSoup(html_doc,'html.parser')
        title = soup.find(class_="record-value-7")
        title_text = title.text
        post_id = title.attrs['id'][15:]
        date = soup.find(class_="record-value-4").text
        faculty = soup.find(class_="record-value-109").text
        grade = soup.find(class_="record-value-119").text
        link = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/db.cgi?page=DBRecord&did=393&qid=all&vid=24&rid=" + post_id
        if post_id != self.previous_call_id:
            post = "#Prokumaの掲示板BOT\n" + "学生呼出 No." + str(post_id) + "\n作件：" + str(title_text) + "\n学科：" + str(faculty) + "\n投稿日：" + str(date) + "\n対象：" + str(grade) + "\n" + str(link)
            status = api.PostUpdate(post)
            self.previous_call_id = post_id
        threading.Timer(self.refresh_time, self.callTimer).start()
        
    def scholarshipTimer(self):
        print("Getting data from Internet...")
        html_doc = urllib.request.urlopen(link_scholarship).read()
        soup = BeautifulSoup(html_doc,'html.parser')
        title = soup.find(class_="record-value-7")
        title_text = title.text
        post_id = title.attrs['id'][15:]
        type_scholarship = soup.find(class_="record-value-6").text
        link = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/db.cgi?page=DBRecord&did=393&qid=all&vid=24&rid=" + post_id
        if post_id != self.previous_scholarship_id:
            post = "#Prokumaの掲示板BOT\n" + "奨学金 No." + str(post_id) + "\n作件：" + str(title_text) + "\n種別：" + str(type_scholarship) + "\n" + str(link)
            status = api.PostUpdate(post)
            self.previous_scholarship_id = post_id
        threading.Timer(self.refresh_time, self.scholarshipTimer).start()

    def concentrationTimer(self):
        print("Getting data from Internet...")
        html_doc = urllib.request.urlopen(link_concentration).read()
        soup = BeautifulSoup(html_doc,'html.parser')
        title = soup.find(class_="record-value-7")
        title_text = title.text
        post_id = title.attrs['id'][15:]
        date = soup.find(class_="record-value-4")
        link = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/db.cgi?page=DBRecord&did=379&qid=all&vid=24&rid=" + post_id
        if post_id != self.previous_scholarship_id:
            post = "#Prokumaの掲示板BOT\n" + "集中講義 No." + str(post_id) + "\n" + str(title_text) + "\n日付：" + str(date) + "\n" + str(link)
            status = api.PostUpdate(post)
            self.previous_scholarship_id = post_id
        threading.Timer(self.refresh_time, self.scholarshipTimer).start()

    def aboardTimer(self):
        print("Getting data from Internet...")
        html_doc = urllib.request.urlopen(link_aboard).read()
        soup = BeautifulSoup(html_doc,'html.parser')
        title = soup.find(class_="record-value-7")
        title_text = title.text
        post_id = title.attrs['id'][15:]
        charge = soup.find(class_="record-value-113")
        link = "https://db.jimu.kyutech.ac.jp/cgi-bin/cbdb/db.cgi?page=DBRecord&did=372&qid=all&vid=24&rid=" + post_id
        if post_id != self.previous_scholarship_id:
            post = "#Prokumaの掲示板BOT\n" + "留学・国際関連 No." + str(post_id) + "\n" +  str(title_text) + "\n担当部署：" + str(charge) + "\n" + str(link)
            status = api.PostUpdate(post)
            self.previous_scholarship_id = post_id
        threading.Timer(self.refresh_time, self.scholarshipTimer).start()


def main():
    print('START')
    task = Task()
    task.noticeTimer()
    task.timetableTimer()
    task.nolecTimer()
    task.addlecTimer()
    task.callTimer()
    task.scholarshipTimer()

if __name__ == '__main__':
    main()

