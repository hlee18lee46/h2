
# Python program to generate heatmap which  
# represents panda dataframe in color-coding schemes 
# along with values mentioned in each cell 
  
# import required libraries 



# Defining figure size   
# for the output plot
def get_pdchart1(): 
    import pandas as pd  
    #import seaborn as sns 
    #import matplotlib.pyplot as plt
    # Python program to generate a heatmap 
    # which displays the value in each cell  
    # corresponding to the given dataframe  
    
    # import required libraries 

    
    # defining index for the dataframe 
    idx = ['1', '2', '3', '4'] 
    
    # defining columns for the dataframe 
    cols = list('ABCD') 
    
    # entering values in the index and columns   
    # and converting them into a panda dataframe 
    df = pd.DataFrame([[10, 20, 30, 40], [50, 30, 8, 15], 
                    [25, 14, 41, 8], [7, 14, 21, 28]], 
                    columns = cols, index = idx) 
    
    # displaying dataframe as an heatmap  
    # with diverging colourmap as virdis 
    df.style.background_gradient(cmap ='viridis').set_properties(**{'font-size': '20px'}) 
def get_pdchart2(): 
    # Python program to generate a heatmap 
    # which represents panda dataframe 
    # in colour coding schemes 

    # import required libraries 
    import matplotlib.pyplot as plt 
    import pandas as pd 

    # Defining index for the dataframe 
    idx = ['1', '2', '3', '4'] 

    # Defining columns for the dataframe 
    cols = list('ABCD') 

    # Entering values in the index and columns 
    # and converting them into a panda dataframe 
    df = pd.DataFrame([[10, 20, 30, 40], [50, 30, 8, 15], 
                    [25, 14, 41, 8], [7, 14, 21, 28]], 
                    columns = cols, index = idx) 

    # Displaying dataframe as an heatmap 
    # with diverging colourmap as RdYlBu 
    plt.imshow(df, cmap ="RdYlBu") 

    # Displaying a color bar to understand 
    # which color represents which range of data 
    plt.colorbar() 

    # Assigning labels of x-axis 
    # according to dataframe 
    plt.xticks(range(len(df)), df.columns) 

    # Assigning labels of y-axis 
    # according to dataframe 
    plt.yticks(range(len(df)), df.index) 

    # Displaying the figure 
    plt.show() 

    