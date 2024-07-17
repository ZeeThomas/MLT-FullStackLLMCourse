import requests
class SecEdgar:
    
    
    def __init__(self, fileurl):
        self.fileurl = fileurl
        self.namedict = {}
        self.tickerdict = {}
        headers = {'user-agent': 'Florida Polytechnic University zthomas0695@floridapoly.edu'}
        r = requests.get(self.fileurl, headers=headers)
        self.filejson = r.json
        items =  r.json()
        #print(r.text)
        #print(self.filejson)
        #if r.status_code == 200:
        for key, item in items.items():
            name = item['title']
            ticker = item['ticker']
            
            self.namedict[name] = {'cik_str': item['cik_str'], 'ticker': item['ticker']}
            self.tickerdict[ticker] = {'cik_str': item['cik_str'],'title': item['title']}
        #print(self.namedict)
        searchNum = input("What are you searching with 1-Title or 2-Ticker?: ")

        if searchNum == "1":
            title = input("What's the title?: ")
            response = self.name_to_cik(title)
            print(response)
        elif searchNum == "2":
            ticker = input("What's the ticker?: ")
            response = self.ticker_to_cik(ticker)
            print(response)
        else:
            print("not a valid option")
            
    def name_to_cik(self, key):
        ans = self.namedict.get(key)
        if ans: 
            response = (key, ans['cik_str'], ans['ticker'])
            return response
        else:
            print("Key not found")
            return
    def ticker_to_cik(self, key):
        ans = self.tickerdict.get(key)
        if ans: 
            response = (key, ans['cik_str'], ans['title'])
            return response
        else:
            print("Key not found")
            return

   
        
    

se = SecEdgar('https://www.sec.gov/files/company_tickers.json')