def bank(test):

    n = test['N']
    start_time = test['branch_officers_timings']
    current_time = start_time[:]
    # sort_start_time = sorted(start_time[:])

    for i in range(len(current_time), n):
        branch_go = current_time.index(min(current_time))
        time_taken = current_time[branch_go]
        for j in range(len(current_time)):
            if current_time[j] > 0:
                current_time[j] -= time_taken
                if current_time[j] < 0:
                    current_time[j] = 0
        current_time[branch_go] = start_time[branch_go]

    return branch_go+1

test = {'N': 572, 'branch_officers_timings': [20, 11, 11, 3, 3, 20, 9, 3, 17, 16, 9, 10, 19, 4, 15, 6, 15, 14, 15, 9, 15, 5, 7, 10, 6, 8, 13, 16, 7, 10, 18]}
test5 = {
  "N": 800000002,
  "branch_officers_timings": [
    2,
    100000,
    100000,
    100000,
    100000,
    100000,
    100000,
    100000,
    100000,
    3
  ]
}
print(bank(test))