ma <- function(arr, n=10){
  res = arr
  for(i in n:length(arr)){
    res[i] = mean(arr[(i-n):i])
  }
  res
}

Mode<- function(x) {
  ux <- unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}

Modes<-function(x) {
  ux <- unique(x)
  tab <- tabulate(match(x, ux))
  ux[tab == min(tab)]
}

