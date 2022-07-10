import sys
import pandas as pd
import os 

def main():
    """
    Test the pipeline
    """

    print(f"the current path is:{os.getcwd()}")
    print("pandas version:%s" % (pd.__version__))
    
    # Get docker file parameter
    try:
        print(f"passed argument {sys.argv[1]}")
    except IndexError:
        print("No parameter is passed")

if __name__=="__main__":
    main()