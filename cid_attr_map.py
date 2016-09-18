#! /usr/bin/env python

import sys, codecs, locale

#sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
cid_attr = {}
cid_attr_val = {}
for line in sys.stdin:
	rec = line.strip().split("\t")
	if len(rec) < 4:
		continue
	cid = rec[0]
	attr = rec[2]
	val = rec[3]
	cid_attr_str = cid + " " + attr

	if cid in cid_attr:
		if attr in cid_attr[cid]:
			cid_attr[cid][attr] = cid_attr[cid][attr] + 1
		else:
			cid_attr[cid][attr] = 1
	else:
		cid_attr[cid] = {}
		cid_attr[cid][attr] = 1

	if cid_attr_str in cid_attr_val:
		if val in cid_attr_val[cid_attr_str]:
			cid_attr_val[cid_attr_str][val] = cid_attr_val[cid_attr_str][val] + 1
		else:
			cid_attr_val[cid_attr_str][val] = 1
	else:
		cid_attr_val[cid_attr_str] = {}
		cid_attr_val[cid_attr_str][val] = 1

for cid in cid_attr:
	for attr in cid_attr[cid]:
		cid_attr_str = cid + " " + attr
		valstr = ""
		for val in cid_attr_val[cid_attr_str]:
			valstr = valstr + val + "AND"
		print ("%s\t%s\t%s\t%s" %(cid, attr, cid_attr[cid][attr], valstr))
