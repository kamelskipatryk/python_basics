import time
import datetime

# aktulana ilość sekund od 1 stycznia 1970
ticks = time.time()
print(ticks) # 1660408953.7611413

# localtime -> zwraca więcej informacji o dacie, wrzuca je do krotki
time_data = time.localtime()
print(time_data) # time.struct_time(tm_year=2022, tm_mon=8, tm_mday=13, tm_hour=18, tm_min=43, tm_sec=33, tm_wday=5, tm_yday=225, tm_isdst=1)
# tm_isdst=1 -> czy python zarządza czasem letnim -> 1 zarządza, -1 nie zarządza

print(time_data.tm_zone) # Środkowoeuropejski czas letni
print(time_data.tm_year) # 2022

# time.asctime -> pokazanie daty w bardziej przystępny sposób
# time.localtime(10) -> pierwsze 10 sekund od 1 sycznia 1970
result = time.asctime( time.localtime() ) # localtime() bez argumentu -> daje dane dzisiejsze
print(result) # Sat Aug 13 18:48:15 2022

# sformatowanie daty wg. swoich potrzeb
time_data_2 = time.localtime()
print( time.strftime( '%d/%m/%Y %H:%M:%S ', time_data_2 ) )# drugi argument to krotka z danymi
# 13/08/2022 18:52:57

# odczytanie daty z łańcucha znaków do krotki
time_string = '18:53:49 13.08.2008'
time_data_from_string = time.strptime(time_string, '%H:%M:%S %d.%m.%Y')
print(time_data_from_string)
print( time.strftime( '%d/%m/%Y %H:%M:%S ', time_data_from_string ) ) # 13/08/2008 18:53:49 <- string

# time.sleep -> uśpicie wątka dla programu
i = 0
while i < 12:
    time.sleep(0.0000001) # pół sekundy
    print( time.asctime(time.localtime()) )
    i += 1

# time.perf_counter() -> sprawdzenie jak długo wykonuje się program/fragment programu
time_start = time.perf_counter() # czas początkowy
time.sleep(0.0000001) # symulacja trwania kodu
time_end = time.perf_counter()
print('Code took: ',(time_end - time_start), 'seconds.') # Code took:  0.0017647999999894637 seconds.

# datetime -> manipulujemy czasem oraz datą
date_time_obj = datetime.datetime.now()
print(date_time_obj) # 2022-08-13 20:14:48.932256
print(dir(date_time_obj)) # lista dostępnych metod dla tej zmiennej (datetime)

date_time_obj_2 = datetime.datetime(2025, 3, 10)
print(date_time_obj_2) # 2025-03-10 00:00:00

date_time_obj_3 = datetime.datetime(2025, 3, 10, 22, 59, 59)
print(date_time_obj_3) # 2025-03-10 22:59:59

print('date():', date_time_obj_2.date()) # date():  2025-03-10
print('time():', date_time_obj_3.time()) # time():  22:59:59
print('timestamp():', date_time_obj_3.timestamp()) # timestamp():  1741643999.0
print('today():', date_time_obj_3.today) # today():  2022-08-13 20:21:02.506817
print('year:', date_time_obj_3.year) # year: 2025
print('month:', date_time_obj_3.month) # month: 3
print('day:', date_time_obj_3.day) # day: 10
print('hour:', date_time_obj_3.hour) # hour: 22
print('minute:', date_time_obj_3.minute) # minute: 59
print('second:', date_time_obj_3.second) # second: 59

print( 'format:',date_time_obj_3.strftime('%H:%M:%S %d.%m.%y') ) # format: 22:59:59 10.03.25

date_time_obj_now = datetime.datetime.now()
print( 'format:',date_time_obj_now.strftime('%H:%M:%S %d.%m.%y') ) # format: 20:29:26 13.08.22

date_time_1 = datetime.datetime(2025,1,1, 23,59,59)
date_time_2 = datetime.datetime(2035,1,1, 23,59,59)

print( date_time_1 > date_time_2 ) # False
print( date_time_1 < date_time_2 ) # True

date_1 = datetime.date(2025,1,1)
date_2 = datetime.date(2030,1,1)

print( date_1 > date_2 ) # False
print( date_1 < date_2 ) # True
