x = 0:0.05:5*pi;
y = sin(x);

% figure;
% plot(x,y,'b--');
% title('Sine wave');
% xlabel('Time(s)');
% ylabel('Amplitude');
% axis([0 2*pi -1.2 1.2]); 

% y2=cos(x);
% figure;
% plot(x,y,'b--','DisplayName','sin(x)');
% hold on;
% plot(x,y2,'r--','DisplayName','cos(x)');
% hold off;
% legend;

figure;
subplot(2, 1, 1);
plot(x, y);
title('Subplot 1: Sine');

subplot(2, 1, 2);
plot(x, y2);
title('Subplot 2: Cosine');



