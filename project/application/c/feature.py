def mean(a,b): 
	return (a+b)/2

def median(numb):
    sort = sorted(numb)
    length = len(sort)
    if length % 2 == 0:
        mid1 = sort[length // 2 - 1]
        mid2 = sort[length // 2]
        median = (mid1 + mid2) / 2
    else:
        median = sort[length // 2]
    return median

def numb_count(numb):
    numb_dict = {}
    for i in numb:
        if i in numb_dict:
            numb_dict[i] += 1
        else:
            numb_dict[i] = 1
    return numb_dict

def mode(numb):
    numb_dict = numb_count(numb)
    max_key = max(numb_dict, key=numb_dict.get)
    return max_key



	
