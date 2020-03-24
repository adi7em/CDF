# ENVIRONEMNT SETUP
1. Clone the git repo
   $ git clone git@github.com:adi7em/CDF.git
    
   -> now go to project dir
      $ cd CDF
    
2. Installing Python 3 and venv
  -> check python version
      $ python3 -V
  -> output shuld look like this
      Python 3.6.6
  -> install virtual env(if not have)
      $ sudo apt install python3-venv
      
3. Creating a Virtual Environment
    $ python3 -m venv venv
    
    -> Activate the Virtual Environment for start Using it
        $ source venv/bin/activate
        
    -> Upgrade pip
        $ pip install --upgrade pip
        
4. Install requirements
   $ pip install pandas
   
# USING THE PROJECT
1. In main.py, there's a section "CHANGE VALUE OF VARIABLES ACCORDING TO YOUR NEED" where you can
   -> change the input csv file (fileName)
   -> output file path (outputFilePath)
   -> (digitsInFileName) this represents the number of digits in the imagefile name.
      Ex. image-0001.pgm has 4 digits
          image-00001.pgm has 5 digits
   -> (framesPerSecond) is number of image generated for second
   -> (rowsToSkip) is redundant rows for us, in .csv file 2nd and 3rd rows are irrelevant to us(first row is header)
   -> (sep) represents the separator in the output file. Default is tab, you change it to ',' for comma separated and         to '\s' for space separated
   -> (ext) represents the extenstion of image file
   
   **All values have default values according to current configuration**
   
2. Run the script
  $ python main.py
  
  -> output will be generated in a folder called result(unless default value of outputFilePath is changed)
  
3. Deactivate virtual Env
  -> when you're done, you can deactivate the virtual env
   $ deactivate
