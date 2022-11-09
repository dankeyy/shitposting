#include <stdio.h>

// implicit return type
// implicit return value
// expression blocks
// empty bodied loops
//
// c is fun

eql (char *a, char *b) {
    (a == b) || ({while (*a && *b && *a++ == *b++); !*a && !*b;});
}


int main() {
    char* a = "lolol";
    char* b = "lolol";
    char* c = a;
    char* d = "kek";
    char* s = "s";

    printf(eql(a, b) ? "true\n" : "false\n");
    printf(eql(a, c) ? "true\n" : "false\n");
    printf(eql(a, d) ? "true\n" : "false\n");
    printf(eql(a, s) ? "true\n" : "false\n");
    printf(eql(c, b) ? "true\n" : "false\n");
}
