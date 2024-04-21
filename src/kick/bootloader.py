import kernel
import _thread

for i in range(23):
    _thread.start_new_thread(kernel.run,())