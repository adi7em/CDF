# ENVIRONEMNT SETUP
1. Clone the git repo\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$ git clone git@github.com:adi7em/CDF.git
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> now go to project dir\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$ cd CDF
    
2. Installing Python 3 and venv\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> check python version\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$ python3 -V\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> output shuld look like this\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python 3.6.6\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> install virtual env(if not have)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$ sudo apt install python3-venv
      
3. Creating a Virtual Environment\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$ python3 -m venv venv
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> Activate the Virtual Environment for start Using it\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$ source venv/bin/activate
        
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> Upgrade pip\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$ pip install --upgrade pip
        
4. Install requirements\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$ pip install pandas
   
# USING THE PROJECT
1. In main.py, there's a section "CHANGE VALUE OF VARIABLES ACCORDING TO YOUR NEED" where you can\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> change the input csv file (fileName)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> output file path (outputFilePath)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> (digitsInFileName) this represents the number of digits in the imagefile name.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ex. image-0001.pgm has 4 digits\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;image-00001.pgm has 5 digits\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> (framesPerSecond) is number of image generated for second\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> (rowsToSkip) is redundant rows for us, in .csv file 2nd and 3rd rows are irrelevant to us(first row is header)\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> (sep) represents the separator in the output file. Default is tab, you change it to ',' for comma separated and         to '\s' for space separated\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> (ext) represents the extenstion of image file
   
   **All values have default values according to current configuration**
   
2. Run the script\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$ python main.py
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> output will be generated in a folder called result(unless default value of outputFilePath is changed)\
  
3. Deactivate virtual Env\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> when you're done, you can deactivate the virtual env\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$ deactivate
