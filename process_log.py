import numpy as np

f = open('casia_batchl2_log.txt')
line = f.readline()

num = 1
gar_list = []
while line:
    arr = line.split('  ')
    try:
        arr[1][0:3]
    except IndexError:
        pass
    else:
        if arr[1][0:3] == 'FAR':
            far = arr[1][4:12]
	    if float(far) == 0.000001:
	        gar_list.append(float(arr[2][4:12]))
    num += 1
    line = f.readline()

print num 
print '\n'
print max(gar_list)
print np.argmax(gar_list)
