n_t_c = int(input())
freq = dict()
for i in range(n_t_c):
    us_name = input()
    if us_name in freq:
        print(f'{us_name}{freq[us_name]}')
        freq[us_name] += 1
    else:
        freq[us_name] = 1
        print('OK')
# check if present in dict, if not set freq = 1 and PRINT OK, if alr present in dict, PRINT NAME+{FREQ}