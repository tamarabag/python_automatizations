# listing filenames into a csv
# importing os module
import os
import csv

# Function to make a list with filenames and create a csv


def main():
    i = 0
    names = []
    srcFolder = "img_rnm"
    for filename in os.listdir(srcFolder):
        names.append(filename)
        i += 1

# 'w': crea el archivo si no existe y me lo sobre escribe si existe
# 'a': Opens a file for appending at the end of the file.
    with open('file_names.csv', 'w') as csvFile:
        writer = csv.writer(csvFile, dialect='excel', delimiter='\n')
        # writer.write('List of Files in {} Folder'.format(srcFolder))
        writer.writerow(names)
        csvFile.close()

    print('The file has been updated :)')


# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
