from pprint import pprint

try:
    import understand as und
except ImportError:
    print("Can not import understand")

db = und.open("D:\Dev\JavaSample\JavaSample1.udb")

ent = db.lookup("Admin", "class")[0]

print(ent, ent.kind())
for i in ent.ents(""):
    print(i)
