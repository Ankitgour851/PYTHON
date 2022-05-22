import os

def createifnotexist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername,files):  
    for file in files:
        os.replace(file, f"{foldername}/{file}")


files = os.listdir()
files.remove('main.py')
print(files)

createifnotexist('Images')
createifnotexist('Media')
createifnotexist('Docs')
createifnotexist('others')


imgExts=['.jpg','.png','.jpeg']
images = [file for file  in files if os.path.splitext(file)[1].lower() in imgExts]

docExts = ['.txt','.doc','.docx','.pdf']
docs =  [file for file  in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts = ['.mp4','.mp3']
medias =  [file for file  in files if os.path.splitext(file)[1].lower() in mediaExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
        others.append(file)

move("Images",images)
move("Docs",docs)
move("Media",medias)
move("others",others)
