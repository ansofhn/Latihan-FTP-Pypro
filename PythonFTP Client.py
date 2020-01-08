import ftplib

print("","="*18,"\n","PYTHON FTP PROGRAM","\n","="*18,"\n")
ftp=ftplib.FTP("")
ip=input("Input IP FTP Server     : ")
port=int(input("Input PORT FTP Server   : "))
print("\n"+"="*25)
user=input("USERNAME    : ")
paswd=input("PASSWORD    : ")
print("="*25,"\n")
ftp.connect(ip,port)
ftp.login(user,paswd)
while True:
    print("","="*15,"\n","< SERVER FILE >","\n","="*15,"\n")
    ftp.retrlines("LIST")

    print("\n",">> 1. Download","\n",">> 2. Upload","\n",">> 3. Exit","\n")
    pilihan=int(input("What Do You Want? (1-3): "))

    if pilihan== 1:
        def downloadfile():
            filename = input("Pick From Server  : ")
            localfile = open(filename, 'wb')
            ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
            print("Download Finished")
            localfile.close()
        downloadfile()
    elif pilihan== 2:
        def uploadfile():
            filename = input("Pick Your File    : ")
            ftp.storbinary('STOR '+filename, open(filename, 'rb'))
            print("Upload Finished")
        uploadfile()
    else:
        print("Program Finished")
        ftp.close()
        break