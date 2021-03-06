housing <- read.csv("housing1.csv",sep=",")
summary(housing)
SalesPrice <- c(housing$SalePrice)
LotArea <- c(housing$LotArea)
TotalBsmtSF <- c(housing$TotalBsmtSF)
Regression <- lm(SalesPrice~LotArea+TotalBsmtSF)
summary(Regression)
plot(Regression)
newhouse <- data.frame(LotArea=1500 , TotalBsmtSF=1200)
newhouse
predict(Regression,newhouse)