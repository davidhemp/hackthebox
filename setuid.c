#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char **argv) { 
    if (argc != 2) { 
        puts("Usage: <this> \"command and args\"");
        return 1;
    } else if (geteuid() == 0) { 
        setuid(0);
        setgid(0);
        puts("Executing the following as root");
        puts(argv[1]);
        system(argv[1]);
    } else {
        puts("You do not have privs");
    }
    return 0;
}
