# NON-EXAM ASSESSMENT
## SECTIONS 0-8

## SECTION 0: CONTENTS
An index of the topics covered.

### Analysis
I. [Introduction](#i-introduction)  
II. [Identifying Client Needs](#ii-identifying-client-needs)  
III. [Researching the Current System](#iii-researching-the-current-system)  
IV. [Meeting Client Needs](#iv-meeting-client-needs)  
V. [Objectives](#v-objectives)

## SECTION 1: ANALYSIS
An abstract section, highlighting the purpose of this NEA write-up and the purpose of my project.

### I. Introduction
The aim of my NEA (Non-exam assessment) is to document a password manager project, written in Python. This NEA will seek to address and highlight the challenges that I faced during the development of this project.

With the increasing number of online accounts, the insecurity of storing passwords locally, and the corresponding need for authentication security, this project aims to mitigate these issues and more. This will be achieved by storing user's passwords in a centralized, secure & privacy-respecting authentication manager.

### II. Identifying client needs
The primary end users would be a wide variety of individuals, who cannot be identified simply by their demographics and digital habits, however, they do share one common pass-time: navigating the digital landscape daily, managing multiple online accounts and passwords across various websites and applications. They need a secure, convenient, and privacy-respecting password manager to simplify their digital lives by securely storing, generating, and auto-filling passwords, eliminating the need to remember complex login credentials.

The centralization aspect of my password manager offers convenience to all users. By storing passwords in a singular, secure location, users can easily access their accounts without the need to remember multiple passwords from multiple platforms. This, in itself, is a security measure, by simplifying authentication management, we can ensure our clients reduce the risk of forgetting passwords or reusing weaker ones.

'But won't centralization reduce security?' in most cases, yes. However, my password manager will employ end-to-end encryption using the Rivest-Shamir-Adleman algorithm (RSA-2048) for the storage of public and private keys on the database, and the Advanced-Encryption-Standard (AES-128) on the client-side. Therefore, in the event of a data-breach or unauthenticated access to the database, the encryption keys remain secure and inaccessible to malicious users.

The usage of randomly generated user IDs enhances privacy, each user will be provided with a unique identifier that cannot be linked back to any personally identifiable information (PII), further mitigating the risk of PII breaches, and granting a certain level of anonymity.

By understanding the diverse needs of my end-users above, I will develop a solution that will prioritize not only security but also convenience and anonymity.

### III. Investigation of client needs
To further identify the real-world needs of my clients, I decided to create a survey using tally.so, which was distributed to 50 people, ranging between the ages of 13-70+

These are the questions I intend to ask : 
### IV. Researching the current system
My password manager will stand out as a privacy-focused and open-source solution in a competitive landscape dominated by various alternatives that often disregard privacy.

From my research, I found that commercial solutions often rely on cloud-based storage, raising concerns about data security and unauthorized access. In contrast, my proposed password manager offers a privacy-focused, open-source alternative in a market where privacy is again, so frequently disregarded.

A distinguishing feature that will be implemented in my password manager is its approach to secure data storage. Data will be stored on both a cloud-based database and the client-side, ensuring superior security. Users will be equipped with a double keypair for decryption. This means that encryption methods, including the Rivest-Shamir-Adleman algorithm (RSA-2048) for public and private key storage on the cloud-based database and the Advanced Encryption Standard (AES-128) on the client-side, will ensure that data remains confidential and secure.

Here, I will visually illustrate how a current password manager would typically operate, using a flowchart.

![](/relavant/Capture.PNG)



### V. Meeting client needs
The core features - such as the generation of randomly generated passwords and usernames, will ensure a certain level of defense against common cyber threats like brute force attacks and data breaches.

My encryption algorithm, utilizing RSA-AES, is designed to meet any client's security requirements effectively, mitigating concerns related to third-party access or cloud-based vulnerabilities, as the double private keypair system ensures client security.

### VI. Objectives
In this section, I will highlight components of my practical project based on the research I have compiled & create a working checklist that I can complete throughout the development of my project.

- Choosing a suitable project Initially I wanted to create a web-based enumeration project; however, due to the simplicity of the initial idea, critics suggested that I should choose a project that could harbor more expansive ideas, such as an SQL database.

- Encryption algorithms While looking through the AQA study material, I saw mention of RSA encryption; I did some research into its security of it & after some reading I decided to use RSA & AES.

- Gaining a deeper understanding of python syntax I'm very new to programming, therefore I had to resort to python docs to learn built-ins and general syntax. To ensure that my project would be up to submission standards, I now regularly do python challenges from [edabit.com](https://edabit.com) & [codewards.com](https://codewards.com)
- Choosing the preferred flavor of SQL In the end, I chose PostgreSQL, due to the robust data-types offered.
- Learning SQL Before touching a database, I wanted to learn how RDBMS work, which will enable me to efficiently and effectively manage, query and manipulate my database.

## SECTION 2: THEORETICAL PLAN-OF-ACTION
Documentation of my thought process & planning ahead for potential setbacks, security risks, ethical & legal violations, & practical implementation.

In this section, I will highlight the general steps of my current working theory, which will be explained in informative paragraphs that will include small code blocks.

### I. Client-side encryption
On the client-side, users will use Advanced Encryption Standard (AES) to encrypt their plaintext password. There will be no data exchange to the server at this point, & the user will remain in control of their AES key in its entirety.

```python
def aes_encrypt(plaintext, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext= pad_plaintext(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return(key, ciphertext, iv)
```

The client-side application will also introduce padding, which is crucial for preventing data interception or Man-In-The-Middle (MITM) attacks. In abstract: padding is a technique to add 'random' bytes to the plaintext, obfuscating the length & structure of the ciphertext.[1]

Here, I have made an attempt to randomize my padding bytes on 	line 3.
```python
def pad_plaintext(plaintext, block_size): 
    global padding
    rand_bytes= 16*random.randint(0,7)
    padding_bytes = block_size - len(plaintext) % AES.block_size + rand_bytes
    padding=bytes([padding_bytes])*padding_bytes
    return plaintext + padding
```
### II. Server-side encryption
Once encrypted at application level using AES, the client will be 	sent a generated RSA public-key from the server to encrypt their 	AES ciphertext. Once complete. the encrypted AES-RSA 	ciphertext is sent to the server for centralisation & secure storage.
This ensures end-to-end & secure encryption for users, as the 	server administrators will not have access to the AES key, and in 	the event of an attack on the databsase, malicious users will not 	have access to the 	plaintext.

I.	Client-side decryption
	This function takes the aes_encrypt() output as positional 	arguments, therefore using the same key & initialization vector.[2]
```python
def aes_decrypt(ukey, ciphertext, uiv):
    cipher = AES.new(ukey, AES.MODE_CBC, uiv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext
```
Once I have the encoded plaintext, I need to remove the padding 	for formatting purposes.
I had issues with removing specific values due to the fact I haven't 	worked with bytes before, in the end I just took the len(padding) & 	used it as a negative index.[2]
```py
def unpad_plaintext(padded_plaintext):
    unpadded_plantext = padded_plaintext[:-len(padding)].decode()
    return unpadded_plantext
```
### II.  Server-side decryption
As for server-side decryption, to ensure security, trust and a level 	of anonimity, the server will never hold plain-text passwords. 	Utilizing the afformentioned AES private-key, which was 	generated by the server, the stored password will be decrypted.

The client will initiate a request to the server, providing specific 	data indicating which password is to be transmitted, this packet 	will also contain a secondary RSA public-key that the server 	will use to re-encrypt & transmit the requested AES-RSA 	ciphertext.


Moving on from encryption & decryption, the following will highlight my thought process of utilizing a PostgreSQL server for secure & efficient storage.

After studying the PostgreSQL documentation, I organised my database schema into three main tables: 'users', 'passwords' & 'keys'. Each table serves a specific role in ensuring not only the security, but the functionality and efficiency of the password manager.

I.	Users table
```sql
CREATE TABLE users (
user_id SERIAL PRIMARY KEY NOT NULL,
login_id VARCHAR(200) UNIQUE NOT NULL,
password BYTEA NOT NULL
);
```
This table stores user initial login passwords, essentially unlocking the password manager. Login ID will be randomly generated and human readable.

II.	Passwords table
```sql
CREATE TABLE passwords (
password_id SERIAL PRIMARY KEY,
user_id INT REFERENCES users(user_id),
domain VARCHAR(253) NOT NULL,
username VARCHAR(180),
password BYTEA NOT NULL UNIQUE
);
```
This table layout is the central layout of the password manager system. The table's structure includes a "password_id" column as the primary key with an auto-incrementing serial value, ensuring each entry is unique. It also references the "user_id" to link the credentials with the respective user from the "users" table. Additionally, the "domain" column is a required field, storing the URL or domain name associated with the login credentials. 

III.	Keys table
```sql
CREATE TABLE keys (
key_id SERIAL PRIMARY KEY,
user_id INT REFERENCES users(user_id),
key_type varchar(8), -- public or private
key_value BYTEA
);
```

These are RSA keys that will be queried & transmitted to the user when the vault is unlocked.
