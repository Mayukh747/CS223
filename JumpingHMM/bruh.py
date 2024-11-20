# states = ["M1", "M2", "M3", "M4", "M5", "I1", "I2", "I3", "I4"]
# N = len(states)
# state_id = {states[idx]: idx for idx in range(N)}
#
# mat = [[0 for _ in range(N)] for _ in range(N)]
#
# mat[state_id["M1"]][state_id["M2"]] = 0.9
# mat[state_id["M2"]][state_id["M3"]] = 0.9
# mat[state_id["M3"]][state_id["M4"]] = 0.9
# mat[state_id["M4"]][state_id["M5"]] = 0.9
# mat[state_id["M5"]][state_id["M5"]] = 1
#
# mat[state_id["I1"]][state_id["I1"]] = 0.4
# mat[state_id["I2"]][state_id["I2"]] = 0.4
# mat[state_id["I3"]][state_id["I3"]] = 0.4
# mat[state_id["I4"]][state_id["I4"]] = 0.4
#
# emission_matrix = [
#     [0.7, 0.1, 0.1, 0.1, ]
#     [0.1, 0.1, 0.7, 0.1,]
#     [0.1, 0.8, 0.1, 0,]
#     [0.1, 0.1, 0.1, 0.7,]
#     [0.8, 0, 0, 0.2,]
#     [0.25, 0.25, 0.25, 0.25,]
#     [0.25, 0.25, 0.25, 0.25,]
#     [0.25, 0.25, 0.25, 0.25,]
#     [0.25, 0.25, 0.25, 0.25]
# ]
# start_probs = [0.2, 0.2, 0.2, 0.2, 0.2, 0, 0, 0, 0]
#
# for row in mat:
#     print(row)
