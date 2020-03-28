import urllib.request as ul
import json, datetime, time
import pandas as pd

def info():
    movieDate=time.strftime('%Y%m%d', time.localtime(time.time()))
    print(movieDate)
    cine=[{}]
    #while int(movieDate)//10000 != 2018:
    for i in range(0,30):
        url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=66e652e1d2656b42f10d93c91e0295e4&targetDt={movieDate}"

        request = ul.Request(url)
        print(request)
        response = ul.urlopen(request)
        print(response)
        rescode = response.getcode()
        print(rescode)
        if(rescode == 200):
            responseData = response.read()

        result = json.loads(responseData)
        #print(result)
        pre_result =result["boxOfficeResult"]
        #print(pre_result)
        
        pre_result1 = pre_result["dailyBoxOfficeList"]
        #print(pre_result1)
        #print(type(pre_result1))
                
        # 날짜, 영화이름, 누적관객수
        for i in range(0,len(pre_result1)):
            pre_result1[i]['targetDt']=movieDate
            cine.append(pre_result1[i])
        

        #반복 함수 마지막에 날짜를 줄이는 함수를 사용한다.
        #str -> date
        datetime_obj = datetime.datetime.strptime(movieDate,"%Y%m%d").date()

        # 1주일씩 시간을 줄여간다.
        datetime_obj_tmp = datetime_obj - datetime.timedelta(days=1)
        #datetime_obj_tmp = datetime_obj - datetime.timedelta(weeks=1)

        #date -> str
        day = datetime_obj_tmp.strftime("%Y-%m-%d").split('-')
        movieDate = day[0]+day[1]+day[2]
        print(movieDate)
        
    print(cine)    
    dataframe=pd.DataFrame(cine)
    #첫행이 비어있음.
    dataframe=dataframe[1:]
    #print(dataframe.head())
    dataframe.to_csv("cine.csv")

if __name__ == "__main__":
    info()

