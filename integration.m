syms x;
% ans=int(x*exp(-3*x));
% disp(simplify(ans));

% f_a = 3 / (x^2 + 5*x + 6)
% I_a = double(int(f_a,x,1,Inf))

C = {'apple', [1, 2, 3], 42};
x = C(1);
y = C{2}(1);
disp(x);
disp(y);