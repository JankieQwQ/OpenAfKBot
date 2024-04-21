import time
import kernel
import _thread


print('Loading Permission module......')
for i in range(10):
    print('|'*10,end='')
    _thread.start_new_thread(kernel.run,())
    time.sleep(3.5)
print('\n Done!')
while True:pass