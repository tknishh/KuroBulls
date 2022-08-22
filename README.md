
# Smart India Hackathon Finale 2022
SIH 2022 brings the next generation evolution by inclusion of new methodology to inculcate the culture of startup and innovation ecosystem across different age groups

# Problem Statement
**PSID:** LC1076

**PS Statement:** *Email Spoofing Detection* – Spoofed email with swapped email id(and IP too) can come to any user’s inbox. Suggest a mechanism to filter the spoofed email at server only.

**Org:** Ministry of External Affairs (MEA)

**Domain Bucket:** Blockchain and Cybersecurity

**Image:**
![Description](Link)

# Research
- Data: spoof email stats to be uploaded in order to showcase research and understanding of the PS.
- Route of Email from senders inbox to receivers inbox and area where we'll be apply our solution.
- Example of email sent to email received if necessary for them.
- Usecases
- USP of our solution to our existing technology.
- End ppt by opening a platform for feedback
- explain solution in best UI don't go explaining code.
- Utilize 3 mins to explain solution mechanics and not brain.
- Ask mentors for dataset.
- Try to gain Jury interest.
Once understood the problem statement and after countless meetings, discussions and brainstorming sessions we came up with an approach to block emails at the server 

# Stats
- 96% of phishing attacks arrive by email
# Solution
1. Construction of a deployable container to perform the task of detecting a spoofed email.
2. Adding additional fields to the email headers to let server understand the authentication of sender mail to if it falls in the category of spoof emails.

## Idea

In order to find validity of an email and authentication of sender's information this particular function calculates a "score" that is formulated on the basis of values of SPF, DKIM, DMARC that comes with the email header. This score along with scores from different models are further used to determine whether an email is spoofed or not.

## Working
1. Firstly, when an email arrives on the server the data from the header is retrieved and stored in a dataframe which is further passed to various models and function in order to determine the score.
2. When it arrives on this particular model, a copy of database if formed wherein 3 specific fields i.e. Received-SPF, DKIM-signature, DMARC value is used for further process.
3. Once these fields are retrieved various regex functions are used to extract values in form of `['PASS', 'NEUTRAL', 'SOFTFAIL', 'FAIL']` for SPF and `['PASS', 'FAIL']` for DKIM and DMARC.
4. Values are then mapped to numerical values ranging from 0-3 (inclusive) where 0 denotes FAIL and 3 denotes PASS for SPF and 0,1 for DKIM and DMARC.
5. Then using a common formula a score is generated which signifies the validity of an email.

## Formula
`Score = val['spf'] * val['dkim'] * val['dmarc']`


## Additional Ideas 
- Implementing a method on server that verify registered domains owned by companies And maintaining a registry for same such that domain-name spoofing becomes inaccessible to spoofers.
- ASCII character matching of domain names.
- 

## Conclusion 
Generated score defines whether an email is spoof, Potential spoof or legitimate on the basis of score. Lesser the overall score more the chances of it being spoofed.


## Email Server Records
- **A record** maps a domain to the physical IP address of the computer hosting that domain.
- **MX Record** directs email to a mail server. Like CNAME records, an MX record must always point to another domain.
- **TXT Record** are a type of Domain Name System (DNS) record that contains text information for sources outside of your domain.
- **CNAME** a type of DNS record that maps an alias name to a true or canonical domain name.
