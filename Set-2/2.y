%{
    #include<stdio.h>
%}

%token NUMBER
%left '+' '-'
%left '*' '/' '%'
%left '(' ')'

%%

ExprEvaluation: E {
    printf("Result : %d", $$);
    return 0;
};

E: E '+' E  {$$ = $1 + $3;}
 | E '*' E  {$$ = $1 * $3;}
 | E '/' E  {$$ = $1 / $3;}
 | E '-' E  {$$ = $1 - $3;}
 | E '%' E  {$$ = $1 % $3;}
 | '('E')'  {$$ = $2;}
 | NUMBER   {$$ = $1;}
;

%%

int main() {
    printf("Enter the Expression : ");
    yyparse();
    return 0;
}

int yyerror() {
    printf("Some error occured!!");
    return 1;
}
