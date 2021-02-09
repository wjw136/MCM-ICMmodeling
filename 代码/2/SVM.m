clear;clc;
close all;
data=xlsread("C:/Users/ASUS/Desktop/代码/美赛/C题/代码/2'/ffdata.xlsx")
data2=xlsread("C:\Users\ASUS\Desktop\代码\美赛\C题\代码\2'\ffdata(test).xlsx")
%2069all 1500train 569 test
train_matrix = data(:,3:end);
train_label = data(:,2);
test_matrix = data2(:,5:end);
test_label = data2(:,4);

[Train_matrix,PS] = mapminmax(train_matrix');
Train_matrix = Train_matrix';
Test_matrix = mapminmax('apply',test_matrix',PS);
Test_matrix = Test_matrix';

cmd = ' -t 2 -c 42.2243 -g 2.639' 
[c,g] = meshgrid(-10:0.2:10,-10:0.2:10);
[m,n] = size(c);
cg = zeros(m,n);
eps = 10^(-4);
v = 5;
bestc = 1;
bestg = 0.1;
bestacc = 0;

model = svmtrain(train_label,Train_matrix,cmd);

[predict_label_1,accuracy_1,prob_estimates] = svmpredict(train_label,Train_matrix,model);
[predict_label_2,accuracy_2,prob_estimates2] = svmpredict(test_label,Test_matrix,model);
result_1 = [train_label predict_label_1];
result_2 = [test_label predict_label_2];
%% plot
figure
test_label = test_label+1;
predict_label_2= predict_label_2+1;
plot(1:length(test_label),test_label,'r-*')
hold on
plot(1:length(test_label),predict_label_2,'b:o')
grid on
 set(gca,'linewidth',0.5,'fontsize',15,'fontname','宋体');
    set(gca,'ytick',[0 1 2 3]);
    set(gca,'yticklabel',{"" "Negative ID" "Positive ID" ""});
set(gca,'YLim',[0,3]);
legend('real type','predicted type')
xlabel('Test set sample number')
ylabel('Test set sample category')
string = {'Comparison of SVM prediction results of test set (RBF kernel function)';
          ['accuracy = ' num2str(accuracy_2(1)) '%']};
title(string)
%% plot2
% y=[1499,1;563,6];
% 
% b=bar(y);
% grid on;
% 
% set(gca,'XTickLabel',{'true predict','false predict'})
% 
% 
% legend('train','test');
% xlabel('different dataset');
% ylabel('number of report');
% set(gca,'YLim',[0,1800]);
% title('training dataset')