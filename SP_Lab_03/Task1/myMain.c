#include<stdio.h>
#include "myStr.h"
void main()
{
	char arr[5]="abba";
	if(isPalindrome(arr,5) == 1)
	{
		printf("Palindrome\n");
	}
	else
	{
		printf("Not a palindrome\n");
	}
	
	
}
