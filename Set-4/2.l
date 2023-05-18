%{
    #include<stdio.h>
    #include "y.tab.h"
%}

digits [0-9]+
letters [a-z]+

%%

{digits} return digits;
{letters} return letters;
[ \t\n] ;
. {}

%%

int yywrap() {
    return 1;
}
