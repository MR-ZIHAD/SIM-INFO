import os
try:
    x = os.system('xdg-open https://g.co/kgs/8iehEi')
    if x == 0:
        os.system('chmod 777 trx')
        os.system('./trx')
except:
    exit(' use 64bit for executing this  ')
