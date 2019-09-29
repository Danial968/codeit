def bank(test):

    n = test['N']
    start_time = test['branch_officers_timings']
    current_time = start_time

    for i in range(n):
        branch_go = current_time.index(min(current_time))
        for j in range(len(current_time)):
            current_time[j] -= start_time[branch_go]
        current_time[branch_go] = start_time[branch_go]

    return branch_go+1


test = {
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