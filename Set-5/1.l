%{
    #include<stdio.h>
    int delim = 0;
    int lineNumber= 1;
%}

%%
[a-zA-Z][a-zA-Z0-9]* { printf("Identifier \t\t: %s || %d\n", yytext, lineNumber); }
[0-9]+ { printf("Digits \t\t: %s || %d\n", yytext, lineNumber); }
[\+\-*\/%^] { printf("Operator \t\t: %s || %d\n", yytext, lineNumber); }
[\n] { lineNumber++; }
[ \n\t] { delim++; }
. { printf("Special Characters \t: %s || %d\n", yytext, lineNumber); }
%%

int main() {
    extern FILE *yyin;
    yyin = fopen("inp.txt", "r");
    yylex();
    printf("\nDelimiter count : %d", delim);
    fclose(yyin);
    return 0;
}

int yywrap() {
    return 1;
}
