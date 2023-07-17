from src.SlimService import slims
import sys,os

user = raw_input("Username: ")

import getpass

sandi = getpass.getpass()

if sandi == 'jakarta ghost' and user == 'luhekerr':

    print "Anda Telah Login"

else:

    print "Username atau Password Anda Salah"
    
os.system("clear")

def param_check():
	try:
		a = sys.argv[1]
	except IndexError:
		print("\033[1;31m Usage python2 slim.py file.txt \033[1;37m")
		os.sys.exit()

def file_check():
	try:
		open(sys.argv[1])
	except IOError:
		print("Pastikan file yang mau di upload benar")
		os.sys.exit()

def about():
	os.system(" ")
print ('\033[1;31m    _______ ')
print (' __ / / ___/')
print ('/ // / (_ / ')
print ('\___/\___/ \033[1;37mSlimass By Jakarta Ghost\n')

    




if __name__ == "__main__":
	try:
		about()
		param_check()
		file_check()
		while True:
			target = raw_input("\033[1;37m[ \033[1;31mURL \033[1;37m]> ")
			a = slims(target, sys.argv[1])
	except:
		pass