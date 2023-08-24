from datetime import datetime
import time

def util(d):
	result = []
	for i in d:
		n = len(d[i])
		if n >=2:
			frst_executed_time = d[i][0]
			sec_executed_time = d[i][1]
			diff = (sec_executed_time - frst_executed_time ).total_seconds() / 60.0
			
			#print(type(diff))
			flag = 1
			j = 2
			while(j < n and flag == 1):
				temp_diff = (d[i][j] - d[i][j-1]).total_seconds() / 60.0
				
				if temp_diff != diff:
					flag = 0
				j+=1
			if flag:
				result.append(i+" which will execute at every "+ str(diff) + " minutes")
	if len(result) == 0:
		print("No cronjob found")
	else:
		print("These are the possible cronjobs!\n \n")
		for i in result:
			print('[*] ' + i)				
		
		
def identify_possible_cronjob(ip):
	l = ip.split("\n")
	fmt = '%Y/%m/%d %H:%M:%S'
	d = {}
	for i in l:
		
		t = i.split(" ")
		if len(t) < 2:
			continue
		time = datetime.strptime(t[0]+" "+t[1], fmt)
		script = i.split(" | ")[-1]
		
		
		if script in d:
			d[script].append(time)
		else:
			d[script] = [time]
	
	util(d)
with open('result.txt') as f:
    ip = f.read()

identify_possible_cronjob(ip)

