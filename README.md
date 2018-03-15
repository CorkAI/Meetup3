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

#### 2: Clone the GitHub repository for Meetup3
**Folder setup**
 Type the following commands to get setup for running the code:
 - ```mkdir cork_ai```   *(make a new folder to work in)*
 - ```cd cork_ai```         *(switch to the newly created folder)*
 - ```git clone https://github.com/CorkAI/Meetup3.git```  *(this will make a Meetup3 folder with all the code/data we need)*
 - ```cd Meetup3```     *(switch to the Meetup3 folder)*

**Launch conda environment**
 Our AWS machine has multiple deep-learning environments installed (conda environments).  We need to launch one with a suitable Python version and TensorFlow already installed:
 - Type ```source activate tensorflow_p36```

 Note: In previous meetups "tensorflow_p27" was used to activate Python version 2.7. Here, we're using
 Python version 3.6.

**Install NLTK**
The "doccluster" example requires the NLTK (Natural Language Tool Kit) module to be installed. To do this:
- Type ```pip install nltk```

Now the "Punkt" English parser will be installed.
- Type ```python```   *(Runs the Python 3.6.4 interpreter)*
- Type ```import nltk```   *(Imports the NLTK module into Python)*
- Type ```nltk.download('punkt')```   *(Downloads and installs the Punkt parser)*
- Type ```exit()```  *(Exits the Python interpreter)*

**Install BeautifulSoup**
In addition, "BeautifulSoup" (bs4) is required to extract text from the HTML documents together with the 'lxml' parser. To do this:
- Type ```pip install bs4```
- Type ```pip install lxml```

**Install SkLearn**
 The "doccluster" and "word2vec" examples require the SkLearn module be installed. To do this:
 - Type ```pip install sklearn```

#### 3: Execute doccluster.py
Executing doccluster.py will cluster the documents in the "Data" directory
and create the "docclust.png" image with the dendrogram showing the similarity
between docments.
- Type ```python doccluster.py```

The following blog post provides a short description of this program: https://nickgrattandatascience.wordpress.com/2018/03/15/document-clustering-example/

The output file 'docclust.png' is written in folder 'output_images'.
 - Use scp to copy the output images to your local machine for inspection:
 	- (linux, mac, cygwin): open a new shell on your local machine and create a fresh empty directory. Then copy the output images to your local system:
		- ```mkdir output_images```
		- ```cd output_images```
		- ```scp -i /path/my-key-pair.pem ubuntu@[copied-DNS]:/home/ubuntu/cork_ai/Meetup3/output_images/* .```
		- View the image using Finder / Explorer or your preferred image viewer.
	- (putty on Windows): Open a command line prompt (cmd)
		- ```pscp -i C:\path\my-key-pair.ppk ubuntu@[copied-DNS]:/home/ubuntu/cork_ai/Meetup3/output_images/* c:\[my_local_directory]```
		- View the image using your preferred image viewer

#### 4: Execute word2vec.py
You can now execute word2vec.py to calculate the word embeddings.
- Type ```python word2vec.py```

As well as reporting semantically similar words, the program creates a plot 'tsne.png' in the "output_images" folder. This visually shows semantic similarities between terms. Use the instuctions from above to download and view the image.

The following blog post provides a short description of this program: https://nickgrattandatascience.wordpress.com/2018/03/15/doc2vec-example/