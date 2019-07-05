import xml.dom.minidom
import os

path = os.getcwd() + '/ancora-3.0.1es'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.xml' in file:
            files.append(os.path.join(r, file))

def getWord(node):
    oracion = ""
    for parent in node.childNodes:
        if parent.nodeType != parent.TEXT_NODE:
            if parent.getAttribute("wd") != "":
                oracion += parent.getAttribute("wd") + " "
            else:
                oracion += getWord(parent)
    
    return oracion

for i, f in enumerate(files):
    
    path2 = f.replace("ancora-3.0.1es", "raw")
    name2 = path2.replace(".xml", ".txt")
    if not os.path.exists(os.path.dirname(name2)):
        os.makedirs(os.path.dirname(name2))
    
    print name2 + "\n" 

    file2 = open(name2, "a+")

    doc = xml.dom.minidom.parse(f);
    sentence = doc.getElementsByTagName("sentence")
    for tag in sentence:
        #print getWord(tag)
        file2.write(getWord(tag).encode('utf8') + "\n")
    
    file2.close()
