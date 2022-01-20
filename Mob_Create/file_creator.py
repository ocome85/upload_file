import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials 
 
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']


corepath ="C:\\Users\\koyos\\Desktop\\Forge\\tool\\upload_file\\Mob_Create\\"
# 秘密鍵（JSONファイル）のファイル名を入力
credentials = ServiceAccountCredentials.from_json_keyfile_name(corepath + "key\\minecraftforge.json", scope)
gc = gspread.authorize(credentials)

 
#Google スプレッドシート名
wb = gc.open('Minecraft_Nijisanji_Mod')
ws = wb.get_worksheet(0)
#2列目をすべて取得　この文字列分変換してコードを作成します
col_list = ws.col_values(2)

#ファイルパスを記入

folderpath1 =corepath +"file_creator\\file_creator1.txt"
newfolderpath1 =corepath +"file_creator\\newfile_creator1.txt"
folderpath2 =corepath +"file_creator\\file_creator2.txt"
newfolderpath2 =corepath +"file_creator\\newfile_creator2.txt"
folderpath3 =corepath +"file_creator\\file_creator3.txt"
newfolderpath3 =corepath +"file_creator\\newfile_creator3.txt"
#... 好きなだけ増やして

#該当文字を別文字へ、その小文字と大文字も対応して変換
for sheetvalue in col_list:
    print(sheetvalue)
    OldWord = 'Test'
    NewWord = sheetvalue
    BigOldWord = OldWord.upper()
    BigNewWord = NewWord.upper()
    SmallOldWord = OldWord.lower()
    SmallNewWord = NewWord.lower()


    #ファイル内文字列変換
    #File置換
    with open(folderpath1, encoding="cp932") as f:
        data_lines = f.read()
    data_lines = data_lines.replace(OldWord, NewWord).replace(BigOldWord, BigNewWord).replace(SmallOldWord, SmallNewWord)
    with open(newfolderpath1, mode="a", encoding="cp932") as f:
        f.write(data_lines)

    with open(folderpath2, encoding="cp932") as f:
        data_lines = f.read()
    data_lines = data_lines.replace(OldWord, NewWord).replace(BigOldWord, BigNewWord).replace(SmallOldWord, SmallNewWord)
    with open(newfolderpath2, mode="a", encoding="cp932") as f:
        f.write(data_lines)

    with open(folderpath3, encoding="cp932") as f:
        data_lines = f.read()
    data_lines = data_lines.replace(OldWord, NewWord).replace(BigOldWord, BigNewWord).replace(SmallOldWord, SmallNewWord)
    with open(newfolderpath3, mode="a", encoding="cp932") as f:
        f.write(data_lines)



