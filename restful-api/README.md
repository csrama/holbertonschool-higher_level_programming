## RESTful API Fundamentals Project

---
## Introduction

In the evolving world of software development, understanding how to communicate and transfer data efficiently between systems is essential. This project explores RESTful APIs, a cornerstone of modern web services.

REST (Representational State Transfer) is an architectural style that enforces scalability, statelessness, and cacheability, making systems easier to integrate, maintain, and scale. Through this project, learners gain both theoretical understanding and hands-on experience in consuming, developing, securing, and documenting APIs using industry-standard tools and practices.

Learning Objectives

By completing this project, you will be able to:

HTTP/HTTPS Basics

Understand how web communication works, HTTP methods, status codes, and the difference between secure and non-secure protocols.

API Consumption with Command Line

Interact with APIs using tools like curl and wget.

API Consumption with Python

Fetch and manipulate data using Python libraries such as requests.

API Development with http.server

Build a basic API using Python’s built-in HTTP server modules.

API Development with Flask

Create scalable APIs with routing, data handling, and REST principles using Flask.

API Security & Authentication

Apply security concepts such as tokens, authentication headers, and HTTPS.

API Standards & Documentation with OpenAPI

Produce standardized API documentation for maintainability and usability.

Importance

RESTful APIs power nearly every modern application — from social media integrations to cloud services and industrial automation systems.

Mastering APIs equips developers with essential skills to:

Integrate services efficiently

Build scalable systems

Secure data exchange

Maintain long-term, well-documented platforms

This project bridges both technical implementation and architectural understanding, ensuring you can design and consume APIs professionally.


   Client[Client] -->|Request| WebServer[Web Server]
   
    WebServer -->|Process| APIServer[API Server]
    
    APIServer -->|Fetch/Modify| Database[Database]
    
    Database --> APIServer
    
    APIServer -->|Return| WebServer
    
    WebServer -->|Response| Client



Components

Client
The requester of the service (browser, mobile app, or CLI tool).

Web Server
Receives requests and forwards them to the API layer.

API Server
Contains business logic and processes client requests.

Database
Stores persistent data that the API reads or modifies.

Request Flow

The client sends an HTTP/HTTPS request.

The web server routes the request to the API server.

The API server processes the request and queries the database if needed.

The API server returns a response to the web server.

The web server sends the final response back to the client.

In smaller systems, the Web Server and API Server may be combined into a single service.

Technologies Used

Python

Flask

HTTP/HTTPS

REST Architecture

OpenAPI / Swagger

Command-line tools (curl, wget)

Outcome

After completing this project, you will be able to:

Design RESTful APIs

Consume APIs using CLI tools and Python

Secure endpoints

Document APIs professionally


## 0. Basics of HTTP/HTTPS
Background

The Hypertext Transfer Protocol (HTTP) is the foundation of data communication on the web. It allows clients such as browsers and applications to communicate with servers. HTTPS (HTTP Secure) is the encrypted version of HTTP, using SSL/TLS to protect data from interception and tampering.

Objective

By the end of this task, students should be able to:

Differentiate between HTTP and HTTPS

Understand the structure of HTTP requests and responses

Identify common HTTP methods and status codes

HTTP vs HTTPS
Feature	HTTP	HTTPS
Security	No encryption	Encrypted using SSL/TLS
Port	80	443
Data Protection	Vulnerable to interception	Protected from eavesdropping
Use Case	Public content	Sensitive data (logins, payments)

Summary:
HTTP sends data in plain text, while HTTPS encrypts communication and verifies server identity, ensuring confidentiality and integrity.

HTTP Request Structure
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html

(optional body)


Components:

Method

Path

Headers

Body (optional)

HTTP Response Structure
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>...</html>


Components:

Status line

Headers

Body

Common HTTP Methods
Method	Description	Use Case
GET	Retrieves data	Fetching a webpage or API data
POST	Sends data to create a resource	Submitting a form
PUT	Updates a resource	Updating user information
DELETE	Removes a resource	Deleting data
Common HTTP Status Codes
Code	Meaning	Scenario
200	OK	Successful request
201	Created	Resource successfully created
301	Moved Permanently	URL changed
404	Not Found	Resource does not exist
500	Internal Server Error	Server failure
Key Takeaways

HTTPS encrypts communication while HTTP does not.

HTTP requests contain methods, headers, and optional bodies.

HTTP responses include status codes and response data.

Status codes are grouped into 1xx, 2xx, 3xx, 4xx, and 5xx.
