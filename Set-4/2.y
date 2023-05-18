%{
    #include<stdio.h>
    int valid = 1;
%}

%token letters digits

%%

start: letters E

E: letters E
 | digits E
 |
;

%%

int main() {
    printf("Enter the expression : ");
    yyparse();
    if(valid) {
        printf("Expression is valid!!");
    }
}

int yyerror() {
    valid = 0;
    printf("Expression is invalid!!");
}
