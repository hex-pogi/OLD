import os, sys,time, platform
os.system('clear') 
print('\nCHECKING FOR UPDATED....\n') 
bit = platform.architecture()[0]
if bit == '64bit':
    print("\033[0m\033[91m Sorry Your Device Is 64Bit, This Tool 64Bit Not Sported, Only For \033[92m32bit\033[0m ]");exit() 
elif bit == '32bit':
    import bryx_old_clone
