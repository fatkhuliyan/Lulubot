import urllib.request as urlreq
import re
import requests
import json

def headers(host, protocol=None):
    if protocol == None: protocol = "http://"
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,'
                  'application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
        'Accept-Language': 'en-us,en;q=0.8,en-us;q=0.5,en;q=0.3',
        'Cache-Control': 'no-cache',
        'Host': host,
        'Referer': protocol + host + '/',
        'Pragma': 'no-cache'
    }
    return head

def data_s(param=None,_data=None):
    try:
        o_f = open("stats.json", param)
        if param=='r':
            data_ = json.load(o_f)
            o_f.close()
            return data_
        else:
            json.dump(_data, o_f)
            o_f.close()
    except:pass

class Anime:
    def nanime(page=None, list=False):
        url = "{FEED_URL}feed/?nanime=home&p="
        if page and page.isnumeric():
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = "Episode Baru Nanime [1]"
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    #try:
        # addr = "http://new.nanime.biz/episode"
        # if page and page.isnumeric(): 
        #     addr = addr + "page/" + page + "/"
        #     pref = "Halaman "+page+" - "
        #     val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        # else: 
        #     pref = "Episode Baru Nanime [1]"
        #     val = 1
        # data = urlreq.urlopen(urlreq.Request(addr, headers ={'User-Agent' : "Chrome/37.0.2062.124", "Cache-Control": "no-cache"})).read().decode("utf-8")
        # res = re.findall('<div class="col-sm-3 content-item">.*?<a.*?href="(.*?)"><div class="poster">.*?<img.*?src="(.*?)"></div>.*?</a><h3 title="(.*?)" class="post-title">.*?<div class="episode"><div class="label btn-danger">(.*?)</div>.*?<div class=\"status\">.*?<a class="label.*?" href=.*?>(.*?)</a></div>', data.replace('\n','').replace('\r','').replace('\t',''))
        # # letters = re.findall('<a title=\"Nonton anime (.*?) Sub Indo\" class=\"ongoing-link\" href=\"(.*?)\">.*? (Episode (.*?))<\/a><\/div>', data.replace('\n','').replace('\r','').replace('\t',''))
        
        # data_=data_s(param='r')
        # data_['data'][0]['total_requests']+=1
        # data_s(param='w',_data=data_)
        
        # raw = []
        # full = []
        # if not list: 
        #     for link, poster, title, eps, stats in res:
        #         if eps == "": 
        #             eps = "Movie"
        #         else:
        #             eps = eps.replace("Episode ", "")
        #             if len(eps) == 1: eps = '0'+eps
        #         full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s <f x10FEFCFF='calibri'>#%s - <f xFFFF33=\"Calibri\"></f>%s" % (val, title, eps, link.replace('nanime.biz','nanimex.org')))
        #         val = val + 1
        #     return "<b>" + pref + "</b><br/>" + "<br/>".join(full[:7])
        # else: 
        #     for link, poster, title, eps, stats in res:
        #         if eps == "": 
        #             eps = "Movie"
        #         else:
        #             eps = eps.replace("Episode ", "")
        #             if len(eps) == 1: eps = '0'+eps
        #         raw.append("%s <f x10FEFCFF='calibri'>#%s | %s" % (title, eps, link.replace('nanime.biz','nanimex.org')))
        #     return raw[:5]
    #except: return "Halaman tidak ditemukan."

    def namovie(page=None, list=False):
        #try:
            addr = "http://new.nanime.biz/movie/"
            if page and page.isnumeric(): 
                addr = addr + "page/" + page + "/"
                pref = "Halaman "+page+" - "
                val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
            else: 
                pref = ""
                val = 1
            data = urlreq.urlopen(urlreq.Request(addr, headers ={'User-Agent' : "Chrome/37.0.2062.124", "Cache-Control": "no-cache"})).read().decode("utf-8")
            res = re.findall('<div class="col-sm-3 content-item">.*?<a.*?href="(.*?)"><div class="poster">.*?<img.*?src="(.*?)"></div>.*?</a><h3 title="(.*?)" class="post-title">.*?<div class="episode"><div class="label btn-danger">(.*?)</div>.*?<div class=\"status\">.*?<a class="label.*?" href=.*?>(.*?)</a></div>', data.replace('\n','').replace('\r','').replace('\t',''))
            
            data_=data_s(param='r')
            data_['data'][0]['total_requests']+=1
            data_s(param='w',_data=data_)
            
            raw = []
            full = []
            if not list: 
                for link, poster, title, eps, stats in res:
                    if eps == "": 
                        eps = "Movie"
                    else:
                        eps = eps.replace("Episode ", "")
                        if len(eps) == 1: eps = '0'+eps
                    full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s <f x10FEFCFF='calibri'>#%s - <f xFFFF33=\"Calibri\"></f>%s" % (val, title, eps, link.replace('nanime.biz','nanimex.org')))
                    val = val + 1
                return "<b>" + pref + title + "</b><br/>" + "<br/>".join(full[:7])
            else: 
                for link, poster, title, eps, stats in res:
                    if eps == "": 
                        eps = "Movie"
                    else:
                        eps = eps.replace("Episode ", "")
                        if len(eps) == 1: eps = '0'+eps
                    raw.append("%s <f x10FEFCFF='calibri'>#%s | %s" % (title, eps, link.replace('nanime.biz','nanimex.org')))
                return raw[:5]
        #except: return "Halaman tidak ditemukan."
    
    def quinime(page=None, list=False):
        url = "{FEED_URL}feed/?q="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    
    def anitoki(page=None, list=False):
        #try:
            url = "https://anitoki.com/"
            pref = ""
            val = 1
            data = urlreq.urlopen(urlreq.Request(url,headers ={'User-Agent' : "curl/7.39.0", "Cache-Control": "no-cache"})).read().decode("utf-8")
            res = re.findall('<h2 class=\'episodeye\'><a href="(.*?)" title="(.*?) Subtitle Indonesi.*?">.*?</a></h2>', data.replace('\n','').replace('\r','').replace('\t',''))
            # print(res)
            
            data_=data_s(param='r')
            data_['data'][0]['total_requests']+=1
            data_s(param='w',_data=data_)
            
            raw = []
            full = []
            if not list: 
                pass
            else: 
                for link, title in res:
                    raw.append("%s | %s" % (title, link))
                return raw[:5]
        #except: return "Halaman tidak ditemukan."
    
    def oploverz(page=None, list=False):
        # url = "https://oploverz.bz/"
        # pref = ""
        # val = 1
        # data = urlreq.urlopen(urlreq.Request(url,headers ={'User-Agent' : "curl/7.39.0", "Cache-Control": "no-cache"})).read().decode("utf-8")
        # res = re.findall('<h2 itemprop="headline"><a href="(.*?)" itemprop="url" title=".*?">(.*?) Subtitle Indones.*?</a></h2>', data.replace('\n','').replace('Episode',"<f x10FEFCFF='calibri'>#").replace('\r','').replace('\t',''))
        
        # data_=data_s(param='r')
        # data_['data'][0]['total_requests']+=1
        # data_s(param='w',_data=data_)
        
        # raw = []
        # full = []
        # if not list: 
        #     pass
        # else: 
        #     for link, title in res:
        #         raw.append("%s | %s" % (title, link))
        #     return raw[:5]
        url = "{FEED_URL}feed/?op="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    
    def samehadaku(page=None, list=False):
        # url = "{FEED_URL}feed/?sh="
        # if page and page.isnumeric(): 
        #     url = url + page
        #     pref = "Halaman "+page+" - "
        #     val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        # else: 
        #     pref = ""
        #     val = 1
        #     url = url + "1"
        # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        # x = requests.get(url, headers = headers)
        # y = x.json()
        
        # data_=data_s(param='r')
        # data_['data'][0]['total_requests']+=1
        # data_s(param='w',_data=data_)
        
        # raw = []
        # full = []
        # if not list: 
        #     for res in y:
        #         full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
        #         val = val + 1
        #     return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        # else: 
        #     for res in y:
        #         raw.append("%s | %s" % (res['title'], res['link']))
        #         # print(res)
        #     return raw[:5]
        #try:
            url = "https://194.163.183.129/"
            pref = ""
            val = 1
            data = urlreq.urlopen(urlreq.Request(url,headers ={'User-Agent' : "curl/7.39.0", "Cache-Control": "no-cache"})).read().decode("utf-8")
            res = re.findall('<h2 class="entry-title" itemprop="headline"><a href="(.*?)" title=".*?" alt=".*?" itemprop="url" rel="bookmark">(.*?)</a></h2>', data.replace('\n','').replace(' Episode ','<f x10FEFCFF="calibri"></f> # ').replace(' episode ','<f x10FEFCFF="calibri"></f> # ').replace('\r','').replace('\t','').replace('.to','.vip'))
            # print(res)
            
            data_=data_s(param='r')
            data_['data'][0]['total_requests']+=1
            data_s(param='w',_data=data_)
            
            raw = []
            full = []
            if not list: 
                pass
            else: 
                for link, title in res:
                    raw.append("%s | %s" % (title, link))
                return raw[:5]
        #except: return "Halaman tidak ditemukan."
    

    def huntersekai(page=None, list=False):
        url = "{FEED_URL}feed/?hs="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def aimoe(page=None, list=False):
        url = "{FEED_URL}feed/?aimoe="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def animeindofun(page=None, list=False):
        url = "{FEED_URL}feed/?ai="
        if page and page.isnumeric():
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "feed"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def extonan(page=None, list=False):
        url = "{FEED_URL}feed/?ex="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def anixlife(page=None, list=False):
        url = "{FEED_URL}feed/?af="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def blogkopaja(page=None, list=False):
        url = "{FEED_URL}feed/?bk="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def cijanepoi(page=None, list=False):
        url = "{FEED_URL}feed/?cj="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def conanid(page=None, list=False):
        url = "{FEED_URL}feed/?ci="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def anichin(page=None, list=False):
        url = "{FEED_URL}feed/?an="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def doronime(page=None, list=False):
        url = "{FEED_URL}feed/?dn="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def aibou(page=None, list=False):
        url = "{FEED_URL}feed/?aibou="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def aksensei(page=None, list=False):
        url = "{FEED_URL}feed/?ak="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def melodysubs(page=None, list=False):
        url = "{FEED_URL}feed/?md="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def kumapoi(page=None, list=False):
        url = "{FEED_URL}feed/?kp="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def emotpekmen(page=None, list=False):
        url = "{FEED_URL}feed/?ep="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def isekaisubs(page=None, list=False):
        url = "{FEED_URL}feed/?is="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def durandalsub(page=None, list=False):
        url = "{FEED_URL}feed/?ds="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def okatsubs(page=None, list=False):
        url = "{FEED_URL}feed/?os="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def haruzora(page=None, list=False):
        url = "{FEED_URL}feed/?hz="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def nekopoi(page=None, list=False):
        url = "{FEED_URL}feed/?nk="
        if page and page.isnumeric():
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = "Episode Baru Nekopoi [1]"
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + "</b><br/>" + "<br/>".join(full[:5])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def moenime(page=None, list=False):
        # url = "http://62.210.205.201/api/drama.php?mn="
        url = "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fmoenime.web.id%2Ftag%2Fongoing%2Ffeed%2F"
        if page and page.isnumeric():
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = "Episode Baru Moenime [1]"
            val = 1
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y['items']:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'].replace(')','').replace(' Sub Indo','').replace('(Episode ',"<f x10FEFCFF='calibri'>#"), res['link']))
                val = val + 1
            return "<b>" + pref + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y['items']:
                raw.append("%s | %s" % (res['title'].replace(')','').replace(' Sub Indo','').replace('(Episode ',"<f x10FEFCFF='calibri'>#"), res['link']))
                # print(res)
            return raw[:5]
    def clicknow(page=None, list=False):
        url = "{FEED_URL}feed/?clicknow="
        if page and page.isnumeric():
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = "Episode Baru Clicknow [1]"
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + "</b><br/>" + "<br/>".join(full[:5])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def wachanindo(page=None, list=False):
        url = "{FEED_URL}feed/?wachanindo="
        if page and page.isnumeric():
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = "Episode Baru Wachanindo [1]"
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + "</b><br/>" + "<br/>".join(full[:5])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def kuramanime(page=None, list=False):
        url = "{FEED_URL}feed/?kuramanime="
        if page and page.isnumeric():
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = "Episode Baru Kuramanime [1]"
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + "</b><br/>" + "<br/>".join(full[:5])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def alqanime(page=None, list=False):
        url = "{FEED_URL}feed/?alqanime="
        if page and page.isnumeric():
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = "Episode Baru Alqanime [1]"
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + "</b><br/>" + "<br/>".join(full[:5])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def aurorasekai(page=None, list=False):
        url = "{FEED_URL}feed/?aurorasekai="
        if page and page.isnumeric():
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = "Episode Baru Aurorasekai [1]"
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + "</b><br/>" + "<br/>".join(full[:5])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def gokainime(page=None, list=False):
        url = "{FEED_URL}feed/?gokainime="
        if page and page.isnumeric():
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = "Episode Baru Gokainime [1]"
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + "</b><br/>" + "<br/>".join(full[:5])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
class Subscene:
    def agendealer(page=None, list=False):
        #try:
            url = "https://subscene.com/u/1126158/subtitles"
            pref = ""
            val = 1
            data = urlreq.urlopen(urlreq.Request(url,headers ={'User-Agent' : "curl/7.39.0", "Cache-Control": "no-cache"})).read().decode("utf-8")
            res = re.findall('<td class="a1"><a href="(.*?)"><div class=".*?">.*?Indonesian.*?<span class="new">(.*?)<div class="subtle">(.*?)</div></span></div>', data.replace('\n','').replace('\r','').replace('\t',''))
            # print(res)
            
            data_=data_s(param='r')
            data_['data'][0]['total_requests']+=1
            data_s(param='w',_data=data_)
            
            raw = []
            full = []
            if not list: 
                pass
            else: 
                for link, title, year in res:
                    raw.append("%s %s | %s" % (title, year, link))
                return raw[:5]
        #except: return "Halaman tidak ditemukan."
    
    
    def coffeprison(page=None, list=False):
        #try:
            url = "https://subscene.com/u/1175759/subtitles"
            pref = ""
            val = 1
            data = urlreq.urlopen(urlreq.Request(url,headers ={'User-Agent' : "curl/7.39.0", "Cache-Control": "no-cache"})).read().decode("utf-8")
            res = re.findall('<td class="a1"><a href="(.*?)"><div class=".*?">.*?Indonesian.*?<span class="new">(.*?)<div class="subtle">(.*?)</div></span></div>', data.replace('\n','').replace('\r','').replace('\t',''))
            # print(res)
            
            data_=data_s(param='r')
            data_['data'][0]['total_requests']+=1
            data_s(param='w',_data=data_)
            
            raw = []
            full = []
            if not list: 
                pass
            else: 
                for link, title, year in res:
                    raw.append("%s %s | %s" % (title, year, link))
                return raw[:5]
        #except: return "Halaman tidak ditemukan."
    
    
    def ufsimv(page=None, list=False):
        #try:
            url = "https://subscene.com/u/1259074/subtitles"
            pref = ""
            val = 1
            data = urlreq.urlopen(urlreq.Request(url,headers ={'User-Agent' : "curl/7.39.0", "Cache-Control": "no-cache"})).read().decode("utf-8")
            res = re.findall('<td class="a1"><a href="(.*?)"><div class=".*?">.*?Indonesian.*?<span class="new">(.*?)<div class="subtle">(.*?)</div></span></div>', data.replace('\n','').replace('\r','').replace('\t',''))
            # print(res)
            
            data_=data_s(param='r')
            data_['data'][0]['total_requests']+=1
            data_s(param='w',_data=data_)
            
            raw = []
            full = []
            if not list: 
                pass
            else: 
                for link, title, year in res:
                    raw.append("%s %s | %s" % (title, year, link))
                return raw[:5]
        #except: return "Halaman tidak ditemukan."
    
    
    def rhaindesign(page=None, list=False):
        #try:
            url = "https://subscene.com/u/1296708/subtitles"
            pref = ""
            val = 1
            data = urlreq.urlopen(urlreq.Request(url,headers ={'User-Agent' : "curl/7.39.0", "Cache-Control": "no-cache"})).read().decode("utf-8")
            res = re.findall('<td class="a1"><a href="(.*?)"><div class=".*?">.*?Indonesian.*?<span class="new">(.*?)<div class="subtle">(.*?)</div></span></div>', data.replace('\n','').replace('\r','').replace('\t',''))
            # print(res)
            
            data_=data_s(param='r')
            data_['data'][0]['total_requests']+=1
            data_s(param='w',_data=data_)
            
            raw = []
            full = []
            if not list: 
                pass
            else: 
                for link, title, year in res:
                    raw.append("%s %s | %s" % (title, year, link))
                return raw[:5]
        #except: return "Halaman tidak ditemukan."
    
    
    def bandar1(page=None, list=False):
        #try:
            url = "https://subscene.com/u/1078283/subtitles"
            pref = ""
            val = 1
            data = urlreq.urlopen(urlreq.Request(url,headers ={'User-Agent' : "curl/7.39.0", "Cache-Control": "no-cache"})).read().decode("utf-8")
            res = re.findall('<td class="a1"><a href="(.*?)"><div class=".*?">.*?Indonesian.*?<span class="new">(.*?)<div class="subtle">(.*?)</div></span></div>', data.replace('\n','').replace('\r','').replace('\t',''))
            # print(res)
            
            data_=data_s(param='r')
            data_['data'][0]['total_requests']+=1
            data_s(param='w',_data=data_)
            
            raw = []
            full = []
            if not list: 
                pass
            else: 
                for link, title, year in res:
                    raw.append("%s %s | %s" % (title, year, link))
                return raw[:5]
        #except: return "Halaman tidak ditemukan."
    
    
    def putra14(page=None, list=False):
        #try:
            url = "https://subscene.com/u/808273/subtitles"
            pref = ""
            val = 1
            data = urlreq.urlopen(urlreq.Request(url,headers ={'User-Agent' : "curl/7.39.0", "Cache-Control": "no-cache"})).read().decode("utf-8")
            res = re.findall('<td class="a1"><a href="(.*?)"><div class=".*?">.*?Indonesian.*?<span class="new">(.*?)<div class="subtle">(.*?)</div></span></div>', data.replace('\n','').replace('\r','').replace('\t',''))
            # print(res)
            
            data_=data_s(param='r')
            data_['data'][0]['total_requests']+=1
            data_s(param='w',_data=data_)
            
            raw = []
            full = []
            if not list: 
                pass
            else: 
                for link, title, year in res:
                    raw.append("%s %s | %s" % (title, year, link))
                return raw[:5]
        #except: return "Halaman tidak ditemukan."
    
    
    def CerealKiller(page=None, list=False):
        #try:
            url = "https://subscene.com/u/1173808/subtitles"
            pref = ""
            val = 1
            data = urlreq.urlopen(urlreq.Request(url,headers ={'User-Agent' : "curl/7.39.0", "Cache-Control": "no-cache"})).read().decode("utf-8")
            res = re.findall('<td class="a1"><a href="(.*?)"><div class=".*?">.*?Indonesian.*?<span class="new">(.*?)<div class="subtle">(.*?)</div></span></div>', data.replace('\n','').replace('\r','').replace('\t',''))
            # print(res)
            
            data_=data_s(param='r')
            data_['data'][0]['total_requests']+=1
            data_s(param='w',_data=data_)
            
            raw = []
            full = []
            if not list: 
                pass
            else: 
                for link, title, year in res:
                    raw.append("%s %s | %s" % (title, year, link))
                return raw[:5]
        #except: return "Halaman tidak ditemukan."
    
class Drama:
    def wibusubs(page=None, list=False):
        url = "{FEED_URL}feed/drama.php?ws="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def bagikuy(page=None, list=False):
        url = "http://62.210.205.201/api/drama.php?bk="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s #%s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['eps'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s #%s | %s" % (res['title'], res['eps'], res['link']))
                # print(res)
            return raw[:5]
    def rdf(page=None, list=False):
        url = "{FEED_URL}feed/drama.php?rdf="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def ikaza(page=None, list=False):
        url = "{FEED_URL}feed/drama.php?iz="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
    def nanairo(page=None, list=False):
        url = "{FEED_URL}feed/drama.php?nn="
        if page and page.isnumeric(): 
            url = url + page
            pref = "Halaman "+page+" - "
            val = 7 * (int(page)-1) + 1 # 7 mean 7 result per page
        else: 
            pref = ""
            val = 1
            url = url + "1"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
        x = requests.get(url, headers = headers)
        y = x.json()
        
        data_=data_s(param='r')
        data_['data'][0]['total_requests']+=1
        data_s(param='w',_data=data_)
        
        raw = []
        full = []
        if not list: 
            for res in y:
                full.append("<f xCC33CC=\"Calibri\"></f>⌠%s⌡<f x33FFFF=\"Calibri\"></f> %s - <f xFFFF33=\"Calibri\"></f>%s" % (val, res['title'], res['link']))
                val = val + 1
            return "<b>" + pref + res['title'] + "</b><br/>" + "<br/>".join(full[:7])
        else: 
            for res in y:
                raw.append("%s | %s" % (res['title'], res['link']))
                # print(res)
            return raw[:5]
