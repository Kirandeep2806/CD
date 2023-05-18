%{
    #include<stdio.h>
    int valid = 1;
%}

%token a_ b_

%%

A: a_ A b_
 |
;

%%

int main() {
    printf("Enter the expression : ");
    yyparse();
    if(valid) {
        printf("Valid string");
    }
}

int yyerror() {
    valid = 0;
    printf("Invalid string");
}
