# Function for getting of regions list
import string

brains=context.portal_catalog.searchResults({'portal_type' : ('region',) })

print "[" + ' ' 

for b in brains:
 print "{"
 o=b.getObject()
 print '"id":"%s",' % b.getURL()
 print '"title":"%s",' % o.title
 print '"desription":"%s",' % o.description
 print '"geometry":"%s' %b.getURL() + '/@@geo-json.json''"'
 print "},"

return printed[:-2] + '\n' + "]"