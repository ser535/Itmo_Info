import re
import time

input = open('input.json', 'r')
output = open('output.yml', 'w')

start_time = time.perf_counter()
strings = input.read().split('\n')
input.close()
output.write('---')
for i in range(len(strings)):
    if ':' in strings[i]:
        strings[i] = re.sub('[{}"",]', '', strings[i])
        output.write('\n' + strings[i])

output.close()
print(time.perf_counter() - start_time)