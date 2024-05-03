import time
import datetime

epoch_time = time.time()
human_readable_time = datetime.datetime.fromtimestamp(epoch_time).strftime("%m-%d-%Y_%H-%M-%S-%f")[:-3]
print(human_readable_time)
