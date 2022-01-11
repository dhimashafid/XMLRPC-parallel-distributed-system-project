from xmlrpc.server import SimpleXMLRPCServer #import library xmlrpc server
import xmlrpc.client #import library xmlrpc client 

#fungsi file_upload akan digunakan di admin karena admin yang akan melakukan upload informasi boarding
# dan lokasi transit ke server 
def file_upload(filedata):
    try:
        if (filedata.data != open("/Users/dev/Documents/Sister/Tubes/server/upload.txt", "rb").read()):#ini untuk kondisi jika data yang
            #diupload berbeda dengan data yang sebelumnya 
            with open('/Users/dev/Documents/Sister/Tubes/server/upload.txt','wb') as handle:
            #lakukan write file yang akan diupload,wb adalah write binary(file ditulis secara binary) dan hubungkan pada handle    
                data=filedata.data 
                print('Data berhasil diperbarui')
                handle.write(data)
                return True
        else:#ini kondisi jika data sebelumnya sama maka tidak akan dilakukan upload lagi
            print('Data tidak diperbarui karena sama dengan sebelumnya !!!')
            return False
    except:
        #ini kondisi jika di server tidak ada data boarding atau kosong maka akan dilakukan upload dan akan muncul file upload.txt diserver
        with open('/Users/dev/Documents/Sister/Tubes/server/upload.txt','wb') as handle:
            #lakukan write file yang akan diupload,wb adalah write binary(file ditulis secara binary) dan hubungkan pada handle
            data=filedata.data 
            print('Data berhasil ditambahkan')
            handle.write(data)
            return True

def file_download():
    #fungsi file_download akan digunakan di client agar bisa menerima informasi jadwal boarding dan lokasi transit, karena 
    #client yang akan mendowload data boarding dan lokasi transit 
    with open('/Users/dev/Documents/Sister/Tubes/server/upload.txt','rb') as handle:
        #lakukan read file yang akan diupload,rb adalah read binary(file dibaca secara binary) dan hubungkan pada handle
        return xmlrpc.client.Binary(handle.read())
        handle.close()

server = SimpleXMLRPCServer(("127.0.0.1", 5005))#buat server

print ("Listening on port 5005")

server.register_function(file_upload, "upload")# register fungsi file_upload menjadi upload pada server
server.register_function(file_download, "download")# register fungsi file_download menjadi download pada server

server.serve_forever()# jalankan server
