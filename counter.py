import os
dosyalar = []
output = os.popen("dir").read().split('\n')
print(f"\nDosya yolu: {output[3].split(' ')[-1]}")
print("Bu dosya yolunda bulunan dosyalar şunlardır:")

for i in output[7:-3]:
    dosya=(i.split(' ')[-1])
    if not dosya.endswith('.py') and not dosya.startswith('results_'):
        print(f' > {len(dosyalar)+1}. {dosya}')
print("\nBir dosya üzerinde sayım işlemi yapmak için dosyanın ismini ya da belirttiğimiz sırasını yazınız.")

# with open(selectedfile, 'r') as fd:
    # print(