#include<stdio.h>

void hackrich()
{
    system("/bin/sh");
}
void foo()
{
    char buffer[40];
    gets(buffer);
    
    printf(buffer);
    puts("\n");
    gets(buffer);
    
}

void main()
{
    foo();
   
}
