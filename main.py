#  Create by adyfas
#  https://github.com/adyfas
#  For fun (:


import socket
import json
import requests
from bs4 import BeautifulSoup
import argparse

def dapatkan_info_ip(alamat_ip):
    url_info_ip = f"https://ipinfo.io/{alamat_ip}/json"
    respons = requests.get(url_info_ip)
    info_ip = json.loads(respons.text)
    return info_ip

def tampilkan_info_ip(info_ip):
    print("\nInformasi IP:")
    for kunci, nilai in info_ip.items():
        print(f"{kunci}: {nilai}")

def dapatkan_konten_web(url):
    respons = requests.get(url)
    return respons.text

def simpan_ke_file(konten, nama_file):
    with open(nama_file, 'w', encoding='utf-8') as file:
        file.write(konten)

def dapatkan_header_keamanan(url):
    respons = requests.get(url)
    header = respons.headers
    header_keamanan = header.get('X-Swag-Security', 'Header Tidak Ditemukan')
    return header_keamanan

def utama():
    parser = argparse.ArgumentParser(description='Ambil konten web dan header keamanan.')
    parser.add_argument('-w', '--website', help='URL Website atau URL phissing yang ingin kalian lihat kodenya', required=True)
    args = parser.parse_args()

    konten_web = dapatkan_konten_web(args.website)
    header_keamanan = dapatkan_header_keamanan(args.website)

    print("Konten Web, bro:")
    print(konten_web)

    print("\nHeader Keamanan, kekinian banget:")
    print(header_keamanan)

    soup = BeautifulSoup(konten_web, 'html.parser')
    konten_html = soup.prettify()
    nama_file_html = "output.html"
    simpan_ke_file(konten_html, nama_file_html)
    print(f"\nHTML disimpan di: {nama_file_html}")
    nama_file_css = "output.css"
    konten_css = '\n'.join([tag_style.text for tag_style in soup.find_all('style')])
    simpan_ke_file(konten_css, nama_file_css)
    print(f"CSS disimpan di: {nama_file_css}")
    nama_file_js = "output.js"
    konten_js = '\n'.join([tag_script.text for tag_script in soup.find_all('script')])
    simpan_ke_file(konten_js, nama_file_js)
    print(f"JavaScript disimpan di: {nama_file_js}")
    
    alamat_ip = socket.gethostbyname(args.website.split('//')[1].split('/')[0])
    print(f"\nAlamat IP: {alamat_ip}")
    info_ip = dapatkan_info_ip(alamat_ip)
    tampilkan_info_ip(info_ip)

if __name__ == "__main__":
    utama()