# Load the HMM package
library(HMM)


# HMM 1
# Define states, symbols, and transition/emission matrices
states_HMM1 <- c("HMM1_M1", "HMM1_M2", "HMM1_M3", "HMM1_M4", "HMM1_M5", "HMM1_I1", "HMM1_I2", "HMM1_I3", "HMM1_I4")
# symbols <- c("A", "T", "C", "G")

transitionMatrix_HMM1 <- matrix(data=c(
      0, 0.9, 0, 0, 0, 0.1, 0, 0, 0, 
      0, 0, 0.9, 0, 0, 0, 0.1, 0, 0,
      0, 0, 0, 0.9, 0, 0, 0, 0.1, 0,
      0, 0, 0, 0, 0.9, 0, 0, 0, 0.1,
      0, 0, 0, 0, 1, 0, 0, 0, 0,
      0, 0.6, 0, 0, 0, 0.4, 0, 0, 0,
      0, 0, 0.6, 0, 0, 0, 0.4, 0, 0,
      0, 0, 0, 0.6, 0, 0, 0, 0.4, 0,
      0, 0, 0, 0, 0.6, 0, 0, 0, 0.4),
      byrow=TRUE, nrow=9, dimnames=list(states, states))

emissionMatrix_HMM1 <- matrix(data=c(
    0.7, 0.1, 0.1, 0.1,
    0.1, 0.1, 0.7, 0.1,
    0.1, 0.8, 0.1, 0,
    0.1, 0.1, 0.1, 0.7,
    0.8, 0, 0, 0.2,
    0.25, 0.25, 0.25, 0.25,
    0.25, 0.25, 0.25, 0.25,
    0.25, 0.25, 0.25, 0.25,
    0.25, 0.25, 0.25, 0.25),
    byrow=TRUE, nrow=9, dimnames=list(states, symbols))

# startProbs <- c(0.2, 0.2, 0.2, 0.2, 0.2, 0, 0, 0, 0)

# # Initialize the HMM
# hmm <- initHMM(States = states, 
#                Symbols = symbols, 
#                startProbs = startProbs, 
#                transProbs = transitionMatrix, 
#                emissionProbs = emissionMatrix)

# # Run Viterbi for each observation sequence and calculate average length
# avg_length <- 0

# # Sequence 1: "ACTGA"
# observations <- c("A", "C", "T", "G", "A")
# print('observations <- c("A", "C", "T", "G", "A")')
# viterbi_result <- viterbi(hmm, observations)
# print(viterbi_result)
# avg_length <- avg_length + length(viterbi_result)
# print("")

# # Sequence 2: "AGCTGA"
# observations <- c("A", "G", "C", "T", "G", "A")
# print('observations <- c("A", "G", "C", "T", "G", "A")')
# viterbi_result <- viterbi(hmm, observations)
# print(viterbi_result)
# avg_length <- avg_length + length(viterbi_result)
# print("")

# # Sequence 3: "AGCCTGA"
# observations <- c("A", "G", "C", "C", "T", "G", "A")
# print('observations <- c("A", "G", "C", "C", "T", "G", "A")')
# viterbi_result <- viterbi(hmm, observations)
# print(viterbi_result)
# avg_length <- avg_length + length(viterbi_result)
# print("")

# # Calculate and print the average length of Viterbi results
# avg_length <- avg_length / 3
# cat("Average length of Viterbi results:", avg_length, "\n")


# #HMM 2
# Define states, symbols, and transition/emission matrices
states_HMM2 <- c("HMM2_M1", "HMM2_M2", "HMM2_M3", "HMM2_M4", "HMM2_M5", "HMM2_I1", "HMM2_I2", "HMM2_I3", "HMM2_I4")
#symbols <- c("A", "T", "C", "G")

transitionMatrix_HMM2 <- matrix(data=c(
      0, 0.8, 0.05, 0.05, 0, 0.1, 0, 0, 0, 
      0.05, 0, 0.7, 0.05, 0, 0.05, 0.15, 0, 0,
      0, 0.05, 0, 0.8, 0, 0, 0.1, 0.05, 0,
      0.1, 0, 0, 0, 0.7, 0, 0, 0.1, 0.1,
      0.05, 0, 0, 0.05, 0.9, 0, 0, 0, 0,
      0.2, 0.4, 0, 0, 0.1, 0.3, 0, 0, 0,
      0.1, 0, 0.4, 0, 0, 0, 0.3, 0.2, 0,
      0, 0, 0.1, 0.3, 0.1, 0, 0, 0.5, 0,
      0, 0.1, 0, 0.2, 0.1, 0, 0, 0, 0.6),
      byrow=TRUE, nrow=9, dimnames=list(states, states))



emissionMatrix_HMM2 <- matrix(data=c(
    0.4, 0.2, 0.2, 0.2,    # M1 has a balanced probability
    0.1, 0.3, 0.5, 0.1,    # M2 is more likely to emit "C"
    0.05, 0.75, 0.1, 0.1,  # M3 has a strong preference for "T"
    0.1, 0.15, 0.15, 0.6,  # M4 is more likely to emit "G"
    0.5, 0.1, 0.1, 0.3,    # M5 has a higher probability for "A"
    0.25, 0.25, 0.25, 0.25, # I1 has equal probability for all symbols
    0.3, 0.2, 0.2, 0.3,    # I2 has a preference for "A" and "G"
    0.15, 0.35, 0.3, 0.2,  # I3 prefers "T" and "C"
    0.2, 0.3, 0.2, 0.3     # I4 has a balanced distribution with a slight preference for "A" and "G"
    ),
    byrow=TRUE, nrow=9, dimnames=list(states, symbols))



# startProbs <- c(0.2, 0.2, 0.2, 0.2, 0.2, 0, 0, 0, 0)

# # Initialize the HMM
# hmm <- initHMM(States = states, 
#                Symbols = symbols, 
#                startProbs = startProbs, 
#                transProbs = transitionMatrix_HMM2, 
#                emissionProbs = emissionMatrix_HMM2)

# # Run Viterbi for each observation sequence and calculate average length
# avg_length <- 0

# # Sequence 1: "ACTGA"
# observations <- c("A", "C", "T", "G", "A")
# print('observations <- c("A", "C", "T", "G", "A")')
# viterbi_result <- viterbi(hmm, observations)
# print(viterbi_result)
# avg_length <- avg_length + length(viterbi_result)
# print("")

# # Sequence 2: "AGCTGA"
# observations <- c("A", "G", "C", "T", "G", "A")
# print('observations <- c("A", "G", "C", "T", "G", "A")')
# viterbi_result <- viterbi(hmm, observations)
# print(viterbi_result)
# avg_length <- avg_length + length(viterbi_result)
# print("")

# # Sequence 3: "AGCCTGA"
# observations <- c("A", "G", "C", "C", "T", "G", "A")
# print('observations <- c("A", "G", "C", "C", "T", "G", "A")')
# viterbi_result <- viterbi(hmm, observations)
# print(viterbi_result)
# avg_length <- avg_length + length(viterbi_result)
# print("")

# # Calculate and print the average length of Viterbi results
# avg_length <- avg_length / 3
# cat("Average length of Viterbi results:", avg_length, "\n")


# Define states and symbols for both HMMs
combined_states <- c(states_HMM1, states_HMM2)

symbols <- c("A", "T", "C", "G")

# Define transition matrices for HMM1 and HMM2 (as in your example)
transitionMatrix_HMM1 <- matrix(..., nrow=length(states_HMM1), dimnames=list(states_HMM1, states_HMM1))
transitionMatrix_HMM2 <- matrix(..., nrow=length(states_HMM2), dimnames=list(states_HMM2, states_HMM2))

# Define emission matrices for HMM1 and HMM2
emissionMatrix_HMM1 <- matrix(..., nrow=length(states_HMM1), dimnames=list(states_HMM1, symbols))
emissionMatrix_HMM2 <- matrix(..., nrow=length(states_HMM2), dimnames=list(states_HMM2, symbols))

# Define the jump probability
p_jump <- 0.1

# Combine the transition matrices into a larger matrix for the jumping HMM
n <- length(combined_states)
combined_transitionMatrix <- matrix(0, n, n, dimnames=list(combined_states, combined_states))

# Copy intra-HMM transitions
combined_transitionMatrix[states_HMM1, states_HMM1] <- (1 - p_jump) * transitionMatrix_HMM1
combined_transitionMatrix[states_HMM2, states_HMM2] <- (1 - p_jump) * transitionMatrix_HMM2

# Add inter-HMM transitions (jumping transitions)
combined_transitionMatrix[states_HMM1, states_HMM2[1]] <- p_jump / length(states_HMM1)
combined_transitionMatrix[states_HMM2, states_HMM1[1]] <- p_jump / length(states_HMM2)

# Combine emission matrices
combined_emissionMatrix <- rbind(emissionMatrix_HMM1, emissionMatrix_HMM2)

# Define start probabilities
# startProbs <- c(rep(0.5 / length(states_HMM1), length(states_HMM1)),
#                 rep(0.5 / length(states_HMM2), length(states_HMM2)))
startProbs <- c(0.1, 0.1, 0.1, 0.1, 0.1, 0, 0, 0, 0, 0.1, 0.1, 0.1, 0.1, 0.1, 0, 0, 0, 0)

# Initialize the jumping HMM
jumping_hmm <- initHMM(States = combined_states, Symbols = symbols, 
                       startProbs = startProbs, 
                       transProbs = combined_transitionMatrix, 
                       emissionProbs = combined_emissionMatrix)

# Run Viterbi for each observation sequence and calculate average length
avg_length <- 0

# Sequence 1: "ACTGA"
observations <- c("A", "C", "T", "G", "A")
print('observations <- c("A", "C", "T", "G", "A")')
viterbi_result <- viterbi(jumping_hmm, observations)
print(viterbi_result)
avg_length <- avg_length + length(viterbi_result)
print("")

# Sequence 2: "AGCTGA"
observations <- c("A", "G", "C", "T", "G", "A")
print('observations <- c("A", "G", "C", "T", "G", "A")')
viterbi_result <- viterbi(hjumping_hmmmm, observations)
print(viterbi_result)
avg_length <- avg_length + length(viterbi_result)
print("")

# Sequence 3: "AGCCTGA"
observations <- c("A", "G", "C", "C", "T", "G", "A")
print('observations <- c("A", "G", "C", "C", "T", "G", "A")')
viterbi_result <- viterbi(jumping_hmm, observations)
print(viterbi_result)
avg_length <- avg_length + length(viterbi_result)
print("")

# Calculate and print the average length of Viterbi results
avg_length <- avg_length / 3
cat("Average length of Viterbi results:", avg_length, "\n")