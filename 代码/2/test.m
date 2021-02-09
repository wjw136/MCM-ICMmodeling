clc;
clear;
close all;
[label_vector, instance_matrix] =libsvmread('D:\matlab\libsvm-3.22\heart_scale');  
model = svmtrain(label_vector, instance_matrix);
[predicted_label, accuracy, prob_estimates] = svmpredict(label_vector, instance_matrix, model, 'b')