% x=linspace(0,35,500);
% y=0.4*(sqrt(1.8*x));

% figure;
% plot(x,y,'b--');
% axis([0,35,0,3.5]);

% n=linspace(0,20,500);
% z=(0.2+0.8i).^n;
% x=real(z);
% y=imag(z);

% figure;
% plot(x,y,'r--*');

% x=linspace(0,2);
% y=sinh(x);
% y1=0.5*exp(x);

% figure;
% plot(x,y,'r-');
% hold on;
% plot(x,y1,'b-');
% hold off;
% grid on;
% title('Comparison of sinh(x) and 0.5e^x');
% xlabel('x');
% ylabel('y');
% text(0.8, 0.5 * exp(0.8) + 0.3, '0.5e^x','Color','r');
% text(0.8,sinh(0.8),'sinh(x)','Color','b');

x=linspace(0,1,200);
y=sin(x);
y1=x-(x.^3)/3;

figure;
plot(x,y1,'r--*');
hold on;
plot(x,y,'b--');
hold off;
grid on;
title('Comparison of sin(x) and x - x^3/3');
xlabel('x');
ylabel('y');
legend;

disp('Click for identifying sinx graph');
gtext('Sin(x)');

disp('Click for identifying x-(x.^3)/3 graph ');
gtext('x-(x.^3)/3');





