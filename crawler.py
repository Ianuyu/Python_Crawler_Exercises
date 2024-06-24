# 2023/10/21
# B1043001 Hsu Liang-I

import csv
import requests
from bs4 import BeautifulSoup

books = [] # Store data of all books

# Total of nine pages
for i in range(1, 10):
    # Use +str(i) to paginate the webpage
    url = 'https://www.sanmin.com.tw/search/index?ct=k&k=AI%e4%ba%ba%e5%b7%a5%e6%99%ba%e6%85%a7&ls=sd&fu=0&vs=list&pi=' + str(i)
    # Send a GET request to the url, the response content is a string
    html = requests.get(url).text
    # Create a BeautifulSoup object to better manipulate the html structure
    soup = BeautifulSoup(html, 'html.parser')
    
    goods = soup.find_all('div', class_='Info') # Find a div that contains book data (title, author, price)
    
    # Use a loop to extract data such as title, author, price
    for good in goods: 
        name = good.find('h3', class_='Title').a 
        # Extract book data (title)
        author = good.find('div', class_='Author').find('span', class_='text-green').a
        # Extract book data (author)
        price = good.find('span', class_='Price')
        # Extract book data (price)
        if name is not None and author is not None and price is not None: 
            # Check if the data is successfully extracted
            book = [] # Store each book's data (title + author + price)
            name_element = "Title: " + name.text + " "     # Extract the text of the title
            author_element = "Author: " + author.text + " " # Extract the text of the author
            price_element = "Price: " + price.text + " NTD"  # Extract the text of the price
            price_value = int(price.text)      # Convert the numerical part of the price to int (for sorting)
            book.append(name_element)          # Append the extracted title, author, and price to book
            book.append(author_element)
            book.append(price_element)
            books.append((book, price_value))  # Store book data and price (for sorting) in books

# Print the books
# Sort by price
sorted_books = sorted(books, key=lambda x: x[1]) # Sort books by price_value, which is x[1]
for item in sorted_books:
    print(item[0], "\n")    # Print the sorted result

# Save data to a text file
textfile = open("books.txt", 'w', encoding='utf-8') # Create a new file or clear the existing file and write data, using UTF-8 encoding
textfile.write("Student ID: B1043001, Name: Hsu Liang-yi\n")   # Write student ID and name, then a new line
textfile.write("\n")      # New line
for item in sorted_books:             # Write data
    textfile.write(item[0][0] + "\n") # Write title sequentially
    textfile.write(item[0][1] + "\n") # Write author
    textfile.write(item[0][2] + "\n") # Write price
    textfile.write("\n")              # New line
textfile.close() # Close the file
print("TXT file created successfully!")

# Save data to a CSV file
with open("books.csv", 'w', encoding='utf-8') as csvfile:
    # Open a CSV file named "books.csv", using UTF-8 encoding
    csv_writer = csv.writer(csvfile)
    # Write the header row of the CSV file
    csv_writer.writerow(["Title", "Author", "Price"])
    # Write book information
    for book in sorted_books:
        csv_writer.writerow(book[0])     
print("CSV file created successfully!")






