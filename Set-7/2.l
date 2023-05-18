%{
    #include<stdio.h>
%}

%%
[aeiouAEIOU] { printf("Vowel \t\t- %s\n", yytext); }
[ \t\n] ;
[a-zA-Z] { printf("Consonant \t- %s\n", yytext); }
. {}
%%

int main() {
    extern FILE *yyin;
    yyin = fopen("inp.txt", "r");
    yylex();
    fclose(yyin);
    return 0;
}

int yywrap() {
    return 1;
}
