import threading, time

data = ['Adam','Ola','Kasia','Daniel','Rafał']
data_lock = threading.Lock()

class some_thread(threading.Thread):
    def __init__(self, thread_name, data_len, sleep_time):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.sleep_time = sleep_time
        self.data_len = data_len

    def run(self):
        num = 0
        while num < self.data_len:
            # linijki między acquire i release bedą synchronizowane
            data_lock.acquire()
            data[num] = data[num] + ' ' + str(num)
            print(self.thread_name, data[num])
            data_lock.release()

            time.sleep(self.sleep_time)

            num += 1
        print(self.thread_name, 'ended.', data)

t1 = some_thread('t1', len(data), 0.1)
t2 = some_thread('t2', len(data), 0.2)
t3 = some_thread('t3', len(data), 0.3)

t1.start()
t2.start()
t3.start()

print('t2 is alive:', t2.is_alive())

t1.join()
t2.join()
t3.join()

print('All threads ended.')