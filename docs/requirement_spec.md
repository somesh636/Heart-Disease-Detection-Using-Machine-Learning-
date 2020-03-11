\# Requirements Document
## Requirements
### Functional
* The user should enter their test data and receive graphical and numerical results of their heart disease risk over time. This should take the form of charts and perhaps an index or score of their heart disease risk.
* Upon receiving results, the highest risk areas should be prominent so that the user can address these first. Links to resources are also necessary.
* There must be a method for data entry which permits a minimal subset of features. That is, the analysis can run with the minimum data but not necessarily well. Any less should be forbidden.
* The user should be able to submit feedback by some method, for example an email form, chat box or similar.
* The user should have an alert or notification if their chance of stroke within 6-12 months is high.

### Non-functional
#### Look and Feel
* Each field for data input should have a heading describing what is inspected. A full description should be readily available, eg by mousing over the input field.
#### QoS
* The tests should return accurate results so some kind of visual indication of confidence should be available.

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
|	+-- (docker config files) <br/>
+-- (Other config files) <br/>

## Testing
Since this project is relatively small, only unit tests should be necessary and must therefore take priority. However, higher level tests should be considered and implemented if possible.
