# 3 conns, and extend timeout to 500 for demo (in debugger)
AdminConfig.modify('(cells/DefaultCell01|resources.xml#ConnectionPool_1543005577211)', '[[connectionTimeout "500"] [maxConnections "3"] [unusedTimeout "1800"] [minConnections "0"] [agedTimeout "0"] [purgePolicy "EntirePool"] [reapTime "180"]]') 

print "Saving"
AdminConfig.save()

