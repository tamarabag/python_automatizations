# Python 3 code to rename multiple files on a folder

# importing os module
import os

# Function to rename multiple files


def main():
    i = 0

    for filename in os.listdir("img"):
        dst = "picture_rnm" + str(i) + ".jpg"
        src = 'img/' + filename
        dst = 'img_rnm/' + dst

        os.rename(src, dst)
        i += 1


# Driver Code
if __name__ == '__main__':
    main()
