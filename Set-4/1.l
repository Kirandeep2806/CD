%{
    #include "y.tab.h"
    #include<stdio.h>
%}

%%

[a] { return a_; }
[b] { return b_; }
[ \t\n] ;
. {}

%%

int yywrap() {
    return 1;
}
