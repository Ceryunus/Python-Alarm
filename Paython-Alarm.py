import random
import time
import webbrowser


class calarsaat():

    def randomSelectorAndPlayer(self):
        # Alarm Sesleri
        url1 = "https://www.youtube.com/watch?v=396gGW4VhM4"
        url2 = "https://www.youtube.com/watch?v=RO8MHmT_qaA"
        url3 = "https://www.youtube.com/watch?v=Qp21t5T2LkM"

        urls = [url1, url2, url3]
        webbrowser.open(random.choice(urls))

    def input(self):
        sa = int(input("Alarm Saatini Giriniz : "))
        self.kalkissaati = sa
        dk = int(input("Alarm Dakikasını Giriniz : "))
        self.kalkisdakikasi = dk

    def alarm(self):
        self.input()
        while True:
            t = time.localtime()
            time.sleep(1)
            self.saat = t.tm_hour
            self.dakika = t.tm_min
            print(t.tm_hour, t.tm_min, t.tm_sec)
            if self.saat == self.kalkissaati and self.dakika == self.kalkisdakikasi:
                self.randomSelectorAndPlayer()
                break


alaram1 = calarsaat()
alaram1.alarm()
