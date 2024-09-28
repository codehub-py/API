1. Introduction
   This document provides a detailed overview of the Sentiment Analysis API developed using Flask. The API processes customer reviews from CSV or XLSX files, analyzes sentiment based on predefined positive and negative words, and returns structured results.

2. Problem Statement
   The goal of this project is to create an API that can perform sentiment analysis on customer reviews to determine the overall sentiment (positive, negative, neutral) based on the presence of specific words in the reviews.

3. Approach to Solving the Problem
  The solution involves developing a Flask-based web application that:
    # Accepts CSV or XLSX files containing customer reviews.
    # Analyzes each review for sentiment based on a predefined list of positive and negative words.
    # Returns the results in a structured JSON format.

4. Analysis of Results
   * Limitations
     # The sentiment analysis is based on predefined words, which may not cover all sentiments effectively.
     # The method may not handle context or sarcasm in reviews.
  * Potential Improvements
     # Expand the list of positive and negative words.
     # Implement machine learning models for more accurate sentiment detection.

5. Additional Insights
  * The application effectively demonstrates a basic approach to sentiment analysis using simple word matching.
  * It provides a good foundation for more advanced sentiment analysis implementations.
    
6. Screenshots
   * Interface Image: ![Screenshot (109)](https://github.com/user-attachments/assets/747e23a6-05f6-4960-acff-a653c27dc405)

   * File Uploading Image: ![Screenshot (110)](https://github.com/user-attachments/assets/ce85ce8a-ec80-4c15-8134-b7b5e7164c46)

   * Analysis Result Image: ![Screenshot (111)](https://github.com/user-attachments/assets/b14626de-25e3-4758-aacc-47e2ca37aad4)


7. Conclusion
  This Sentiment Analysis API serves as a fundamental tool for processing customer reviews and extracting sentiment metrics. While it has limitations, it provides a valuable starting point for further enhancement and exploration in the field of natural language processing.

   
