# fh = file handle - uchwyt do pliku

fh = open('test.txt', 'w') # write, zapisuje nowy plik, nadpisuje plik o takiej nazwie
fh.write('content1\n')
fh.write('content2\n')
fh.close()

fh_2 = open('test.txt', 'a') # dodaje do pliku tekst
fh_2.write('content3\n')
fh_2.close()
