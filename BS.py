def bubble_improve(l):
    print l
    flag = 1
    for index in range(len(l) - 1, 0 , -1):
        if flag:
            flag = 0
            for two_index in range(index):
                if l[two_index] > l[two_index + 1]:
                    l[two_index], l[two_index + 1] = l[two_index + 1], l[two_index]
                    flag = 1
        else:
            break
    print l
    
l = [10, 20, 40, 50, 30, 60]
bubble_improve(l)
