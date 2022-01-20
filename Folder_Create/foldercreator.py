import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials 
 
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

#フォルダーパスを記入
corepath ="C:\\Users\\koyos\\Desktop\\Forge\\tool\\upload_file\\Folder_Create\\" 
# 秘密鍵（JSONファイル）のファイル名を入力
credentials = ServiceAccountCredentials.from_json_keyfile_name(corepath + "key\\minecraftforge.json", scope)
gc = gspread.authorize(credentials)

#Google スプレッドシート名
wb = gc.open('Minecraft_Nijisanji_Mod')
ws = wb.get_worksheet(0)
#2列目をすべて取得　この文字列分変換してコードを作成します
col_list = ws.col_values(2)

for sheetvalue in col_list:
    print(sheetvalue)
    OldWord = 'Test'
    NewWord = sheetvalue
    BigOldWord = OldWord.upper()
    BigNewWord = NewWord.upper()
    SmallOldWord = OldWord.lower()
    SmallNewWord = NewWord.lower()
    #フォルダコピー
    import shutil
    shutil.copytree(corepath + OldWord,corepath + NewWord)


    #ファイル名変更
    #entity コピー
    BaseEntityFile = corepath + NewWord + '\\' + OldWord + '.java' 
    NewEntityFile = corepath + NewWord + '\\' + NewWord + '.java'
    os.rename(BaseEntityFile, NewEntityFile)

    #model コピー
    BaseModelFile = corepath + NewWord +'\\'+ OldWord + 'Model.java' 
    NewModelFile= corepath + NewWord +'\\'+ NewWord + 'Model.java'
    os.rename(BaseModelFile, NewModelFile)

    #renderer コピー
    BaseRendererFile  =corepath + NewWord +'\\'+ OldWord + 'Renderer.java'
    NewRendererFile  = corepath +NewWord +'\\'+ NewWord +'Renderer.java'
    os.rename(BaseRendererFile, NewRendererFile)



    #ファイル内文字列変換
    #EntityFile置換
    with open(NewEntityFile, encoding="cp932") as f:
        data_lines = f.read()
    data_lines = data_lines.replace(OldWord, NewWord).replace(BigOldWord, BigNewWord).replace(SmallOldWord, SmallNewWord)
    with open(NewEntityFile, mode="w", encoding="cp932") as f:
        f.write(data_lines)

    #ModelFile置換
    with open(NewModelFile, encoding="cp932") as f:
        data_lines = f.read()
    data_lines = data_lines.replace(OldWord, NewWord).replace(BigOldWord, BigNewWord).replace(SmallOldWord, SmallNewWord)
    with open(NewModelFile, mode="w", encoding="cp932") as f:
        f.write(data_lines)

    #RendererFile置換
    with open(NewRendererFile, encoding="cp932") as f:
        data_lines = f.read()
    data_lines = data_lines.replace(OldWord, NewWord).replace(BigOldWord, BigNewWord).replace(SmallOldWord, SmallNewWord)
    with open(NewRendererFile, mode="w", encoding="cp932") as f:
        f.write(data_lines)

