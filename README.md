# TCP-video-streaming-server
Project: TCP video streaming server. ( Not how actual video streaming servers works). This server reads a video file frame by frame and sends them to the client. The client receives the raw data, reconstitutes them into video, and plays it. 

## How to:
1. To launch the server use server_script.py
2. To launch the client, use client_script,py
3. Change path_to_video_file variable in server.py with a path to a video file on your machine.
4. Start with a single-threaded server. Once it is done, make it multithreaded to accept multiple clients.
5. You will require cv2 for this. You can install opencv from opencv-python [opencv-python](https://pypi.org/project/opencv-python/).
6. It is suggested that you create a virtual environment or conda environment.

## Learning outcomes
Upon completion of this project, you will have gained extensive knowledge in creating and designing a complex program from the ground up, including techniques for managing errors and processing user input.


### Coded with ♥ by [Rokibul Hasan](https://www.facebook.com/rokib16x)
