This code is for cleveland dataset heart disease classification. 

I have used two classifiers SVM using SVC and Logistic regression. According to my analysis the SVM works better than Logistic regression as the training classification is higher as compared to logistic training dataset whereas the testing dataset remains the same value. However I will also check for Random forest as it looks promising but my code for that is not running as of now.

This code is focused on choosing classifer so has less graphs. 

I was able to obtain the targets by maping multiple parameters to one output as given in datasets index exlains that the values leads to same classification which is having the heart disease. here 0: means no heart disease and 1 : means heart disease.

for computing the performance of the algorithms I used confusion matrix although any other metric can be used. I found this to be easier and the doc for good.

to run: 

python3 -i HeartDisease_Prediction.py 
Note: if you don't put -i you won't be able to see the graph.