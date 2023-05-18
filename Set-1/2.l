%{
    #include<stdio.h>
    #include<ctype.h>
%}

letter [a-z]

%%
{letter} { printf("%c", toupper(yytext[0])); }
%%

int main() {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}
