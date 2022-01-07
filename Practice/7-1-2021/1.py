"""
Question: 1
Write a python program that will take input from the user until the user 
gives “STOP” as input. In every line the user will provide input as follow:
[Brand Name] [PRICE]
Your task is to create a dictionary where the brand’s name will be key and 
the value will be a list of that brand’s watches ID. ID generate process: 
inputno_FirstTwoLetterOfBrand_Price. Finally print the dictionary.

Sample Input 1:
OMEGA 10000
TITAN 5000
TITAN 3000
CREDENCE 150000
OMEGA 12000
CREDENCE 90000
STOP
Sample Output 1:
{'OMEGA': ['1_OM_10000', '5_OM_12000'], 'TITAN': 
['2_TI_5000', '3_TI_3000'], 'CREDENCE': ['4_CR_150000', '6_CR_90000']}

Sample Input 2:
CREDENCE 5000
CREDENCE 11000
OMEGA 8000
TITAN 7500
QUARTZ 8000
CASIO 6000
CASIO 7000
STOP
Sample Output 2:
{'CREDENCE': ['1_CR_5000', '2_CR_11000'], 'OMEGA': ['3_OM_8000'], 'TITAN': 
['4_TI_7500'], 'QUARTZ': ['5_QU_8000'], 'CASIO': ['6_CA_6000', '7_CA_7000']}

"""

data={}
n=0
while (True):
    info=input()
    if (info=="STOP"):
        break
    else:
        n=n+1
    brand_name=info.split()[0]
    price=info.split()[1]
    if data.get(brand_name,0)==0:
        data[brand_name]=[str(n)+"_"+brand_name[:2]+"_"+price]
    else:
        data.get(brand_name,0).append(str(n)+"_"+brand_name[:2]+"_"+price)

print(data)
