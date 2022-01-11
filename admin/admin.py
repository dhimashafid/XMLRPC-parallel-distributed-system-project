import xmlrpc.client #gunakan library xmlrpc.client untuk bertindak sebagai admin 

proxy = xmlrpc.client.ServerProxy("http://25.21.44.226:5005") #masukkan proxy berupa alamat ip server di device yang telah disambungkan di satu jaringan lokal(VPN)

with open('C:\\Users\\DhimasHafid\OneDrive - Telkom University\\Documents\\tubes\\admin\\tiket2.txt','rb') as handle:
#lakukan read file yang akan diupload, rb adalah read binary (file dibaca secara binary) dan hubungkan pada handle untuk bisa melakukan read di baris selanjutnya

    file = xmlrpc.client.Binary(handle.read()) #file yang sudah dibaca disimpan dalam variable "file" untuk dibaca menggunakan library dan handle read
    handle.close()  #menghentikan operasi sebelumnya (read file) dan dilakukan decrement agar operasi sebelumnya benar benar berhenti

proxy.upload(file)  #prosedur untuk mengaktfikan / memanggil fungsi upload yang sudah dituliskan pada server

#admin bertugas untuk upload file boarding yang nantinya dikirim ke server dan diteruskan server ke client
#client akan mendownload file boarding yang telah diupload admin
