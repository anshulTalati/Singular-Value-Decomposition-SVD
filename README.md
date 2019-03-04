# Singular-Value-Decomposition-SVD-

 1.	Problem:
Given a .tiff image, we are to perform the singular value decomposition on the image and regenerate the image for rank [5, 10, 20, 50, 100, 200]. 
 2.	Data:
The Data image given to us is 512x512 pixel image named as ruler.512.tiff. The image is required to be stored in the same directory of the program for the program to find the image.
 3.	Method:
Singular Value Decomposition says that matrix of can be regenerated by dot product of three matrices. The generation of the matrix is given by following formula: - Anxp= Unxn Snxp VTpxp
 The numpy library is used to generate the matrix viz U, S and Vtranspose(). 
### Note :- The svd function of numpy outputs 
* 	Vtranspose and not matrix V. So, there is no need for taking the transpose of the matrix 
* 	Smatrix obtained is as column matrix which is then taken according to the rank provided by the user and converted into a                    diagonal matrix (using diag() function of numpy ). The Elements of Smatrix is such that the element at (0,0) is the largest                and decreases as we traverse down the diagonal. 

 4.	Results:
The output screen ask user to provide the factor(rank) for regeneration. Once the user inputs the rank the program calculates the regeneration matrix and displays the image for that particular rank.
Note:- Install the numpy and pillow library for your version of python.
