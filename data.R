dataset = read.csv('Data.csv')
dataset$Age= ifelse(is.na(dataset$Age))
