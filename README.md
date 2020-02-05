# GDPR Censor
Aims to anonymize string data for GDPR compliance.

## Quickstart
```
import gdpr
print(gdpr.anonymize("Hi ! My name is John Doe. And I want to say that I am very glad to be a customer of your store in Paris. Patricia, my advisor helps me a lot to choose my products. I give you my phone number to call me about my joy : 07 86 49 19 63."))
```

The results should be :
```
Hi ! My name is FIRST_NAME LAST_NAME. And I want to say that I am very glad to be a customer of your store in Paris. FIRST_NAME, my advisor helps me a lot to choose my products. I give you my phone number to call me about my joy : PHONE_NUMBER.
```
