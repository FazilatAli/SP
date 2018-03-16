int isPalindrome(char *arr, int size)
{
	char temparr[size];
	int f=0;
	int k;
	k=size-1;
	for(int i=0; i<size; i++)
	{
		temparr[i]=arr[k];
		k--;
	}
	for(int j=0; j<size; j++)
	{
		if(temparr[j]==arr[j])
		{
			continue;
			f=1;
		}
		else
		{
			f=0;
			break;
		}
	}
	return f;
	
}
