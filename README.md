# Medical Keyword Extractor

The following Python Script is a great helper for Doctors and Medical Staff. No doctors are ever free to read any emails from their patients which, might be important and urgent.
The program listed here can easily extract any Symptoms experienced, Diseases mentioned, Drugs taken or any Tests mentioned in those mails and simply output them to the doctor.

The program uses Natural Language Processing for the algorithm. The datasets used are from trusted medical organizations around the world like WebMD, WHO and Centre for Disease Control.

FlowChart: <br><br>:
![alt text](https://github.com/arshmittal16/Medical-Keyword-Extractor/blob/master/Images/Flow.jpeg)

Methodology: 
1. Input is taken from the user
2. Text is then divided into several tokens.
3. Each token is combined with other using tokenization and n-grams are created.
4. Each n-gram is then matched with the database and if any *symptom*, *disease*, *test* or *drug* is found in the text, results are uploaded to the database.
5. The output is then fetched from the database and is shown to the user.

Live Link: 
https://arshmittal16.github.io/Medical-Keyword-Extractor-1/

Example Input: <br><br>
![alt text](https://github.com/arshmittal16/Medical-Keyword-Extractor/blob/master/Images/Inp.jpeg)

Example Output: <br><br>
![alt text](https://github.com/arshmittal16/Medical-Keyword-Extractor/blob/master/Images/Out.jpeg) 
