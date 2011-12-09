# -*- encoding: utf-8 -*-

import csv

csvpath = "/home/resteve/Escriptori/oerp2tryton/zip/"
zipcsv = "municipios_cpostal.csv"
separator_zip = ";"
zipsubdivision = "zip_spain.csv"
separator_sub = ","

csvzip = open(csvpath+zipcsv, "r")
csvsub = open(csvpath+zipsubdivision, "r")

zip_codes = {}
for csvsub in csvsub.readlines():
    csvsub_line = csvsub.replace('\n', '')
    csvsub_line = csvsub_line.split(separator_sub)
    zip_codes[csvsub_line[1]] = csvsub_line[2]

print "<?xml version=\"1.0\"?>"
print "<tryton>"
print "    <data>"

#~ print zip_codes
i = 0
zip_history = []
for csvzip in csvzip.readlines():
    csvzip_line = csvzip.replace('\n', '')
    csvzip_line = csvzip_line.split(separator_zip)
    zip = csvzip_line[0]
    # delete zip if is created because XML only need a unique id
    if zip not in zip_history:
        zip_prefix = str(csvzip_line[0])[:2]
        subdivision = zip_codes[zip_prefix]
        print "%s - %s - %s" % (csvzip_line[0], csvzip_line[1], subdivision)
        print "        <record model=\"country.zip\" id=\"es-%s\">" % (csvzip_line[0])
        print "            <field name=\"zip\">ES%s</field>" % (zip)
        print "            <field name=\"city\">%s</field>" % (csvzip_line[1])
        print "            <field name=\"subdivision\" ref=\"country.%s\"/>" % (subdivision)
        print "        </record>"
        zip_codes[csvsub_line[1]] = csvsub_line[0]
    #~ else:
        #~ i = i+1
        #~ print i
    zip_history.append(zip)

print "    </data>"
print "</tryton>"
