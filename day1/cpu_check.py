
# cpu = int(input("Enter the CPU model: "))

# if cpu > 50:
#     print("CPU model is greater than 50")
# else:
#     print("CPU model is less than or equal to 50")


##########################################################Env setup command : pthon -m venv env but if you want to create virtual environment in specific location then you can use below command
# python -m venv /path/to/new/virtual/environment
# For activation  .\env\Scripts\Activate
#####################################################################################################################################################################################

import psutil

# print(dir(psutil)) # Returns a list of all the attributes and methods of the psutil module
#print(psutil.subprocess.__doc__()) # Returns the documentation string for the subprocess module in psutil > __doc__ is a special attribute that contains the documentation string for a module, class, or function. It can be accessed using the __doc__ attribute of the module, class, or function.

threshold = float(input("Enter the CPU threshold percentage: "))

for i in range(2):
    cpu_percent = psutil.cpu_percent(interval=1) # Returns the CPU utilization as a percentage
    print(f"CPU utilization: {cpu_percent}%")
    
    if cpu_percent > threshold:
        print("CPU utilization is above the threshold!")
    else:
        print("CPU utilization is below the threshold.") 

# print(psutil.cpu_percent(interval=1)) # Returns the CPU utilization as a percentage ?
