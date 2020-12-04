import os
import string
dosyalar = []
selectedfile = None

output = os.popen("dir").read().split('\n') #send a command 'dir'
print(f"\nDosya yolu: {output[3].split(' ')[-1]}") #print file direction
print("Bu dosya yolunda bulunan dosyalar şunlardır:")

for i in output[7:-3]: #print files in direction
    dosya=(i.split(' ')[-1])
    if not dosya.endswith('.py') and not dosya.startswith('results_') and dosya: #print only possible files
        print(f' > {len(dosyalar)+1}. {dosya}')
        dosyalar.append(dosya)

#Possible searchs for 2. Filename.txt: 2, 2., 2. file, filename, filename.txt, FiLenAm...
def checksel(sel, dosyalar):
    if sel.split('.')[0] in map(str,range(len(dosyalar)+1)): #check for 2, 2., 2.
        try:
            return(dosyalar[int(sel.split('.')[0])-1])
        except:
            None
    elif sel.lower() in map(str.lower,dosyalar): #check for filename.txt, fiLeNaMe.TXT...
        for i in dosyalar:
            if sel.lower() == i.lower():
                return(i)
    elif not any(char.isdigit() for char in sel) and not '.' in sel: #check for filename, fiLeNaM...
        results=[]
        for i in dosyalar:
            if i.lower().split('.')[0].startswith(sel.lower()):
                results.append(i)
        if len(results) == 1:
            return(results[0])
        elif len(results) >= 2: #if more than one filenam...
            for i in results:
                if sel.lower() == i.lower().split('.')[0]: #if one of these accually filenam.txt
                    return(i)
                else:
                    if i == results[-1]: #if no filenam.txt and more than one filenam...
                        print("\nBirden fazla sonuç bulundu. Lütfen daha seçmek istediğiniz dosyayı daha açık bir şekilde yazın.")
                        print("Bulunan sonuçlar: "+", ".join(map(str, dosyalar))+".")
    else:
        return(None)

while selectedfile is None: #selecting file
    sel = input("\nBir dosya üzerinde sayım işlemi yapmak için dosyanın ismini ya da belirttiğimiz sırasını yazınız.\n>")
    selectedfile = checksel(sel, dosyalar)
    if selectedfile is None and len(sel) != 1:
        if len(dosyalar) == 1:
            print(f"\n{sel}, bu doğrultuda bulunamadı. Klasörü kontrol ediniz.\nBelge: "+", ".join(map(str, dosyalar))+".")
        elif len(dosyalar) >= 2:
            print(f"\n{sel}, bu doğrultuda bulunamadı. Klasörü kontrol ediniz.\nBelge: "+", ".join(map(str, dosyalar))+".")
        elif len(dosyalar) == 0:
            print(f"\n{sel}, bu doğrultuda bulunamadı. Klasörünüzde zaten işlem yapılacak bir belge gözükmüyor.\nDosya Yolunuz:{output[3].split(' ')[-1]}")
    elif selectedfile is None and len(sel) != 1:
        print("Aranması için hiçbir şey girmediniz.")
print(selectedfile)

#sort method
def sortbydata(x):
  return (x[1])

#read file
with open(selectedfile, 'r') as fd:
    paragraph = 0
    sentence = 0
    word = 0
    letter = 0
    words = [["test",1]]
    for i in fd.read().split("\n"):
        if any(c.isalpha() for c in i):
            paragraph+=1
            sentence+=len(i.split("."))
            for s in i.split(" "):
                word += 1
                if s[-1] in string.ascii_letters+string.digits:
                    letter += len(s)
                    for c in range(len(words)):
                        if words[c][0] == s.lower():
                            words[c]=[s.lower(),words[c][1]+1]
                            break
                        elif c == len(words)-1:
                            words.append([s.lower(),1])
                            break
                elif s[-1] in string.punctuation and len(s)!=1:
                    letter += len(s)-1
                    s=s[:-1]
                    for c in range(len(words)):
                        if words[c][0] == s.lower():
                            words[c]=[s.lower(),words[c][1]+1]
                            break
                        elif c == len(words)-1:
                            words.append([s.lower(),1])
                            break
    #print datas
    with open(f"results_{selectedfile}", 'w') as fw:
        words=words[1:]
        words.sort(key=sortbydata)#sort
        words=words[::-1]
        for i in words[1:]:
            print(i[0].ljust(15)+f"({str(i[1]).zfill(2)})",end=":")
            fw.write(i[0].ljust(15)+f"({str(i[1]).zfill(2)}):")
            for a in range(i[1]):
                print("|", end="")
                fw.write("|")
            print()
            fw.write("\n")
        print(f"Bu metin {paragraph} Paragraf, {sentence} Cümle, {word} Kelime ve {letter} Harf içerir.")
        fw.write(f"Bu metin {paragraph} Paragraf, {sentence} Cümle, {word} Kelime ve {letter} Harf içerir.\n")
        print("Metin kaydedildi.")
        