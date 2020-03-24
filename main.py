import pandas as pd
import os

#######################################################
# CHANGE VALUE OF VARIABLES ACCORDING TO YOUR NEED
#######################################################
fileName = 'data/example..CSV'#replace fileName with path of csv file
outputFilePath = 'result/data.txt'#replace this with resulting file path(full or relative)
digitsInFileName = 4
framesPerSecond = 2
rowsToSkip = 2
sep = '\t'
ext = 'pgm'
######################################################

#image file name format
# image-0000.pgm
df = pd.read_csv(fileName).iloc[rowsToSkip:]
df['images'] = df.apply(lambda row: "image-{count}.{ext}".format(count=str(int(framesPerSecond*float(row.Time))).zfill(digitsInFileName), ext=ext), axis = 1) 
print(df)

outputFolder, outputFileName = os.path.split(outputFilePath)
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)


df.to_csv(outputFilePath, sep=sep, columns=['images','Vhcl.Steer.Ang'], header=False, index=False)