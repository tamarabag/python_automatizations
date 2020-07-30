# Downloads Folder Organizer
# Automatization: organices files in the download folder
# rearengin them into specific folders depending on its type

# there are many extentions missing,
# as this is the first iteration.


import os
import shutil


def main():
    newFolder = ''
    srcFolder = '/Users/tamara/Downloads'
    dstFolder = '/Users/tamara/Downloads/'

    for filename in os.listdir(srcFolder):

        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png') or filename.endswith('.gif'):
            newFolder = '*Images*'
            if not os.path.exists(dstFolder + newFolder):
                os.mkdir(dstFolder + newFolder)
            shutil.move(srcFolder+'/'+filename, dstFolder +
                        newFolder + '/'+filename)

        elif filename.endswith('.mov'):
            newFolder = '*Videos*'
            if not os.path.exists(dstFolder + newFolder):
                os.mkdir(dstFolder + newFolder)
            shutil.move(srcFolder+'/'+filename, dstFolder +
                        newFolder + '/'+filename)

        elif filename.endswith('.apk'):
            newFolder = '*APKs*'
            if not os.path.exists(dstFolder + newFolder):
                os.mkdir(dstFolder + newFolder)
            shutil.move(srcFolder+'/'+filename, dstFolder +
                        newFolder + '/'+filename)

        elif filename.endswith('.wav') or filename.endswith('.mp3'):
            newFolder = '*Audios*'
            if not os.path.exists(dstFolder + newFolder):
                os.mkdir(dstFolder + newFolder)
            shutil.move(srcFolder+'/'+filename, dstFolder +
                        newFolder + '/'+filename)

        elif filename.endswith('.zip') or filename.endswith('.rar'):
            newFolder = '*Compressed*'
            if not os.path.exists(dstFolder + newFolder):
                os.mkdir(dstFolder + newFolder)
            shutil.move(srcFolder+'/'+filename, dstFolder +
                        newFolder + '/'+filename)

        elif filename.endswith('.pdf') or filename.endswith('.PDF'):
            newFolder = '*PDFs*'
            if not os.path.exists(dstFolder + newFolder):
                os.mkdir(dstFolder + newFolder)
            shutil.move(srcFolder+'/'+filename, dstFolder +
                        newFolder + '/'+filename)

        elif filename.endswith('.doc') or filename.endswith('.docx'):
            newFolder = '*Docs*'
            if not os.path.exists(dstFolder + newFolder):
                os.mkdir(dstFolder + newFolder)
            shutil.move(srcFolder+'/'+filename, dstFolder +
                        newFolder + '/'+filename)

        elif filename.endswith('.xlm'):
            newFolder = '*Excel*'
            if not os.path.exists(dstFolder + newFolder):
                os.mkdir(dstFolder + newFolder)
            shutil.move(srcFolder+'/'+filename, dstFolder +
                        newFolder + '/'+filename)

        elif filename.endswith('.html') or filename.endswith('.py') or filename.endswith('.css') or filename.endswith('.js'):
            newFolder = '*Code*'
            if not os.path.exists(dstFolder + newFolder):
                os.mkdir(dstFolder + newFolder)
            shutil.move(srcFolder+'/'+filename, dstFolder +
                        newFolder + '/'+filename)

        elif os.path.isdir(srcFolder + '/' + filename) and not filename.startswith('*'):
            newFolder = '*Folders*'
            if not os.path.exists(dstFolder + newFolder):
                os.mkdir(dstFolder + newFolder)
            shutil.move(srcFolder+'/'+filename, dstFolder +
                        newFolder + '/'+filename)

        else:
            if not filename.startswith('*'):
                newFolder = '*Miscellaneous*'
                if not os.path.exists(dstFolder + newFolder):
                    os.mkdir(dstFolder + newFolder)
                shutil.move(srcFolder+'/'+filename, dstFolder +
                            newFolder + '/'+filename)

    print('The organization is finished.')


if __name__ == "__main__":
    main()
