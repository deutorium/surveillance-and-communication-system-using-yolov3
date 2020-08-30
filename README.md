# surveillance-and-communication-system-using-yolov3
A smart surveillance system that detects threats along with voice assistance and communication system .

![](images/Screenshot(26).png)

Clone or download the zip file first
Make sure u  have python 3.6.5 and anaconda for the same

first pip install all these if u have gpu in ur system

        tensorflow-gpu==2.1.0
        numpy
        opencv-python==4.1.1.26
        lxml
        tqdm
        flask
        seaborn
        pillow
 if u dont have gpu , pip install these
 
        tensorflow==2.0.1
        numpy
        opencv-python==4.1.1.26
        lxml
        tqdm
        flask
        seaborn
        pillow
      
now open the directory where u have my files  using command prompt ...example---"cd C:\Users\Lenovo\Desktop\yolov3_kd1"



if u dont have gpu run these in command prompt

        conda env create -f conda-cpu.yml
        conda activate yolov3-cpu
        
if u have gpu run these

        conda env create -f conda-gpu.yml
        conda activate yolov3-gpu
        
Weights
        
         Right now weights are trained to identify handguns , rifles and huge-fires . They are stored in weights folder . For a custom dataset train your own weights.
         its better to use google colab for creation of weights.
         use this video to create custom yolov3 weights ------> https://www.youtube.com/watch?v=_FNfRtXEbr4&t=1s

if weights and installation of all packages is over run these

        python load_weights.py
        python detect.py --images "data/images/1.jpg ,data/images/2.jpg"
   
After running detect.py u will find outputs in the detections folder .
