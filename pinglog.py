secondHalf = None
firstHalf = 0
oldLine = ""
pinglog = open("pinglog.txt", "r")
results = open("results.txt", "w")
for pingLine in pinglog:
  xx = secondHalf
  if "icmp_seq=" in pingLine:
      firstHalf = pingLine.split("=",1)[1]
  if " ttl=" in pingLine:
      secondHalf = firstHalf.split(" ttl=",1)[0]
  if xx !=None and int(secondHalf) > int(xx) + 10:
      #print (xx + "-" + secondHalf)
      print (oldLine + pingLine)
      results.write(oldLine + pingLine + "----------" + '\n')
  oldLine = pingLine
results.close()
