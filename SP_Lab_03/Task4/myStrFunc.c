int isPalindrome(char *arr, int size)
{
	int f=0;
	int k=size-1;
	for(int i=0; i<k; i++)
	{
		
		if(arr[i] == arr[k])
		{
			k--;
			f=1;
		}
		else
		{
			f=-1;
		}
	}
	
	return f;
	
}
