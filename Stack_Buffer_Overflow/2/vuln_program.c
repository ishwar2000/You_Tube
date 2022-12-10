#include<stdio.h>

void hackrich(int a, int b)
{
    
    if(a==0x10 && b==0x15)
    {
        printf("Hacked !!!!!\n");
        system("/bin/sh");
    }
    else if(a==0x10)
    {
    	printf("your second parameter is wrong!! \n");
    }
    
    else
    {
    	printf("you are NOOB !!\n");
    }
    

}

void foo()
{
    char buffer[40];
    puts("give me your input :)\n");
    gets(buffer);
}

void main()
{
    foo();
   
}
