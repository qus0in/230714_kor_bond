import streamlit as st
import pandas as pd
import requests
import datetime

@st.cache_data
def get_bond_info(basDt):
    url = 'http://apis.data.go.kr/1160100/service/GetBondIssuInfoService/getBondBasiInfo'
    params = lambda x: dict(
        servicKey = st.secrets['BOND_INFO_SK'],
        numOfRows = 1000,
        pageNo = x,
        resultType = 'json',
        basDt = basDt
    )
    w = 1
    data = []
    while True:
        try:
            response = requests.get(url, params=params(w))
            df = pd.DataFrame(response.json()['response']['body']['items']['item'])
            data.append(df)
        except:
            break
        w += 1
    return data

def get_today():
    KST = datetime.timezone(datetime.timedelta(hours=9))
    return datetime.datetime.now(KST).strftime('%Y%m%d')

today = get_today()
st.write(today)
st.write("hello!")
st.write(get_bond_info(today))