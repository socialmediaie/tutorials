# Install miniconda before running this. 
# Create a folder called IC2S2 and run all the commands withing that folder
# Run this in git bash or download the repository
git clone https://github.com/socialmediaie/SocialMediaIE.git

# Run the following in Anaconda prompt
conda env create -f SocialMediaIE/environment.yml 
conda activate SocialMediaIE
pip install -e SocialMediaIE/

# Run the following in git bash or download the file manually
DOWNLOAD_PATH="https://databank.illinois.edu/datafiles/vodt2/download"
wget ${DOWNLOAD_PATH} -O ic2s2_data.tar.gz
cd SocialMediaIE/ && tar -xzf ../ic2s2_data.tar.gz 

# Run the following in Anaconda
python test_install.py 

## If you want to run the webserver install the following:
pip install python-dotenv

# Run tagging webserver
cd SocialMediaIE/webapp
flask run --without-threads --no-reload

# Run classification model
cd SocialMediaIE/webapp_classification
flask run --without-threads --no-reload
