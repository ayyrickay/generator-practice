"""Contains examples and exercises for learning about generators"""
from threading import Timer

# **************************
# FOR LOOP
# **************************
# Runs to termination
# No ability to reset
# Looping, not iterating
for x in range(6):
    print x # outputs 0-5 immediately

# **************************
# GENERATOR
# **************************
# Runs as its called
# Can be reset through re-instantiation (with custom values)
# Will instantiate a Generator, which is an iterator - inherently stateful
def generate_x(max_num):
    print 'running generator'
    idx = 0
    while idx < max_num:
        yield idx
        idx += 1

# Create generator
LOGGER = generate_x(6)

def log_two(log):
    print 'Logging Async code'
    print next(log)
    print next(log)

# Go crazy with logs
print next(LOGGER)
print next(LOGGER)
PY_TIMER = Timer(2.0, log_two, [LOGGER])
PY_TIMER.start()
print 'Logging additional output before async'
print next(LOGGER)


# **************************
# SCHEDULER - NO GENERATOR
# **************************
#
# PIECES = ['scales', 'Hanon', 'Minuet in G', 'King March']
#
# NUM_WEEKS = 3
# DAYS_PER_WEEK = 6
#
# totalPracticeDays= NUM_WEEKS * DAYS_PER_WEEK;
#
# currentMusicIndex = 0
#
# schedule = [...Array(totalPracticeDays)].map(() => ({
#     practice: PIECES[currentMusicIndex++ % PIECES.length]
# }))
#
# print schedule


# **************************
# SCHEDULER - WITH GENERATOR
# **************************

# def repeater(arr):
#     index = 0
#     while True:
#         yield arr[index % len(arr)]
#         index += 1
#
# PIECES = ['scales', 'Hanon', 'Minuet in G', 'King March']
#
# NUM_WEEKS = 3
# DAYS_PER_WEEK = 6
#
# TOTALY_PRACTICE_DAYS = NUM_WEEKS * DAYS_PER_WEEK
#
# NEXT_PIECE = repeater(PIECES)
#
# SCHEDULE = [next(NEXT_PIECE) for x in range(TOTAL_PRACTICE_DAYS)]
#
# print schedule

# **************************
# FIBONACCI GENERATOR
# **************************

# def fib():
#     print 'No code yet'
#     # YOUR CODE HERE
#
# # Create Fibonacci generator
# FIB_GENERATOR = fib()
#
# # Logs the first 10 Fibonacci numbers
# index = 0
# while index < 10:
#     print next(FIB_GENERATOR)
#     index += 1
