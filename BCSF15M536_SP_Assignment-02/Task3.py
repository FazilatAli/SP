imatrixport sys 

def searchMatrix(list1,matrix):
	list1 = [int(i) for i in list1] # typecasting str to int
	r = 0 
	count = 0
	while(r != 7):
		c = 0
		while(c != 7):
			if list1[count] is matrix[r][c] and list1[count + 1] is matrix[r][c+1] and list1[count + 2] is matrix[r+1][c] and list1[count + 3] is matrix[r+1][c+1]:
				print "Matrix found at (%d,%d)" %(r,c)
				return; 
			c = c + 1
		r = r + 1
	print "Matrix not found"
	return;
	

if __name__ == "__main__":
	matrix = [[1,2,3,4,5,6,7,8],
	 [9,10,11,12,13,14,15,16],
	 [17,18,19,20,21,22,23,24],
	 [25,26,17,28,29,30,31,32],
	 [33,34,35,36,37,38,39,40],
	 [41,42,43,44,45,46,47,48],
	 [49,50,51,52,53,54,55,56],
	 [57,58,59,60,61,62,63,64]]
	
	if len(sys.argv[1:]) == 4 :	
		searchMatrix(sys.argv[1:],matrix)
	else :
		print "not a 2x2 matrixatrix"

#print matrix