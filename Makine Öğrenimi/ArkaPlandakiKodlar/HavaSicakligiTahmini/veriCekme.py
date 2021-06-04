import requests
import json

def bilgi(il):
    r=requests.get("https://servis.mgm.gov.tr/web/merkezler?il=" + str(il), 
		headers={"accept":"application/json, text/plain, */*",
		"referer":"https://www.mgm.gov.tr/",
		"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
		"sec-ch-ua":"\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
		"sec-ch-ua-mobile":"?0",
		"sec-fetch-dest":"empty",
		"sec-fetch-mode":"cors",
		"host":"servis.mgm.gov.tr",
		"origin":"https://www.mgm.gov.tr",
		"accept-encoding":"gzip, deflate, br",
		"accept-language":"en-US,en;q=0.9,tr-TR;q=0.8,tr;q=0.7,de-DE;q=0.6,de;q=0.5,ja-JP;q=0.4,ja;q=0.3"})
    data = r.json()
    return data[0]


def merkez(m_id):
    r=requests.get("https://servis.mgm.gov.tr/web/sondurumlar?merkezid="+str(m_id), 
		headers={"accept":"application/json, text/plain, */*",
		"referer":"https://www.mgm.gov.tr/",
		"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
		"sec-ch-ua":"\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
		"sec-ch-ua-mobile":"?0",
		"sec-fetch-dest":"empty",
		"sec-fetch-mode":"cors",
		"host":"servis.mgm.gov.tr",
		"origin":"https://www.mgm.gov.tr",
		"accept-encoding":"gzip, deflate, br",
		"accept-language":"en-US,en;q=0.9,tr-TR;q=0.8,tr;q=0.7,de-DE;q=0.6,de;q=0.5,ja-JP;q=0.4,ja;q=0.3"})
    data = r.json()[0]
    veriler ={"Sicaklik": data["sicaklik"],
              "Nem":data["nem"],
              "RuzgarYonu": data["ruzgarYon"],
              "Ruzgar_Hizi":data["ruzgarHiz"],
              "AktuelBasinc":data["aktuelBasinc"],
              "DenizeBasinc":data["denizeIndirgenmisBasinc"],
              "SuAnkiHavaDurumu":data["hadiseKodu"],
              "Yagis":data["yagis00Now"]
              }
    return veriler
    

ist = bilgi("Istanbul")
m_id = ist["merkezId"]

veri = merkez(m_id)


