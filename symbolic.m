% syms x;
% eq_a = x^3 - 2*x +5==0;
% disp(double(solve(eq_a)));
% f = @(x) x^2+3*x-2;
syms x

% Define function
f1 = (x^3 + x + 1) / x;

% % a) First derivative
% df1 = diff(f1,x,1);
% disp('1a) First derivative:');
% disp(simplify(df1));

% % b) Evaluate at x = 1
% val1 = subs(df1,x, 1);
% disp('1b) Value at x = 1:');
% disp(double(val1));

% f=exp(3*x^2+1);
% df1=diff(f,x,1);
% disp("1st derivative:");
% disp(simplify(df1));
% disp("tangent at x=1");
% disp(subs(df1,x,1));
% disp("Critical points:");
% disp(solve(df1==0,x));