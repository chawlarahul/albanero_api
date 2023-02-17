This Project Generates and Stores the CSV File Stats in the Database taking the csv file url as an input.  

It exposes the APIs for
1. Generating and Storing the CSV File Stats in the Database taking the csv file url as an input. 
    The Following Stats are generated in lieu of every File url given as an input
    1. Number of Rows in the File
    2. Number of Columns in the File
    3. For each column in the file, what are the number of distinct values
    4. For each column in the file, how many values are NULL.
  
2. Fetching the File Stats from the Database taking the file url as an input. 



Sample Output of the API via which we can fetch the File Stats


1. Sending a valid file url as input

    <img width="1177" alt="Screenshot 2023-02-17 at 10 37 31 PM" src="https://user-images.githubusercontent.com/37452767/219718089-2dc7a3b0-9138-4087-bc14-63cff00094f4.png">

2. Sending an invalid file url as input

    <img width="1021" alt="Screenshot 2023-02-17 at 10 51 50 PM" src="https://user-images.githubusercontent.com/37452767/219721307-237c2a43-993c-4642-ba41-7d1ef989a134.png">

3. Sending no file url parameter 

    <img width="1056" alt="Screenshot 2023-02-17 at 10 52 32 PM" src="https://user-images.githubusercontent.com/37452767/219721581-21c68a94-3fc1-4ab1-ac35-48ac11d3a96e.png">
