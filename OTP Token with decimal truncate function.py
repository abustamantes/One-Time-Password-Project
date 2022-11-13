import hmac
import hashlib
import pandas as pd
import base64
import matplotlib.pyplot as plt
import numpy as np


key="800070FF00FF08012"
key=bytes(key,'utf-8')
collision=[]
for x in range(1,1000001):
    msg=bytes(f'{x}','utf-8')
    #digest = hmac.new(key, msg,"sha256")
    digest = hmac.new(key, msg, "sha256").digest() #Main algorithm
    key = key.replace(key, digest)
    offset = digest[19] & 0xF
    code = digest[offset: offset + 4]
    code = int.from_bytes(code, "big") & 0x7FFFFFFF
    code = code % 1000000
    code = "{:06d}".format(code)    
    collision.append(code)

#CR2:  the number of similar two consecutive  OTPs in N(1 million OTPs). 
count=0
for i in range(0,(len(collision)-1)):
  if (collision[i]==collision[i+1]):
    count=count +1
    print("The next OTP to this one is the same: ")
    print(collision[i])
print(f'The final count of two consecutive OTPs is:{count}')
print("\n")

#Generate 1,000,000  OTPs using your  application. Show a graph describing how  the collision properties evolve as the number of OTPs increases. 
df=pd.DataFrame(collision)
df=df[df.duplicated(keep=False)]
df_index=df.index.to_numpy()
df=df.values.flatten()
final=np.stack((df_index,df),axis=1)
_, idx, counts = np.unique(final[:, 1], return_index=True, return_counts=True)
idx = idx[counts > 1]
final = np.delete(final, idx, axis=0)
print(f'The number of repeated OTPs is: {len(final)}')
print(final)
index=[i[0] for i in final]
counter=[i for i in range(1,len(index)+1)]
index=[0]+index
counter=[0]+counter
print("\n")
plt.figure(figsize=(15, 8))
plt.plot(index,counter,color='red',linewidth=4)
plt.xlabel("Number of OTPs generated",fontsize=15)
plt.ylabel("Number of repeated OTPs",fontsize=15)
plt.title("Collision resistance graph",fontsize=15)
#plt.yticks([x for x in range(0,len(counter)+1,2)])
plt.show()