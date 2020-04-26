def counter():
    for i in range(99, -1, -1):
        if i == 0:
            print('No more bottles of beer on the wall, no more bottles of beer')
            print('Go to the store and buy some more, 99 bottles of beer on the wall')
        if i == 1:
            print ('One more bottle of beer on the wall, one more bottle of beer')
            print ('Take one down and pass it around, no more bottles of beer on the wall')
        if i > 1:
            print(i,' bottles of beer on the wall, ' + str(i) + ' more bottles of beer')
            print('take one down and pass it around, '+ str(i-1) +  ' bottles of beer on the wall')


    
