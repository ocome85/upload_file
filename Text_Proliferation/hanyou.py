from telnetlib import WONT
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials 
 
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
 
# 秘密鍵（JSONファイル）のファイル名を入力
credentials = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\koyos\\Desktop\\Forge\\tool\\minecraftforge.json", scope)
gc = gspread.authorize(credentials)

 
wb = gc.open('Minecraft_Nijisanji_Mod')
ws = wb.get_worksheet(0)
#0列目(1列目)を読むよ
col_list0 = ws.col_values(1)
#2(3)
col_list = ws.col_values(2)

#パス入力　\は2ついるよ
folderpath ="C:\\Users\\koyos\\Desktop\\Forge\\tool\\upload_file\\Text_Proliferation\\"
file = folderpath +"hanyou.txt"
newfile =folderpath +"newhanyou.txt"

#開始は0読み取りなので
gyou = -1
for sheetvalue in col_list:
    gyou +=1
    print(sheetvalue)
    OldWord = 'Test'
    NewWord = sheetvalue
    BigOldWord = OldWord.upper()
    BigNewWord = NewWord.upper()
    SmallOldWord = OldWord.lower()
    SmallNewWord = NewWord.lower()
    text1 ="sampletext"
    text2 =col_list0[gyou]

    #ファイル内文字列変換
    #EntityFile置換
    with open(file, encoding="cp932") as f:
        data_lines = f.read()
    data_lines = data_lines.replace(OldWord, NewWord).replace(BigOldWord, BigNewWord).replace(SmallOldWord,SmallNewWord).replace(text1,text2)
    # with open(newfile, mode="a", encoding="cp932") as f:
    #     f.write(data_lines)
    with open(newfile, mode="a", encoding="cp932") as f:
        f.write(data_lines)



