states1 <- c("M1", "M2", "M3", "M4", "M5", "I1", "I2", "I3", "I4", "T", "N", "C")
states2 <- c("m1", "m2", "m3", "m4", "m5", "i1", "i2", "i3","i4")
states <- c(states1, states2)

#minimum inter transit probability
x <- 0.33

transitionMatrixLeftTop <- matrix(data=c(
   0, 0.9,   0,   0,   0, 0.1,   0,   0,   0,   0,   0,   0,
   0,   0, (0.9-x),   0,   0,   0, 0.1,   0,   0,   0,   0,   0,
   0,   0,   0, 0.9,   0,   0,   0, 0.1,   0,   0,   0,   0,
   0,   0,   0,   0, 0.9,   0,   0,   0, 0.1,   0,   0,   0,
   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,
   0, 0.6,   0,   0,   0, 0.4,   0,   0,   0,   0,   0,   0,
   0,   0, 0.6,   0,   0,   0, 0.4,   0,   0,   0,   0,   0,
   0,   0,   0, 0.6,   0,   0,   0, 0.4,   0,   0,   0,   0,
   0,   0,   0,   0, 0.6,   0,   0,   0, 0.4,   0,   0,   0,
   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,
   0.1, 0,   0,   0,   0,   0,   0,   0,   0,   0, 0.8,   0,
   0,   0,   0,   0,   0,   0,   0,   0,   0, 0.2,   0, 0.8
   ), byrow=TRUE, nrow=12,
dimnames=list(states1, states1))

transitionMatrixRightBottom<- matrix(data=c(
   0, 0.9,   0,   0,   0, 0.1,   0,   0,   0,
   0,   0, (0.9-x),   0,   0,   0, 0.1,   0,   0,
   0,   0,   0, 0.9,   0,   0,   0, 0.1,   0,
   0,   0,   0,   0, 0.9,   0,   0,   0, 0.1,
   0,   0,   0,   0,   0,   0,   0,   0,   0,
   0, 0.6,   0,   0,   0, 0.4,   0,   0,   0,
   0,   0, 0.6,   0,   0,   0, 0.4,   0,   0,
   0,   0,   0, 0.6,   0,   0,   0, 0.4,   0,
   0,   0,   0,   0, 0.6,   0,   0,   0, 0.4
   ), byrow=TRUE, nrow=9,
dimnames=list(states2, states2))


transitionMatrixRightTop<-matrix(0, length(states1),
length(states2), dimnames=list(states1, states2))
#M2 -> m3
transitionMatrixRightTop [2, 3]<- x
transitionMatrixRightTop [11, 1]<- 0.1
transitionMatrixLeftBottom<-matrix(0, length(states2),
length(states1), dimnames=list(states2, states1))
#m2 -> M3
transitionMatrixLeftBottom [2, 3]<- x
transitionMatrixLeftBottom [5, 12]<-1


# Combine the transition matrices into a larger matrix for the jumping HMM
n <- length(states)
combined_transitionMatrix <- matrix(0, n, n, dimnames=list(states, states))

# Copy intra-HMM transitions
combined_transitionMatrix[states1, states1] <- transitionMatrixLeftTop
combined_transitionMatrix[states2, states2] <- transitionMatrixRightBottom

# Add inter-HMM transitions (jumping transitions)
combined_transitionMatrix[states1, states2] <- transitionMatrixRightTop
combined_transitionMatrix[states2, states1] <- transitionMatrixLeftBottom

symbols <- c("A", "T", "C", "G", "end")
emissionMatrix1<- matrix(data=c(
   0.7,   0.1,   0.1,   0.1,     0,
   0.1,   0.1,   0.7,   0.1,     0,
   0.1,   0.8,   0.1,     0,     0,
   0.1,   0.1,   0.1,   0.7,     0,
   0.8,     0,     0,   0.2,     0,
  0.25,  0.25,  0.25,  0.25,     0,
  0.25,  0.25,  0.25,  0.25,     0,
  0.25,  0.25,  0.25,  0.25,     0,
  0.25,  0.25,  0.25,  0.25,     0,
     0,     0,     0,     0,     1,
  0.25,  0.25,  0.25,  0.25,     0,
  0.25,  0.25,  0.25,  0.25,     0
), byrow=TRUE,
nrow=length(states1), dimnames=list(states1, symbols))

emissionMatrix2 <- matrix(data=c(
   0.4,   0.2,   0.2,   0.2,     0,
   0.2,   0.2,   0.4,   0.2,     0,
   0.1,   0.8,   0.1,     0,     0,
   0.1,     0,     0,   0.9,     0,
   0.9,     0,     0,   0.1,     0,
  0.25,  0.25,  0.25,  0.25,     0,
  0.25,  0.25,  0.25,  0.25,     0,
  0.25,  0.25,  0.25,  0.25,     0,
  0.25,  0.25,  0.25,  0.25,     0
), byrow=TRUE,
nrow=length(states2), dimnames=list(states2, symbols))

emissionMatrix <- rbind(emissionMatrix1, emissionMatrix2)

startProbs <- c(1/12, 1/12, 1/12, 1/12, 1/12, 0, 0, 0,
0, 0, 1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 0, 0,
0, 0)

jumping_hmm <- initHMM(States = states, 
                       Symbols = symbols, 
                       startProbs = startProbs, 
                       transProbs = combined_transitionMatrix, 
                       emissionProbs = emissionMatrix)



# Sequence 1: "GTTTACTGAACACACCC"
observations <- c("G", "T", "T", "T", "A", "C", "T", "G", "A", "A", "C", "A", "C", "A", "C", "C", "C")
print('observations <- c("G", "T", "T", "T", "A", "C", "T", "G", "A", "A", "C", "A", "C", "A", "C", "C", "C")')
viterbi_result <- viterbi(jumping_hmm, observations)
print(viterbi_result)
avg_length <- avg_length + length(viterbi_result)
print("")
