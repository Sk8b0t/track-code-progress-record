% factorial of a number
% n=input("Enter number:");
% pro=1;
% for i=n:-1:1
%     pro=pro*i;
% end
% disp(pro);

% leap yr or not
% yr=input("Enter the year");
% if(mod(yr,4)==0 || mod(yr,400)==0 || mod(yr,100)==0) fprintf("leap yr");
% else fprintf("Not a leap yr");
% end

% x=[-3,4,10];
% for i=x
%     if(i<-2) y=exp(i)+1;
%     elseif(i<6) y=2+cos(i);
%     else y=10*(i-5)+1;
%     end
%     fprintf("for x=%d, y=%d\n",i,y);
% end

% Write a program that uses the switch-case structure to count the number of days in a
% year up to a given date, given the year, the month, and the day of the month as user
% inputs.

% yr=input("Enter the year");
% mon=input("Enter month number:");
% day=input("Enter the day of the month:");
% dy=0;
% isLeap=(mod(yr,4)||mod(yr,400)||mod(yr,100));
% for i=1:mon-1
%     switch i
%         case {1,3,5,7,8,10,12}
%             dy=dy+31;
%         case {2,4,6,9,11} 
%             dy=dy+30;
%         case 2
%             if isLeap
%                 dy=dy+29;
%             else
%                 dy=dy+28;
%             end
%     end
% end
% dy=dy+day;
% fprintf("total no. of days=%d\n",dy);


k=0;
sum=0;
while sum<=2000
    k=k+1;
    sum=sum+(2*k-1);
end
fprintf("The total number of terms required: %d\n",k);
fprintf("the total sum=%d",sum);

    