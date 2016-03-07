"""
Create a 'destino.vcf' from a file.csv with contacts
file.csv have the formart 'name,email'
"""

print "Criando arquivo...."
with open('file.csv', 'r') as f:
    for line in f:
        with open('destino.vcf', 'a') as meudestino:
            meudestino.write("BEGIN:VCARD\n")
            meudestino.write("VERSION:3.0\n")
            meudestino.write("N:" + line.split(',')[0] + "\n")
            meudestino.write("FN:" + line.split(',')[0] + "\n")
            meudestino.write("EMAIL:" + line.split(',')[1]e)
            meudestino.write("END:VCARD\n")
