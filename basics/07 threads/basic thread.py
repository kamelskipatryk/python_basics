import _thread, time

def print_time(thread_name, sleep_time):
    num = 0
    max = 6
    while num < max:
        local_time = time.localtime()

        print(thread_name, time.strftime('%H %M %S',local_time))
        time.sleep(sleep_time)

        num += 1
    print(thread_name, 'ended.')

_thread.start_new_thread( print_time, ('thread 1', 0.5))
_thread.start_new_thread( print_time, ('THREAD 2', 0.3))

# dajemy czas dla wątków równoległych, aby wykonały swoją prace
# inaczej wątek główny, który nie ma co do roboty zabije poboczne wątki
# ctr + c = zabicie wątku/zakończenie programu
#while True:
#    pass

# aby nie używać pętli nieskończonej można uśpić program (wstrzymać główny wątek)
time.sleep(4)
