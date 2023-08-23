#include <stdio.h>

// implicit return type
// implicit return value
// expression blocks
// empty bodied loops
//
// c is fun

eql (char *a, char *b) {
    (a == b) + (!a && !b) || (a && b && ({while (*a++ && *b++ && *a == *b); !*a && !*b;}));
}


int main() {
    char* a = "xyz";
    char* b = "xyz";
    char* c = "xym";
    char* d = "myz";
    char* e = "m";
    char* f = NULL;
    char* g = NULL;

    printf(eql(a, b) ? "true\n" : "false\n");
    printf(eql(a, c) ? "true\n" : "false\n");
    printf(eql(a, d) ? "true\n" : "false\n");
    printf(eql(a, e) ? "true\n" : "false\n");
    printf(eql(a, f) ? "true\n" : "false\n");
    printf(eql(c, d) ? "true\n" : "false\n");
    printf(eql(f, g) ? "true\n" : "false\n");
}
