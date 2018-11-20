import re
tfile = open("temp1.txt","w")
prodChk=0
sandChk=1
prodURL="http://localhost/prod"
sandURL="http://localhost/sand"
version="v1.0.1"
fileName="GITCRM--WorthinessUpgradeEligibiltyAPI_vv1.0.0.xml"
with open(fileName) as fp:
    line = fp.readline()
    tfile.write(line)
    while line:
        line = fp.readline()
#        line = fp.readline().replace('\n','')
        if (prodChk == 0 ):
            if re.search(r'version="v',line):
                verB=line.split("=")
                tfile.write(verB[0]+"=\""+version+"\"\n")
            elif re.search(r'productionEndpoint',line):
                prodChk=1
                tfile.write(line)
            else:
                tfile.write(line)
        elif (prodChk == 1 ):
            uri=line.split("=")
            tfile.write(uri[0]+"=\""+prodURL+"\">\n")
            prodChk=2
        elif (prodChk == 2 ):
            if re.search(r'ENDPOINT_ADDRESS',line):
                prop=line.split("=")
                tfile.write(prop[0]+"="+prop[1]+"=\""+prodURL+"\"/>\n")
                prodChk=3
                sandChk=2
            else:
                tfile.write(line)

        elif (sandChk == 2 ):
            if re.search(r'sandboxEndpoint',line):
                sandChk=3
                tfile.write(line)
            else:
                tfile.write(line)
        elif (sandChk == 3 ):
            uri=line.split("=")
            tfile.write(uri[0]+"=\""+sandURL+"\">\n")
            sandChk=4
        elif (sandChk == 4 ):
            if re.search(r'ENDPOINT_ADDRESS',line):
                sandp=line.split("=")
                tfile.write(sandp[0]+"="+sandp[1]+"=\""+sandURL+"\"/>\n")
                sandChk=5
            else:
                tfile.write(line)
        else:
            tfile.write(line)
#tfile.write(data)
tfile.close()

file = open("temp1.txt","r")
nFile = open(fileName, "w")
Synap = file.read()
nFile.write(Synap)
file.close()
nFile.close()
#print(Synap)


