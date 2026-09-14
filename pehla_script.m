%% Double
a=31.411
b=69.99

%% Single
a=single(a)
%imshow(a)
%bada=single(rand(1069,1069))
%imshow(bada)

%% Integer

%% logical
clc
a=true
b=false
c=logical([1,0,1])
data=rand(1,10)
th=0.5
chkr=data>th  %logical array 
fd=data(chkr)  %using logical indexing 

%% char
clear all
clc
var='Sayan'
a='hello'
b='sk8b0t'
msg=[a,' ',var]

%% String 
disp("MATLAB"+" "+"is"+" "+"weird")
