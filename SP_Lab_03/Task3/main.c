#include<stdio.h>
#include "myStr.h"
#include "myMath.h"
void main()
{
	char arr[4]="abba";
	if(isPalindrome(arr,4) == 1)
	{
		printf("Palindrome\n");
	}
	else
	{
		printf("Not a palindrome\n");
	}
	
	int a=7;
	int b=5;
	if(isEqual(a,b) == 1)
	{
		printf("Equal\n");
	}
	else
	{
		printf("Not Equal\n");
	}
	swap(a,b);
	
}
