#!/usr/bin/env python

import sys, codecs, locale
 
#sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
cid_attr = {}
cid_attr_val = {}
cid_total_num = {}
for line in sys.stdin:
	rec = line.strip().split("\t")
	if len(rec) < 4:
		continue
	cid = rec[0]
	attr = rec[1]
	num = rec[2]
	val = rec[3]
	#
	if cid in cid_total_num:
		cid_total_num[cid] = cid_total_num[cid] + int(num)
	else:
		cid_total_num[cid] = int(num)
	#
	if cid in cid_attr:
		if attr in cid_attr[cid]:
			cid_attr[cid][attr] = cid_attr[cid][attr] + int(num)
		else:
			cid_attr[cid][attr] = int(num)
	else:
		cid_attr[cid] = {}
		cid_attr[cid][attr] = int(num)
	#
	cid_attr_str = cid + " " + attr
	vals = val.split("AND")
	if len(vals) >= 1:
		if cid_attr_str in cid_attr_val:
			for v in vals:
				if v == "":
					continue
				cid_attr_val[cid_attr_str][v] = 1
#				tempStr = v.split("&*|()")
#				if len(tempStr) < 2:
#					continue
#				tempVal = tempStr[0]
#				tempNum = tempStr[1]
#				if not isinstance(int(tempNum), int):
#					continue
#				if tempVal in cid_attr_val[cid_attr_str]:
#					cid_attr_val[cid_attr_str][tempVal] = cid_attr_val[cid_attr_str][tempVal] + int(tempNum)
#				else:
#					cid_attr_val[cid_attr_str][tempVal] = int(tempNum)
		else:
			cid_attr_val[cid_attr_str] = {}
			for v in vals:
				if v == "":
					continue
				cid_attr_val[cid_attr_str][v] = 1
#				tempStr = v.split("&*|()")
#				if len(tempStr) < 2:
#					continue
#				tempVal = tempStr[0]
#				tempNum = tempStr[1]
#				if not isinstance(int(tempNum), int):
#					continue
#				cid_attr_val[cid_attr_str][tempVal] = int(tempNum)
	
count = 1

#temp_cid_attr = {}
#for cid in cid_attr:
#	temp_cid_attr[cid] = {}
#	for attr in cid_attr[cid]:
#		temp_cid_attr[cid][attr] = cid_attr[cid][attr]

for cid in cid_attr:
	print "--" + str(count) + "--: " + str(cid_total_num[cid])
	count = count + 1
	
	orderAttr = []	
	for i in range(len(cid_attr[cid])):
		maxscore = -1
		for attr in cid_attr[cid]:
			if cid_attr[cid][attr] > maxscore:
				maxscore = cid_attr[cid][attr]
				maxattr = attr
		temp_MAX = maxattr + "\t" + str(maxscore)
		orderAttr.append(temp_MAX)
		cid_attr[cid][maxattr] = -1
	
	for i in range(len(orderAttr)):
		attr_score = orderAttr[i]
		attr, score = attr_score.split("\t")
		cid_attr_str = cid + " " + attr
		vals = cid_attr_val[cid_attr_str]
		valstr = ""
		for val in vals:
			if val == "":
				continue
			valstr = valstr + "|" + val
		
		print ("%s\t%s\t%s\t%s" %(cid, attr, score, valstr))
	print "---------------------------------------------------"
