import argparse
import os
import subprocess
import sys
import requests
import socket
from bs4 import BeautifulSoup
import time

hijau = "\033[1;92m"
putih = "\033[1;97m"
abu = "\033[1;90m"
kuning = "\033[1;93m"
ungu = "\033[1;95m"
merah = "\033[1;91m"
biru = "\033[1;96m"

required_modules = ['argparse', 'requests', 'socket', 'time']

def modules():
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            print(f"Modul {module} belum di intall beruntung gw baik ge installin ok")
            wasu(f'{biru}Install.........{putih}')
            os.system(f"pip install {module}")
            os.system(f"pip install -r asu.txt")
            

def judul(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string
            return title
        else:
            print(f"{merah}Gak ada judul kayanya nih webnya bro soalnya requestnya ", response.status_code, "bro!!", putih)
            return None
    except Exception as e:
        print("Error:", e)
        return None

def banternet():
    try:
        socket.create_connection(('www.google.com', 80))
        return True
    except OSError:
        return False

def wasu(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.050)

def kirik(url):
    if not banternet():
        wasu(f'{merah}Elu Kaga Ada Akses Internet Cuuyyyy Coba Sambungin Dulu Terus Jalanin Lagi Ya Asu (: {putih}')
        sys.exit()
    
    manuk = ["wget","--recursive","--no-clobber","--page-requisites","--html-extension","--convert-links","--restrict-file-names=windows","--no-parent","-erobots=off",url]
    subprocess.call(manuk)

     
def main():
    parser = argparse.ArgumentParser(description="Copy-Web by adyfas Ganteng (:")
    parser.add_argument("--wasu", dest="url", help="Jadi tuh gini jadinya nya tuh anunya itu jadi ini ya udah jadi ini gitu anunya tuh gitu....")
    parser.add_argument("--kabeh", dest="file", help="File.txt yang berisi URL-URL")
    parser.add_argument("--langsung", dest="path", help="Direktori tempat file.txt berada misalkan file.txt kamu di direktori system/file/file.txt gitu yaa paham yaa")
    args = parser.parse_args()

    if not banternet():
        wasu(f'{merah}Elu Kaga Ada Akses Internet Cuuyyyy Coba Sambungin Dulu Terus Jalanin Lagi Ya Asu (: {putih}')
        sys.exit()

   
    if args.url:
        title = judul(args.url)
        if title:
            print('-'*15)
            print(f"\n\n{biru}ouh ini nama halamannya:{putih}", title, "\n")
            kirik(args.url)
    elif args.file:
        if os.path.exists(args.file):
            with open(args.file, 'r') as f:
                for line in f:
                    url = line.strip()
                    title = judul(url)
                    if title:
                        print('-'*15)
                        print(f"\n\n{biru}ouh ini nama halamannya:{putih}", title, "\n")
                        kirik(url)
        else:
            wasu(f"{merah}File '{args.file}' Waduhh Kamu ini tuh coba tulis nama filenya yang bener coyyyy{putih}")
    elif args.path:
        file_path = os.path.join(args.path, 'file.txt')
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                for line in f:
                    url = line.strip()
                    title = judul(url)
                    if title:
                        print('-'*25)
                        print(f"\n\n{biru}ouh ini nama halamannya:{putih}", title, "\n")
                        kirik(url)
        else:
            wasu(f"{merah}File '{file_path}' jihh GJ anda ini coba deh cek lagi itu pasti ada yang salah coyyy{putih}")
    else:
        parser.print_help()

if __name__ == "__main__":
    modules()
    main()
