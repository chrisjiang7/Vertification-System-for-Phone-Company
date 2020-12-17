#!/usr/bin/env python
# coding: utf-8

# # Computing 4 Assignment
# 

# ---
# ## Background
# 
# In this assignment you will be implementing a product verification system for a company that manufactures smartphones. Your system will determine if a given smartphone passed quality assurance testing in order for the smartphone to be deemed sellable on the market.
# 
# All smartphones undergo two quality assurance tests, namely **T1** and **T2**. The product and testing information will be provided to your system in a **list of lists** where each sub-list represents a unique product accompanied with its T1 and T2 test scores and test dates. Each sub-list has the following format:
# 
# <br>
# \begin{align}
#   \texttt{[‘serialNum’, [‘T1Score’,‘T1Date’], [‘T2Score’,’T2Date’]]}\tag{1}
# \end{align}
# <br>
# 
# Each entry in the sub-list is explained below:
# 
# |   |   |
# |---|:--|
# |**serialNum** |A string with length 8 that represents the smartphone's serial number.   |
# |**T1Score**   |A string representing the T1 test score.   |
# |**T1Date**    |A string representing the T1 test date (YYYY-MM-DD)   |
# |**T2Score**   |A string representing the T2 test score.   |
# |**T2Date**    |A string representing the T2 test date (YYYY-MM-DD)   |
# 
# 
# The following list of lists provides an example of data used by your system. Each sub-list follows the format given in (1). There are 3 products in this example:
# 
# ```
# smartphones = [
# ['BX001321',['0.99','2019-01-03'],['0.71','2019-09-21']],
# ['GX021629',['0.88','2019-08-06'],['0.67','2019-12-11']],
# ['BX101129',['0.95','2019-05-22'],['0.92', '2019-07-10']]]
# ```
# 
# <br>
# 
# The company manufactures two versions of smartphones, namely **BX** and **GX**. The version of the smartphone can be identified by the first two characters of its serial number. Each smartphone is considered a pass on quality assurance testing based on criteria that its version must meet. The following table depicts this set of criteria for each version:
# 
# | Smartphone Version |  T1 Criteria | T2 Criteria  |
# |---|---|:--|
# | **GX**  | - A score of 0.8 or greater  | - A score of 0.9 or greater  |
# | **BX**  | - A score of 0.7 or greater  |  - If the test was conducted in **January** or **February**: A score of 0.98 or greater<br>- If the test was conducted in **March**: A score of 0.9 or greater<br>- If the test was conducted in **April**: A score of 0.87 or greater<br>- If the test was conducted in any other month: A score of 0.85 or greater|
# 
# \begin{align}
#   \texttt{Table 1}
# \end{align}
# 
# <br>
# 
# Note that a smartphone must satisfy T1 **AND** T2 criteria to be considered a pass for quality assurance. For example, GX smartphones must have a T1 score of 0.8 or greater AND have a T2 score of 0.9 or greater. 
# 
# Given the following information, your task is to generate a list of products that passed quality assurance testing. The steps in the requirements section will help you achieve this task.

# ---
# 
# ## Given
# The following functions have been given to you and are expected to be used by you in the implementations of the 3 required functions.
# ### DO NOT MODIFY THESE FUNCTIONS
# 
# 1. The first function given to you is **getProductVersion**(*testInfo*):
#   - ***testInfo***: A *list* containing product testing information in the form of (1)
#   - **Return**: A *string* denoting the product version for the smartphone in the list testInfo. (either ‘BX’ or ‘GX’)
# 
#   
# 2. The second given function is **getTestScores**(*testInfo*):
#   - ***testInfo***: A *list* containing product testing information in the form of (1)
#   - **Return**: A list of length 2 where the first element is the product’s T1 score as a *float*, and the second element in the list is the product’s T2 score as a *float*.
# 
# 
# 3. The final function given to you is **getTestMonths**(*testInfo*):
#   - ***testInfo***: A *list* containing product testing information in the form of (1)
#   - **Return**: A list of length 2 where the first element the T1 test month as an *int*, and the second element is the T2 test month as an *int*.
# 
# ---
# 
# ## Requirements
# The requirements of the program are given below. Please ensure that your functions have the EXACT naming as specified! Failure to do so will result in lost marks.
# 
# 1. Define a function **passedTestsGX**(*testInfoGX*):
#   - ***testInfoGX***: A *list* containing product testing information in the form of (1). The list contains a smartphone that is version GX.
#   - **Return**: A *Boolean* denoting whether or not the GX product met the criteria given in Table 1. (True if the product met the criteria, otherwise false) <br>*(Hint: Use nested if statements and your **getTestScores** function.)*
# 
# 
# 2. Define a function **passedTestsBX**(*testInfoBX*):
#   - ***testInfoBX***: A *list* containing product testing information in the form of (1). The list contains a smartphone that is version BX.
#   - **Return**: A *Boolean* denoting whether or not the BX product met the criteria given in Table 1. (True if the product met the criteria, otherwise false)
# 
# 
# 3. Define a function **determinePassedProducts**(products):
#   - ***products***: A *list of lists* where each entry is in the form of (1).
#   - **Return**: A *list* of serial numbers of all products that passed quality assurance testing. <br>*(Hint: Use a for loop, an if statement, and the **getProductVersion**, **passedTestsGX** and **passedTestsBX** functions.)*

# ---
# ## Implementation
# Please define all functions in the cell below

# In[16]:


# DO NOT MODIFY THESE FUNCTIONS

# Get smartphone version of a product
def getProductVersion(testInfo):
    version = testInfo[0][0:2] # Extract first two characters of the serialNum to get the smartphone version
                               # We need the first element so [0] and then we need its first 2 characters so [0:2] splice
    return version             # Returns either "BX" or "GX"

# Get test scores from a product
def getTestScores(testInfo):
    scores = []                       # Empty list to add the scores to
    for i in range(1,3):              # Range creates the sequence [1, 2]
        score = float(testInfo[i][0]) # On first loop, get the second element [1] and then that list's first element[0]
        scores.append(score)          # The second element is in the form of [‘𝚃𝟷𝚂𝚌𝚘𝚛𝚎’,‘𝚃𝟷𝙳𝚊𝚝𝚎’] so its also a list
                                      # On the second loop i = 2 so we get the T2Score as well and convert both to floats
                                      # Put both scores in a list and return that from the function
                
    return scores                     # Returns [𝚃𝟷𝚂𝚌𝚘𝚛𝚎, T2Score] as floats in a list

# Get test dates from a product
def getTestMonths(testInfo):
    months = []                         # Empty list to add the months to
    for i in range(1,3):                # Range creates the sequence [1, 2]
        date = testInfo[i][1]           # Similar to the above function, but now we extract each lists' second element  
        month = int(date.split('-')[1]) # The extracted elements are in the shape of 'YYYY-MM-DD'
        months.append(int(month))       # So we split at the -, take the middle element, and convert to int
                                        # Also add the months to a list and return that list
            
    return months                       # Returns [𝚃1 Month, T2 Month] as integers in a list



#You can see what the functions return by using these statements below




# ENTER YOUR SOLUTIONS BELOW HERE

def passedTestsGX(testinfoGX):               
    if getTestScores(testinfoGX)[0] >= 0.8 and getTestScores(testinfoGX)[1] >= 0.9:
        return True
    else:
        return False
            
def passedTestsBX(testinfoBX):
    if getTestScores(testinfoBX)[0] >= 0.7:
        if getTestScores(testinfoBX)[1] >= 0.98 and (getTestMonths(testinfoBX)[1]==1 or getTestMonths(testinfoBX)[1]==2):
            return True
        elif getTestScores(testinfoBX)[1] >= 0.9 and getTestMonths(testinfoBX)[1]==3:
            return True
        elif getTestScores(testinfoBX)[1] >= 0.87 and getTestMonths(testinfoBX)[1]==4:
            return True
        elif getTestScores(testinfoBX)[1] >= 0.85 and getTestMonths(testinfoBX)[1]>4:
            return True
        else:
            return False
    else:
        return False
        
def determinePassedProducts(products):
    temp_list=[]
    for i in (products):
        if getProductVersion(i) == "GX":
            if passedTestsGX(i):
                temp_list.append(i[0])
        if getProductVersion(i) == "BX":
            if passedTestsBX(i):
                temp_list.append(i[0])
    return temp_list


# ---
# ## Testing
# 
# The following code creates a main function that you can use to test out your code once you have implemented your functions.
# 
# ```
# def main():
#   products = [['GX010365', ['0.8', '2019-01-03'], ['0.86', '2019-04-10']],
#               ['BX041085', ['0.77', '2019-05-03'], ['0.86', '2019-09-13']],
#               ['BX031112', ['0.7', '2019-01-02'], ['0.97', '2019-02-13']],
#               ['BX210529', ['0.68', '2019-03-10'], ['0.86', '2019-11-15']],
#               ['GX031153', ['0.88', '2019-01-23'], ['0.91', '2019-04-11']],
#               ['BX601829', ['0.73', '2019-03-26'], ['0.90', '2019-04-28']],
#               ['BX481436', ['0.89', '2019-01-03'], ['0.99', '2019-01-10']],
#               ['GX301320', ['0.81', '2019-05-18'], ['0.92', '2019-05-13']]]
#   passed_products = determinePassedProducts(products)
#   print(passed_products)
# main()
# ```
# 
# Copy the code and paste it into the cell below. Run the cell to verify that your code works correctly with the provided input. The following products should be printed after the main() function above is run:
# 
# >['BX041085', 'GX031153', 'BX601829', 'BX481436', 'GX301320']
# 
# 
# 
# 
# 
# 
# 

# In[18]:


def main():
    products = [['GX010365', ['0.8', '2019-01-03'], ['0.86', '2019-04-10']],
              ['BX041085', ['0.77', '2019-05-03'], ['0.86', '2019-09-13']],
              ['BX031112', ['0.7', '2019-01-02'], ['0.97', '2019-02-13']],
              ['BX210529', ['0.68', '2019-03-10'], ['0.86', '2019-11-15']],
              ['GX031153', ['0.88', '2019-01-23'], ['0.91', '2019-04-11']],
              ['BX601829', ['0.73', '2019-03-26'], ['0.90', '2019-04-28']],
              ['BX481436', ['0.89', '2019-01-03'], ['0.99', '2019-01-10']],
              ['GX301320', ['0.81', '2019-05-18'], ['0.92', '2019-05-13']]]
    passed_products = determinePassedProducts(products)
    print(passed_products)
main()


# Note that your code is not necessarily correct if your output matches the expected output. Your code will be checked against multiple inputs for correctness. The cell above it not graded, so feel free to modify the code as you wish!

# ---
# ## Reflective Questions
# 
# 1. Is it necessary to use a for loop in the **getTestScores** and **getTestMonths** functions? Why or why not? Is it beneficial to use a for loop? Why or why not? How would you handle the situation where the number of quality assurance tests is unknown between each product?
# 
# 2. It is highly likely that you used a for loop in the **determinePassedProducts** function. Is it possible to use a while loop? Is there a benefit to using a while loop over a for loop? If not, can you think of a scenario where a while loop would be more beneficial?
# 
# Please answer all questions in the cell below!

# ```
# 1. It is not necessary to use a loop in the getTestScores and getTestMonths because we know that there were only 2 tests so we know to only run it for each test. However, it's much more beneficial to use a loop because it concises your code. However, it is necessary if we wernt given how many tests we had to filter. Create a varible for the upper limit in the for loop or use a while loop.
# 2. It is definitely possible. There is a no benefit to use a while loop in this scenario because we use i to store an index of the list. You would use a while loop when you dont know your range or how many times you need to loop and use a for loop when you do know how many times you need to loop.
# ```

# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 4 dropbox on avenue with the naming convention: macID_CL4.py
# 
# **Make sure the final version of your lab runs without errors, otherwise, you will likely recieve zero.**
# 
# This assignment is due the day after your Lab A section at 11:59 PM EST.
# 
# Late labs will not be accepted!
