import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials 
 
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
 
# 秘密鍵（JSONファイル）のファイル名を入力
credentials = ServiceAccountCredentials.from_json_keyfile_name("Desktop\Forge\\tool\\minecraftforge.json", scope)
gc = gspread.authorize(credentials)

 
wb = gc.open('Minecraft_Nijisanji_Mod')
ws = wb.get_worksheet(0)
col_list = ws.col_values(2)

for sheetvalue in col_list:
    print(sheetvalue)
    folderpath ="C:Desktop\Forge\\tool\\sound.txt"
    newfolderpath ="C:Desktop\Forge\\tool\\newsound.txt"
    OldWord = 'Ex_Albio'
    NewWord = sheetvalue
    BigOldWord = OldWord.upper()
    BigNewWord = NewWord.upper()
    SmallOldWord = OldWord.lower()
    SmallNewWord = NewWord.lower()


    #ファイル内文字列変換
    #EntityFile置換
    with open(folderpath, encoding="cp932") as f:
        data_lines = f.read()
    data_lines = data_lines.replace(OldWord, NewWord).replace(BigOldWord, BigNewWord).replace(SmallOldWord, SmallNewWord)
    with open(newfolderpath+'new', mode="a", encoding="cp932") as f:
        f.write(data_lines)


