# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mS-o_ZuOq_FWJbrZORCM2BzeWUSO4Ub8
"""

import pandas as pd
baza={
    "FISH":["Xonqulov Muhammadjon" ,"Yusupov Dilyorbek" , "Xoshimov Behruz" , "Abdusattorova Mubina" , "Umarova Sohiba" ,"Sobirov Og'abek" , "Zohidov Mardon", "Sharipov Burhonjon" , "Alijonova Marjona" , "Sodiqova Ruxsora" ],
    "Yoshi": [ "11" , "15" , "14" , "16" , "12" , "13" , "15" , "14" , "17", "16"  ] ,
    "Jinsi": [ "o'g'il bola" , "o'g'il bola" , "o'g'il bola" , "qiz bola" , "qiz bola" , "o'g'il bola" , "o'g'il bola" , "o'g'il bola" , "qiz bola" , "qiz bola"],
    "Maktab raqami":[ "36" ,"18" , "29" , "45" , "25" , "13" , "31" , "30" , "16" , "47"]

}
df=pd.DataFrame(baza)
print(df)