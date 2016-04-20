# WebcamToOpenCV
My research project for Prof. Dodds at Harvey Mudd College during the Spring 2016 semester.  

This script turns your Android phone into a webcam for live image processing using Python and OpenCV. In the use case for Prof. Dodd's robotics research team, an Android phone running the IP Webcam app will be mounted on an RC vehicle tasked with navigating around its environment. This script will send the live image feed from the mounted phone to the team's navigation software. 

[Link to Google Slides for my presentation on 4/18/16](https://docs.google.com/presentation/d/1Nhs-JVYeqCbM7noAmwrrT2DFmLRwvlDXckch8u8cTT8/edit?usp=sharing)     

# Setup Instructions
1. Install Python 3
2. Install the [Anaconda python distribution](https://www.continuum.io/downloads)    
3. Install OpenCV 3 with Anaconda by running the following:  
`conda install --channel https://conda.anaconda.org/menpo opencv3`
4. Install [urllib](https://pypi.python.org/pypi/urllib3)    
5. Install the [IP Webcam Android app](https://play.google.com/store/apps/details?id=com.pas.webcam)    

# Run the Script
1. Open the IP Webcam app, and scroll down. Click the bottom button, "Start server." Once the server starts, you should be able to view the live video feed on the phone screen. Toward the bottom of the screen, you'll find a link displaying an IP address.
2. In the folder where you store `webcamToOpenCV.py`, run the following:  
`python webcamToOpenCV.py -ip <IP_ADDRESS>`  
where IP_ADDRESS is the IP address displayed by the IP Webcam app once it's running. Input the IP address as a string. For example, if the IP Webcam app tells me the video feed link is "http://134.173.207.119:8080", run:  
`python webcamToOpenCV.py -ip "134.173.207.119"`  
The script's output is two adjacent windows, one containing the camera feed and one containing the camera feed run through an OpenCV red color detection.

#Notes
To adjust the size of the images given by the camera feed, select "Video preferences" from the IP Webcam app's home page, then select "Video resolution" and adjust the resolution. The windows output by the Python script should change size based on the change made in the app.
