# Port-Finder
Uses an algorithm to find open ports in the network

# What are Network Ports
A network port is a number that identifies one side of a connection between two computers. Computers use port numbers to determine to which process or application a message should be delivered. As network addresses are like street address, port numbers are like suite or room numbers.

# What's the use of finding open ports?
Services listen to ports. Web servers (a service) listen to port 80, but that's just a standard, not a hard rule. You could configure any service to listen on any port. It's not about 'special packets' it's about 'dialing the right port number' to get the service you want.

If your pseudo program has a vulnerability, then it can be attacked on the port it is assigned to. You can't attack a program on ports it is not listening to. If you try to attack it on another port (like port 80 in your example), your program will not be reached.

Your last question, then, is a little strange: "Why can't a hacker try to craft a TCP packet with a malicious string, encapsulate it inside the HTTP packet and therefore attack the web server?" That IS what hackers do. But they target the port of the service they want to hit. But maybe you can refine that question based on the information I have provided.

