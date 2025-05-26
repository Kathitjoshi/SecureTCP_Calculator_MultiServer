# SecureTCP_Calculator_Multiserver
* It has two parts: a server and a client that can support numerous instances at the same time and enable flexible and secure interaction.
  
**Server Side**
  
* When you run the server, you give it the IP address and the port number on the same command line. This allows for easy startup of multiple instances of the server, each possibly listening on different ports or 
  IP addresses. The server waits for incoming connections on the specified address and will service incoming calculation requests from the clients.
  
**Client Side**

* The user interface of the client program is user-friendly and interactive. When it starts, it asks the user to input the IP address and the port number of the intended server to connect to. This will implement the multi-server nature of the system.
* When connected, the user accepts commands to perform the calculations from the user in the straightforward format of an operator followed by two consecutive numbers, with a space between them (e.g., + 3 4 for 
  “add 3 and 4”). This string of commands is transmitted to the server.
  
**Communication and Security**

* Client and server communicate over raw sockets, providing a simple, low-level mechanism for data exchange. For security and confidentiality of the data being exchanged, the client wraps its connection within an SSL context. This enables data in transit to be encrypted so that it cannot be eavesdropped upon.
  
**Workflow Summary**
  
* The user begins the server by providing IP and port.
* A client begins and prompts the user for the server's IP and the port to attach.
* The user input from the client is in the format <operator>  <num1>  <num2> (i.e., / 7 5 for 7/5 result).
* The command is transmitted securely on the network to the server.
* The server computes the calculation and returns the result.
* The client presents the result back to the user in an interactive manner.
* This layout provides a seamless, adaptable, and secure system for the execution of basic calculations among different servers and clients. There is also a server.log file which keeps logs of the connections, 
  results of the multi-server-client communication.
  

**Commands to run Server and Client on a Linux Distro terminal - refer to the screenshots in the pdf file uploaded.**

