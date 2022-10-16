import os

script_dir = os.path.dirname(__file__) # ścieżka absolutna
print(script_dir)

fh = open( script_dir + '/ogonki.txt', 'w', encoding='utf-8' )
fh.write('test z ogonkakmi: ążź\n')
fh.write('test z ogonkakmi: ążź\n')
fh.write('test z ogonkakmi: ążź\n')
fh.close()


