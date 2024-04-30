import time

# Get current epoch time
epoch_time = int(time.time())

# Convert epoch time to human-readable format
human_readable_time = time.strftime("%m-%d-%Y_%H-%M-%S", time.localtime(epoch_time))

print("Epoch Time:", epoch_time)
print("Human Readable Time (Numeric format of MMDDYYYY HH:MM:SS):", human_readable_time)
