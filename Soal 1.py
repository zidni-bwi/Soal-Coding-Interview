kata = "basi"

def terbalik(kata):
    kata0 = ""
    for i in kata:
        kata0 = i + kata0
    return kata0

if kata == terbalik(kata):
    print("Kata: "+kata)
    print("Kebalikan: "+terbalik(kata))
    print("Hasil : true")
else:
    print("Kata: "+kata)
    print("Kebalikan: "+terbalik(kata))
    print("Hasil : false")
