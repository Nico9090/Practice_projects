factorial<-function(n){
  i<-1
  p<-n
  while (i<n){
    p<-p*(n-i)
    i<-i+1
  }
  return(p)
}
factorial(5)
