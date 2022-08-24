
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

## Conclusion 
Generated score defines whether an email is spoof, Potential spoof or legitimate on the basis of score. Lesser the overall score more the chances of it being spoofed.
