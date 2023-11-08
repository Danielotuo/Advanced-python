# 1. Create own event loop
# 2. Create a co-routine
# 3. Execute the co-routine using the event loop

import asyncio

# create event loop
loop = asyncio.new_event_loop()

# define a task
task1 = asyncio.sleep(3)

# execute a task
loop.run_until_complete(task1)

# report a message
print("Completed")