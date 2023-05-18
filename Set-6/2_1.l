%{
    // With Scanner
    #include<stdio.h>
    int valid = 0;
%}

%%
[_a-zA-Z][a-zA-Z0-9]* { valid = 1; }
. {}
%%

int main() {
    yylex();
    if(valid)
        printf("Valid identifier!!");
    else
        printf("Invalid Identifier!!");
    return 0;
}

int yywrap() {
    return 1;
}
