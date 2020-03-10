# Requirements Document
## Requirements
* As **someone concerned about heart disease,** I would like to **enter a simple test result and receive graphical and numerical results of my heart disease risk over time.** This will allow me to **easily interpret the prediction and make better overall health choices.** 
* As **a person confirmed to be suffering from heart disease,** I would like to **have the highest risk areas highlighted for me, with links to resources to address these issues.** This will allow me to **target the most important areas first.**
* As **a user,** I would like to be able to **enter a minimal subset of test features.** This is because medical tests are expensive and invasive and I would like **to receive results with as little distress as possible.**
* As a **website user**, I want to **be able to submit feedback,** so that the **website owners can consider my opinions and concerns** during future website updates.
* As a **user** I want to **know my chances of getting a stroke in a span of 6-12 months.** This is so I can **take a more proactive approach to my healthcare.**
* As a user, I would like **to have the description of each field** so that **it will be easy for me to understand the input I need to supply.**
* As an **end user** I would like the tests **to be accurate and free from false positives.**
## Modularity
Modularity will be achieved by separating the functionality of the program into different folders within the directory structure and developing modules within these.  
Splitting up the application like this is a minor step, but will hopefully set the standard for modularity that will propagate down to the individual modules.  
Currently, the structure is planned as follows:  
. <br/>
+-- app <br/>
|   +-- (application files, scripts and templates) <br/>
+-- analysis <br/>
|	+-- (data analysis scripts) <br/>
+-- database <br/>
|	+-- (database scripts and plumbing) <br/>
+-- docs <br/>
|	+-- (documentation) <br/>
+-- docker <br/>
|	+-- (docker config files) <br/r>
+-- (Other config files) <br/>

## Testing
Since this project is relatively small, only unit tests should be considered and these should be written for every module.
