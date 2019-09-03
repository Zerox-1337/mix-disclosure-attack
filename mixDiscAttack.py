import numpy as np
import scipy as sp
import time
import random

"""
get receivers list (a batch) when Alice sends something.f= chance of Alice sending something


Increase variable of amount of batches everytime it's called. To compare how long it takes.

b will be amount of messages
"""

def mix(N, b, m, n, f): 
	aliceSends = random.randint(0, 1000000);
	alice = 0;
	if (f >= aliceSends):
		alice = 1;
	if (alice == 0):
		receiverList = [random.randint(1, N)];
		for i in range(0, n):
			receiverList.append(random.randint(max(m) +1, N))
	else: 
		aliceComPartner = m[random.randint(0, len(m) -1)]
		receiverList = [aliceComPartner] 

		for i in range(0, n-1):
			receiverList.append(random.randint(2, N))
	


	return receiverList, alice
	
"""
returns 0 while not being finished.
"""
def intersection(arrayList1, arrayList2):
	return list(set(arrayList1) & set(arrayList2));

def excluding_phase(batchList, N,b,m,n,f):
	batchesChecked = 0;
	loopPhase = 0;
	while (loopPhase == 0):
		batch, alice = mix(N, b, m, n, f);
		batchesChecked += 1;
		if (alice == 1):
			intersectionsFound = 0;
			intersectionFirstIndex = 0;
			endLoop = 1;
			for i in range(0, len(batchList)):
				if (len(batchList[i]) > 1):
					endLoop = 0;
				intersectionValues = intersection(batchList[i], batch)
				if (intersectionValues != []):
					intersectionsFound += 1;
					if (intersectionsFound == 1):
						intersectionFirstIndex = i;
						intersectionFirstValue = intersectionValues;
			if(intersectionsFound == 1):
				batchList[intersectionFirstIndex] = intersectionFirstValue;
			if (endLoop == 1):
				loopPhase = 1;		
	
	return batchesChecked;



def learning_phase(batchList, N, b, m, n, f):
	batchesChecked = 0;

	while (len(batchList) < len(m)):
		batch, alice = mix(N, b, m, n, f);
		if (alice == 1):
			if (len(batchList) == 0):
				batchList.append(batch);
			else:
			
				appendNot = 0;
				for i in range(0, len(batchList)):

					if (intersection(batchList[i], batch) != []):
						appendNot = 1;
				if (appendNot == 0):
					batchList.append(batch);

		batchesChecked += 1;
	return batchesChecked;


	
def disclosureAttack(N,b, m, n, f):
	batchesChecked = 0;
	batchList = [];
	batchesChecked += learning_phase(batchList, N, b, m, n, f);
	batchesChecked += excluding_phase(batchList, N,b,m,n,f);
	print(batchesChecked);
	return batchesChecked;


nIncreasing = [];
for i in range(0, 100):
	print(i);
	nIncreasing.append(disclosureAttack(100000 +100*i, 10, [2,3,4,5,6,7,8,9], 34, 1000000));
print(nIncreasing);
print("done");
