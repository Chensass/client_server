# server_client
This project runs server and client interfaces.

The server gets an image path list and sends it to the client.

The client opens the images in random or loop display with a delay time between images
as given by the user. 

The images are displayed and switched automatically unless the user choose otherwise.

# How to start

1. After you cloned the repository open two terminals- one for client and one for server.
   
2. In each one connect to venv:
- In windows type in cmd:
```buildoutcfg
.\vireualenv\Scripts\activate
```
- For linux you will need to create a new venv and install packages with requirements.txt file:

3. First, activate the server:
```buildoutcfg
python ./server.py
```

4. Next, activate the client:
- You can activate client in default mode - will present photos automatically and randomly with 5 secs gap
```buildoutcfg
python ./client.py
```
- To see other modes of client, type:
```buildoutcfg
python ./client.py --help
```
