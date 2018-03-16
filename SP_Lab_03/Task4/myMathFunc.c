int isEqual(int a , int b)
{
	if(a==b)
	{
		return 1;
	}
	else
	{
		return -1;
	}
}
void swap(int a , int b)
{
	printf("before value of a= %d \n", a);
	printf("before value of b= %d \n", b);
	a=a+b;
	b=a-b;
	a=a-b;
	printf("value of a= %d \n", a);
	printf("value of b= %d \n", b);
}
