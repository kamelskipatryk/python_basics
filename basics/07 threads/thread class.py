import threading, time

class some_thread(threading.Thread):
    def __init__(self, thread_name, sleep_time):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.sleep_time = sleep_time

    def run(self):
        num = 0
        max = 6
        while num < max:
            local_time = time.localtime()

            print(self.thread_name, time.strftime('%H %M %S',local_time))
            time.sleep(self.sleep_time)

            num += 1
        print(self.thread_name, 'ended.')

t1 = some_thread('t1', 0.1)
t2 = some_thread('t2', 0.1)
t3 = some_thread('t3', 0.1)

t1.start()
t2.start()
t3.start()

print('t2 is alive:', t2.is_alive())

t1.join()
t2.join()
t3.join()

print('All threads ended.')