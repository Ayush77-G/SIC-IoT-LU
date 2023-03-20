# Face Mask Detector Using Raspberry Pie


One of the worst jobs in the world right now is being a greeter at a retail store who has to tell people to put on their face masks. Instead of making a human check for mask compliance, we can create a Raspberry Pi-powered mask detector that uses image recognition. Then unruly patrons can yell at a Raspberry Pi screen instead. 

In this article, we’ll show you how to set up a Raspberry Pi Face Mask Detection System and sound a buzzer when someone is not wearing their face mask. This project was inspired by a video of a mall in Asia where an entry gate could only be activated by a user wearing a face mask. 

## How does the Raspberry Pi Face Mask Detector project work? 

When a user approaches your webcam, the Python code utilizing TensorFlow, OpenCV, and imutils packages will detect if a user is wearing a face mask or not. Users not wearing a face mask will be designated with a red box around their face, and users wearing a face mask will see a green box around their face with the text, “Thank you. Mask On.” Users not wearing a face mask will see a red box around their face with, “No Face Mask Detected.” 

## What You’ll Need for Raspberry Pi Face Mask Detection 

1. Raspberry Pi 4 (opens in new tab) (Raspberry Pi Zero is not recommended for this project, and the Raspberry Pi 3 ran very slowly.)

2. 16GB (or larger) microSD card (see best Raspberry Pi microSD cards) with a fresh install of Raspberry Pi OS

3. Power supply/Keyboard/Mouse/Monitor/HDMI Cable (for your Raspberry Pi)

4. USB Webcam (opens in new tab) or Raspberry Pi Camera

## Face Mask Model Training (Long Method) 

Now that you have your face mask detector up and running, you’re probably wondering, “How does it work?”

Over one thousand photos were used to train the model that detect_mask_webcam.py uses to make the mask or no mask determination. The more examples provided, the better the machine learning because fewer photos = less accuracy. 

Photos were divided into 2 folders in our dataset, with_mask and without_mask and the training algorithm created a model of mask vs. no mask based on the dataset.

## Training the model for Raspberry Pi face mask detection

1. Open a Terminal, press Ctrl-T.

2. Install sklearn and matplotlib packages to your Pi

3. Train the model. Keep in mind that, the more photos you have in the dataset folder, the longer it will take to create the model. If you get an “out of memory” error, reduce the number of photos in your dataset until you can successfully run the Python code

## Circuit Connection

![Screenshot 2023-03-20 at 11 21 17 PM](https://user-images.githubusercontent.com/103669722/226425152-bed5423c-984f-4cfd-82a5-9517daf96ea4.png)

## Conclusion

Our model is working perfectly fine with utmost effciency.

