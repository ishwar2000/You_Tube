#include<stdio.h>

void hackrich()
{
    printf("Hacked !!!!!\n");
    system("/bin/sh");

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
