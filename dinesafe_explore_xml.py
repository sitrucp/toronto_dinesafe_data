import xml.etree.ElementTree as ET

doc = ET.parse('C:/Users/bb/Documents/Dropbox/Data analysis/\
City of Toronto/dinesafe.xml')
rows = doc.findall('ROW')

for row in rows:
    print row.find('ESTABLISHMENT_NAME').text, ',' , \
    row.find('ESTABLISHMENT_STATUS').text, ',' , \
    row.find('SEVERITY').text, ',' , \
    row.find('ACTION').text, ',' , \
    row.find('INSPECTION_DATE').text, ',' , \
    row.find('ESTABLISHMENT_ADDRESS').text
