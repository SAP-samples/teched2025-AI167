# Excercise 2: Ground your LLM with Custom Documents

Besides grounding your LLM with SAP help you can of course ground your LLM with you own documents. The document file that the grounding service support here are PDF, HTML, TXT, JPEG, JPG, DOCX, PNG, TIFF, PPT.
However to use Grounding you need to prepare a knowlegde base in advance. Generative AI hub provides two otions for the users to provide data (prepare knowledege base):

* Option 1: Provide the chunks of document via Vector API directly
* Option 2: Upload the documents to supported data repository and run the data pipeline to vectorize the documents

In the following you will get to know both option, and we start with option 1

## Excercise 2.1: Provide the chunks of documents via Vector API directly

In the following we will do the following steps:
+ Prepare the Vector Knowledge Base
    1. Create Collection
    2. Create documents by directly using the chunks of data provided by users
    3.  Store data in the vector database
    4.  Assign repository IDs to access the data
* Configure Grounding Module in the Orchestration 
    1. Create a grounding request configuration in the orchestration pipeline using repository IDs
    2.  Run the orchestration pipeline and check that the response refers to the user data

> 🟨 **TODO:**  
> _Add Excercise with Bruno and Vector API_

## Summary

For the next excercise you will go back to Visual Code.

Continue to - [Exercise 2.2: Run data pipeline to vectorize documents](ex2-2-grounding-custom-documents.ipynb)
