# User Instructions

### Instructions for running the tutorials at Cork AI Meetup3

NOTE: If you attended Meetup1 or Meetup2 you will have already completed some of these steps. Ensure you get to see a command prompt $ for your AWS instance.

#### 1: AMAZON WEB SERVICES (AWS):
**Sign in to your AWS account**
 - From https://aws.amazon.com/ choose "Sign in to the Console"

**Launching AWS virtual machine:**
 - Go to "Services" and under the "compute" heading, choose "EC2"
 - Set "region" in top-right corner to be Ireland
 - Click on "Launch Instance"
 - Scroll down and click "Select" for "Deep Learning AMI (Ubuntu) Version 5.0 - ami-0ebac377"

NOTE: This AMI image is frequently updated, and so you may see a later version than "5.0"

 - Scroll down and select "GPU compute ... p2.xlarge"
 - Click "Review and Launch"
 - Click "Launch"
 - If you do not have an existing key pair, then select "Create a new key pair".  This will direct you to create and download a .pem file to your disk. Otherwise select an existing key pair. Note that you must have access to the key pair PEM file locally.
 - Click "Launch Instances"

**Connecting to the launched instance:**
 - From Services menu choose EC2
 - From EC2 dashboard->instances
 - You should see your launched instance listed
 - To connect to the instance (using linux, mac or cygwin with openSSH setup)
   - copy public DNS(ipv4) field
   - open a shell and type ```ssh -i /path/my-key-pair.pem ubuntu@[copied-DNS]```
   (you may need to type ```chmod 400 /path/my-key-pair.pem``` if your key_pair permissions are incorrect)
(If in doubt, see also http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)
 - To connect to the instance using putty on Windows, please follow directions at http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html

Now you should be logged into the machine and see a command-line prompt $.

NOTE: From this point on, the instructions are specific for Meetup3!

#### 2: Clone the GitHub repository for Meetup3
**Folder setup**
 Type the following commands to get setup for running the code:
 - ```mkdir cork_ai```   *(make a new folder to work in)*
 - ```cd cork_ai```         *(switch to the newly created folder)*
 - ```git clone https://github.com/CorkAI/Meetup3.git```  *(this will make a Meetup2 folder with all the code/data we need)*
 - ```cd Meetup3```     *(switch to the Meetup2 folder)*

**Launch conda environment**
 Our AWS machine has multiple deep-learning environments installed (conda environments).  We need to launch one so that the libraries we need (e.g. tensorflow) are ready for use:
 - Type ```source activate tensorflow_p27```

 ** Install SkLearn**
 The "word2vec" example requires the SkLearn module be installed. To do this:
 - Type ```pip install sklearn```

#### 3: Execute word2vec.py
You can now execute word2vec.py to calculate the word embeddings
- Type ```python word2vec.py```
