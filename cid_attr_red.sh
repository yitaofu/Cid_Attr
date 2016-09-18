#!/bin/bash

awk -F"\t" 'BEGIN{
	count = 1
}{
	if (NR == 1){
		precid = $1;
		preattr = $2;
		preval = $4;

		len = split(preval, vals, "AND");
		for (i = 1; i <= len; i++){
			v = vals[i];
			if (v == ""){
				continue;
			}
			valDict[v] = 1;
		}
		print "--"count"--";
	}else{
		cid = $1;
		attr = $2;
		val = $4;

		len = split(val, vals, "AND");
		if (cid != precid){
			tempVal = "";
			for (v in valDict){
				tempVal = tempVal"|"v;
			}
			print precid"\t"preattr"\t"tempVal;
			print "-------------------";
			count = count +	1;
			print "--"count"--";

			precid = cid;
			preattr = attr;
			delete valDict;
			for (i = 1; i <= len; i++){
				v = vals[i];
				if (v == ""){
					continue;
				}
				valDict[v] = 1;
			}
		}else{
			if (attr != preattr){
				tempVal = "";
				for (v in valDict){
					tempVal = tempVal"|"v;
				}
				print precid"\t"preattr"\t"tempVal;
				preattr = attr;
				delete valDict;
				for (i = 1; i <= len; i++){
					v = vals[i];
					if (v == ""){
						continue;
					}
					valDict[v] = 1;
				}
			}else{
				for (i = 1; i <= len; i++){
					v = vals[i];
					if (v == ""){
						continue;
					}
					valDict[v] = 1;
				}
			}
		}
	}
}END{
	tempVal = "";
	for (v in valDict){
		tempVal = tempVal"|"v;
	}
	print precid"\t"preattr"\t"tempVal;
	print "-------------------";
		
}'
