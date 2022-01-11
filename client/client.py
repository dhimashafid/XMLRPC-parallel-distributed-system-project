import xmlrpc.client #gunakan library xmlrpc.client untuk bertindak sebagai client atau lebih tepatnya penumpang / pemesan tiket 

proxy = xmlrpc.client.ServerProxy("http://25.21.44.226:5005") #masukkan proxy berupa alamat ip server di device yang telah disambungkan di satu jaringan lokal(VPN)

try:
    if (proxy.download().data[:33] != open("C:\\Users\\DhimasHafid\\OneDrive - Telkom University\\Documents\\tubes\\client\\boarding.txt", "rb").read()):
    #panggil fungsi download yang sudah dituliskan pada server untuk melakukan download file yang sudah diupload oleh admin di server dan disimpan pada directory tertulis
    #file akan dibaca dengan membaca 33 string indeks pertama dengan dilakukan read binary terlebih dahulu
    #membaca apakah jam sama dengan data file sebelumnya atau tidak, jika kosong maka akan dijalankan 
        with open('C:\\Users\\DhimasHafid\\OneDrive - Telkom University\\Documents\\tubes\\client\\boarding.txt','wb') as handle: #membuka file boarding.txt untuk dituliskan jadwal boarding yang baru     
            handle.write(proxy.download().data[:33]) #menuliskan data boarding yang baru
            print('Data boarding telah diperbarui') #print Data boarding telah diperbarui
            handle.close() #selesai
    
    if (proxy.download().data[33:] != open("C:\\Users\\DhimasHafid\\OneDrive - Telkom University\\Documents\\tubes\\client\\lokasi.txt", "rb").read()):
       #panggil fungsi download yang sudah dituliskan pada server untuk melakukan download file yang sudah diupload oleh admin di server dan disimpan pada directory tertulis
       #file akan dibaca dengan membaca string setelah indeks ke-33 dengan dilakukan read binary terlebih dahulu
       #membaca apakah nama kota sama dengan data file sebelumnya atau tidak, jika kosong maka akan dijalankan
       with open('C:\\Users\\DhimasHafid\\OneDrive - Telkom University\\Documents\\tubes\\client\\lokasi.txt','wb') as handle:   #membuka file lokasi.txt untuk dituliskan lokasi boarding yang baru 
            handle.write(proxy.download().data[33:]) #menuliskan data boarding yang baru
            print('Data lokasi telah diperbarui') #print Data lokasi telah diperbarui
            handle.close()  #selesai
    
except: #kondisi yang lain selain kondisi yang ada diatas

    with open('C:\\Users\\DhimasHafid\\OneDrive - Telkom University\\Documents\\tubes\\client\\boarding.txt','wb') as handle: #membuka file boarding.txt   
        handle.write(proxy.download().data[:33]) #menambahkan data boarding 
        handle.close() #selesai   
        print('Data boarding telah ditambahkan') #print Data boarding telah ditambahkan

    with open('C:\\Users\\DhimasHafid\\OneDrive - Telkom University\\Documents\\tubes\\client\\lokasi.txt','wb') as handle:    #membuka file lokasi.txt
        handle.write(proxy.download().data[33:])#menambahkan lokasi boarding 
        handle.close()  #selesai 
        print('Data lokasi telah ditambahkan') #print Data lokasi telah ditambahkan