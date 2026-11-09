import psutil


def get_system_info(): 
    cpu = psutil.cpu_percent(interval=1) # Returns the CPU utilization as a percentage
    memory = psutil.virtual_memory().percent # Returns the virtual memory statistics as a named tuple
    disk = psutil.disk_usage("/").percent # Returns the disk usage statistics as a named tuple "/" is use in disk for root directory and .percent is use to get the percentage of disk usage 
    # now we use def for reusable code and also we use return to return the value of function
    

    system_info = {
    "cpu": cpu,
    "memory": memory,
    "disk": disk
     } #this is a concept of dictionary in python , dictionary is a collection of key-value pairs where each key is unique and maps to a value. In this case, the keys are "cpu", "memory", and "disk", and the values are the corresponding system information obtained from the psutil module.

   # print(system_info) #this is a concept of print in python , print is a built-in function that outputs the specified message to the console or other standard output device. In this case, it prints the system_info dictionary containing the CPU, memory, and disk usage information.
    
    return system_info #this is a concept of return in python , return is a statement used to exit a function and optionally pass a value back to the caller. In this case, it returns the system_info dictionary containing the CPU, memory, and disk usage information when the get_system_info() function is called.

    

