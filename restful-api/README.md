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


# 0. Basics of HTTP/HTTPS

## Background

The Hypertext Transfer Protocol (HTTP) is the foundation of web communication. It allows clients such as browsers and applications to communicate with servers. HTTPS (HTTP Secure) is the encrypted version of HTTP, using SSL/TLS to protect data from interception and tampering.

---

## Objectives

By completing this task, you will be able to:

- Differentiate between HTTP and HTTPS  
- Understand the structure of HTTP requests and responses  
- Identify common HTTP methods and status codes  

---

## HTTP vs HTTPS

| Feature | HTTP | HTTPS |
|--------|------|-------|
| Security | No encryption | Encrypted using SSL/TLS |
| Port | 80 | 443 |
| Data Protection | Vulnerable to interception | Protected from eavesdropping |
| Use Case | Public content | Sensitive data (logins, payments) |

**Summary:**  
HTTP sends data in plain text, while HTTPS encrypts communication and verifies server identity, ensuring confidentiality and integrity.

---

# 1. API Consumption with curl

## Background

curl (Client URL) is a command-line tool that allows users to transfer data to or from a network server using various protocols such as HTTP, HTTPS, and FTP. It is widely used for debugging, testing, and interacting with RESTful APIs. Mastering curl enables developers to quickly prototype API requests, inspect responses, and diagnose server issues directly from the terminal.

---

## Objectives

By completing this task, you will be able to:

- Install and use curl from the command line
- Construct and execute API requests using curl
- Interpret responses from RESTful APIs

---

## Installing curl

Check if curl is installed:

```bash
curl --version
