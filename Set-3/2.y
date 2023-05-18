%{
    #include<stdio.h>
%}

%token NUM
%left '+' '-'
%left '*' '/' '%'
%left '(' ')'

%%

E:  E '+' E     {printf("+");}
 |  E '*' E     {printf("*");}
 |  E '-' E     {printf("-");}
 |  E '/' E     {printf("/");}
 |  '(' E ')'   {}
 |  NUM         {printf("%c", yylval);}
;

%%

int main(){
    yyparse();
}

int yyerror (char *msg) {
    return printf ("error YACC: %s\n", msg);
}
