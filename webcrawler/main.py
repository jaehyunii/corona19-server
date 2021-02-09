from apscheduler.schedulers.background import BackgroundScheduler
from seocho import seochocrawler
import time
from datetime import datetime



if __name__ == '__main__' :
    sched = BackgroundScheduler()
    sched.start()

    # 여기에 웹크롤러 함수 스케쥴링 하시면 됩니다!
    sched.add_job(seochocrawler.doCrawling, 'interval', hours=5, id='seochoCrawler', next_run_time=datetime.now())


while True :
    print("Scheduler running")
    time.sleep(50)