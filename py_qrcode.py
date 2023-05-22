import pyqrcode 

def qr_code():
    s='https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'
    d=pyqrcode.create(s)
    d.png('my_img.png',scale=6)
    print('Code Excecuted Proprly')

if __name__ == '__main__':
    qr_code()