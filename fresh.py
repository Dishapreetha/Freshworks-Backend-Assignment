def delete(key):
    if key not in f:
        print("Please enter a valid key, Not in database") 
    else:
        b=f[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del f[key]
                print("key is successfully deleted")
            else:
                print("time-to-live of",key,"has expired") 
        else:
            del f[key]
            print("key is successfully deleted")
