#importing the dataset

dataset=read.csv('Mall_Customers.csv')
x<- dataset[4:5]

#using elboe method to find the number of cluster
set.seed(6)
wcss <- vector()
for(i in 1:10)wcss[i] <-sum(kmeans(x,i)$withinss)
plot(1:10,wcss,type = 'b', main = paste('cluster of clients'),
     xlab = 'number of cluster',
     ylab = 'wcss')

#applying kmeans to the mall dataset
set.seed(29)
kmeans <- kmeans(x,5,iter.max = 300,nstart = 10) 

#visualizing the cluster formed
library(cluster)
clusplot(x,
         kmeans$cluster,
         lines=0,
         shade=TRUE,
         color=TRUE,
         labels=2,
         plotchar= TRUE,
         span=TRUE,
         main=paste('cluster of client'),
         xlab='annual income',
         ylab='spending score')