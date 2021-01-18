# md5-Hash-Cracker

## Team Password
The password for our team is umuafw 

![Password](https://user-images.githubusercontent.com/32941163/104964593-8c113500-5991-11eb-9a95-eb400a5bcb4a.PNG)

### Threads / Processes
For our lab we did not implement threads and used a single process that calls upon multiple functions. 

### CPU model used
As for the CPU models used, Kiet has a AMD Ryzen 5 3600 and Chad has a Ryzen 7 3700X.

### Throughput of password cracking
Our code takes in the encrypted password and salt as input and creates every single possible combination of a 6 character string containing all lower case letters from a-z. During each generation of a combination, our code passes it in through our implemented encryption strategy(initialization, loop, finalization: strategy given in lab). After completing the conversion to its hashed version, the password is returned to see if it matches the hashed password given as input. Once a match is found, the password is returned, otherwise the next combination is generated. Our code checks through 11 +/- 1 passwords per second.
