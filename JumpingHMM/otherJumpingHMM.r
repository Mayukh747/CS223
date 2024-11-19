states1 <- c("M1", "M2", "M3", "M4", "M5", "I1", "I2", "I3",
"I4", "T", "N", "C")
states2 <- c("m1", "m2", "m3", "m4", "m5", "i1", "i2", "i3",
"i4")
states <- c(states1, states2)

transitionMatrixLeftTop <- matrix(data=c(0, 0.9, 0, 0,
0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0.8, 0, 0, 0, 0.1, 0,
0, 0, 0, 0, 0, 0, 0, 0.9, 0, 0, 0, 0.1, 0, 0, 0, 0, 0,
0, 0, 0, 0.9, 0, 0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 1, 0, 0.6, 0, 0, 0, 0.4, 0, 0, 0, 0, 0,
0, 0, 0, 0.6, 0, 0, 0, 0.4, 0, 0, 0, 0, 0, 0, 0, 0,
0.6, 0, 0, 0, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0.6, 0, 0,
0, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, ?,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0.8, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0.2, 0, 0.8), byrow=TRUE, nrow=12,
dimnames=list(states1, states1))

transitionMatrixRightBottom<- matrix(data=c(
0, 0.9 ,0 , 0, 0 ,0.1, 0, 0, 0, 
0, 0, 0.1, 0, 0, 0, 0.1, 0, 0, 
0, 0, 0, 0.9, 0, 0, 0, 0.1, 0,
0, 0, 0, 0, 0.9, 0, 0, 0, 0.1, 
0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0.6, 0, 0, 0, 0.4, 0, 0, 0, 0, 0, 0.6, 0, 0, 0,
0.4, 0, 0, 0, 0, 0, 0.6, 0, 0, 0, 0.4, 0, 0, 0, 0, 0,
0.6, 0, 0, 0, 0.4), byrow=TRUE, nrow=9,
dimnames=list(states2, states2))

# a matrix of zeroes
transitionMatrixRightTop<-matrix(0, length(states1),
length(states2), dimnames=list(states1, states2))
transitionMatrixRightTop [?, 3]<-0.1
transitionMatrixRightTop [11, 1]<-0.1
transitionMatrixLeftBottom<-matrix(0, length(states2),
length(states1), dimnames=list(states2, states1))
transitionMatrixLeftBottom [2, 3]<- 0.8
transitionMatrixLeftBottom [5, 12]<-1

symbols <- c("A", "T", "C", "G", "end")
emissionMatrix1<- matrix(data=c(0.7, 0.1, 0.1, 0.1, 0,
0.1, 0.1, 0.7, 0.1, 0, 0.1, 0.8, 0.1, 0, 0, 0.1, 0.1,
0.1, 0.7, 0, 0.8, 0, 0, 0.2, 0, 0.25, 0.25, 0.25, 0.25,
0, 0.25, 0.25, 0.25, 0.25, 0, 0.25, 0.25, 0.25, 0.25,
0,
0.25, 0.25, 0.25, 0.25, 0, 0, 0, 0, 0, 1, 0.25, 0.25,
0.25, 0.25, 0, 0.25, 0.25, 0.25, 0.25, 0), byrow=TRUE,
nrow=length(states1), dimnames=list(states1, symbols))

emissionMatrix2<- matrix(data=c(0.4, 0.2, 0.2, 0.2, 0,
0.2, 0.2, 0.4, 0.2, 0, 0.1, 0.8, 0.1, ?, 0, 0.1, 0, 0,
0.9, 0, 0.9, 0, 0, 0.1, 0, 0.25, 0.25, 0.25, 0.25, 0,
0.25, 0.25, 0.25, 0.25, 0, 0.25, 0.25, 0.25, 0.25, 0,
0.25, 0.25, 0.25, 0.25, 0), byrow=TRUE,
nrow=length(states2), dimnames=list(states2, symbols))

emissionMatrix<c(emissionMatrix1, emissionMatrix2)

startProbs <- c(1/12, 1/12, 1/12, 1/12, 1/12, 0, 0, 0,
0, 0, 1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 0, 0,
0, 0)