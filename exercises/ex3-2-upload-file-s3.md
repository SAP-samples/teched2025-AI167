# Exercise 3.2: Upload file to S3 Object Store

Before we can use the Pipeline API to create a data grounding pipeline we first need to ingest our document to da supported data source.
Overall the grounding module in GenAI Hub supports as of today the following data repositories:
* Microsoft Share Point 
* AWS S3
* SFTP 
* SAP Build Work Zone
* SAP Document Management Service.

For this Hands-on Session we will use the **AWS S3 object store** as data repository. 

For these step we are again use our API Client Bruno (Hope Kasimir is ok with that). 


## Configure connection to S3 Object Store 
➡️ Go Back to **Bruno** and expand ```AI167_S3ObjectStore``` (1).   
➡️ Click at top right corner on ```No Environments``` (2)      
➡️ Select ```Configure``` to start setting the environment variables. 
<p>
<img src="images/s3_open_env.png" width="900"/>
</p>

The values for the respective key you get from the service key from your Object Store Instance on BTP Cockpit. 

➡️ Take values from TECHED2025-AI167/.objectStore-config.json and copy the respective value from the service key into Bruno.

➡️ After you added teh values, select **Save** and then **Activate**

<p>
<img src="images/s3_save_activate.png" width="900"/>
</p>

## Configure connection to S3 Object Store 
➡️ Click on ```POST S3-Upload```to expand the folder (1).   
➡️ Select in the **Body** ```Select File``` to upload the file.   
<p>
<img src="images/s3_select_file.png" width="900"/>
</p>

We want to upload **Kasimirs SAP TechEd Edition.pdf** to the Object Store. 
➡️ Navigate to  ```TECHED2025-AI167/exercise/document```and select ```Kasimirs SAP TechEd Edition.pdf```and select **Open**.
<p>
<img src="images/s3_open_file.png" width="900"/>
</p>

➡️  Run the request.

To check whether everything was successfully uploaded you can run the ```GET List Objects ``` request. 

## From now, continue the exercise in Visual Studio Code
 
Continue to - [Exercise 3.3: Run data pipeline to vectorize documents](ex3-3-grounding-data-pipeline.ipynb)
 <p>
<img src="images/Use_vs_code.png" width="900"/>
</p>