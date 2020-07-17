# Pre-requisites
* Fast internet connection. **BEWARE: We will be downloading around 5-8 GB of data**
* If you decide to run this software on your local machine, you will be downloading that much data which can exhaust your daily data limits. 
* Your machine should support more than 4 GB of RAM as the models are large.
* Ensure that you have installed Python 3 versions of either [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/individual) before running the following commands. You can check it by running `conda --version`

# Mac and Linux Users:
You can simply run the script [./socialmediaie_setup.sh](./socialmediaie_setup.sh) to setup everything. 

# Windows users

* If you are on Windows you need to have git installed from [https://git-scm.com/downloads](https://git-scm.com/downloads) then you can launch git Bash.
* Windows users: run the commands in their respective applications, i.e. git bash and Anaconda Prompt.
* Create a folder called IC2S2 and run all the commands withing that folder
* Run this in git bash or download the repository from [https://github.com/socialmediaie/SocialMediaIE/archive/master.zip](https://github.com/socialmediaie/SocialMediaIE/archive/master.zip) and unzip it into IC2S2 folder. 
```bash
git clone https://github.com/socialmediaie/SocialMediaIE.git
```

## Run the following in Anaconda prompt

```bash
conda env create -f SocialMediaIE/environment.yml 
conda activate SocialMediaIE
pip install -e SocialMediaIE/
```

## Run the following in git bash 

* **NOTE**: You can also download the file manually from [https://databank.illinois.edu/datafiles/vodt2/download](https://databank.illinois.edu/datafiles/vodt2/download) and place it in `IC2S2` folder. 

```bash
DOWNLOAD_PATH="https://databank.illinois.edu/datafiles/vodt2/download"
wget ${DOWNLOAD_PATH} -O ic2s2_data.tar.gz
cd SocialMediaIE/ && tar -xzf ../ic2s2_data.tar.gz 
```


## Test if everything works
* Run the following on git bash or download the file test_install from [https://github.com/socialmediaie/tutorials/tree/master/docs/IC2S2_2020](https://github.com/socialmediaie/tutorials/tree/master/docs/IC2S2_2020) and place in `IC2S2` folder

```bash
wget https://raw.githubusercontent.com/socialmediaie/tutorials/master/docs/IC2S2_2020/test_install.py
```

### Run the following in Anaconda

```bash
python test_install.py 
```

# Running the web-server on both Mac/Linux/Windows

If you want to run the webserver install the following:

```bash
pip install python-dotenv
```

## Run tagging webserver

```bash
cd SocialMediaIE/webapp
flask run --without-threads --no-reload
```

* Open your browser [http://localhost:5000](http://localhost:5000) once you are done press Ctrl+C in Anaconda prompt

## Run classification model

```bash
cd SocialMediaIE/webapp_classification
flask run --without-threads --no-reload
```
* Open your browser [http://localhost:5000](http://localhost:5000) once you are done press Ctrl+C in Anaconda prompt
