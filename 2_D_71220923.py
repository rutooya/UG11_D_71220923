kata = input("Masukkan kata: ")

def cetakHuruf():
    list = (kata)
    len(kata)
    if(len(kata)%2==0):
        print("Huruf paling ujung pada kata", kata, "adalah", (kata[-3:]))
    else:
        print("Huruf paling ujung pada kata", kata, "adalah", (kata[:3]))
cetakHuruf()
