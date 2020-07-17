# Install miniconda before running this. 
git clone https://github.com/socialmediaie/SocialMediaIE.git
conda env create -f SocialMediaIE/environment.yml 
conda activate SocialMediaIE
pip install -e SocialMediaIE/
wget https://databank.illinois.edu/datafiles/vodt2/download -O ic2s2_data.tar.gz
cd SocialMediaIE/ && tar -xzf ../ic2s2_data.tar.gz 
python test_install.py 
