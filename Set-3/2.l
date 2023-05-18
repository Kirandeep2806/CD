%{
    #include "y.tab.h"
%}
%%
[a-z]+       {yylval=*yytext; return NUM;}
[+-\/*\(\)%] { return yytext[0]; }
[ \t\n]      ;
.            {}
%%

int yywrap(){
    return 1;
}
