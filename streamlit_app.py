import streamlit as st
import pandas as pd
import requests
import datetime

@st.cache_data
def get_bond_info(basDt):
    url = 'http://apis.data.go.kr/1160100/service/GetBondIssuInfoService/getBondBasiInfo'
    params = lambda x: dict(
        servicKey = st.secrets['BOND_INFO_SK'],
        numOfRows = 10000,
        pageNo = x,
        resultType = 'json',
        basDt = basDt
    )
    w = 1
    data = []
    while True:
        response = requests.get(url, params=params(w))
        df = pd.DataFrame(response.json()['response']['body']['items']['item'])
        if not len(df): break
        data.append(df)
        w += 1
    return pd.concat(data)

st.write("hello!")
KST = datetime.timezone(datetime.timedelta(hours=9))
st.write(datetime.date.today(tzinfo=KST))