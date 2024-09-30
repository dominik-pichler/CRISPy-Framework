The aim is to create a knowledge database around the CRISP (DM/ML(Q)) Framework, by setting up the CRISP Phases in Graph, so that each action becomes a node.
Eventually, best practies will be collected and added as further nodes to each action node.
This collection is planed to be executed both by asking industry experts for best practices, as well as scraping and analysing scientific papers.



# CRISP ML(Q)

## 1. Business and Data Understanding

### a. Scope of Application
- Business Needs

### b. Measurable Success Criteria

#### i. Business Success Criteria
- Purpose and Success Criteria from a business point of view

#### ii. ML Success Criteria
- Define minimum acceptable level of performance to meet the business goals

#### iii. Economic Success Criteria
- Objective ML Success by Introduction of KPI(s)

### c. Feasibility

#### i. Applicability of ML Technology

#### ii. Legal Constraints

#### iii. Requirements on the Application
1. Robustness
2. Scalability
3. Explainability
4. Resource Demand

### d. Data Collection

#### i. Data Collection Plan
- In terms of Cost and Time needed to collect enough consistent data

#### ii. Data Version Control
- Data is collected iteratively, hence (planned) modifications of the dataset should be documented

### e. Data Quality Verification

#### i. Data Description
- Expert Knowledge regarding datasets like expected value ranges of features, maximum number of missing values. Guide to identify non-plausible data

#### ii. Data Requirements

#### iii. Data Verification
- Initial data, added data & production data must be checked according to the requirements

### f. Review of Output Documents

## 2. Data Preparation

### a. Select Data

### b. Select Features

#### i. Can be separated into three categories:
1. Filter Methods
2. Wrapper Methods
3. Embedded Methods

#### ii. Would be good to have someone with expert knowledge have a look at it again.

#### iii. Data Selection
- Discarding features/samples should be well documented and strictly based on objective quality criteria

#### iv. Unbalanced Classes

### c. Clean Data

#### i. Noise reduction

#### ii. Data imputation

### d. Construct Data

#### i. Feature Engineering

#### ii. Data augmentation

### e. Standardized Data

#### i. File Format

#### ii. Normalization

## 3. Modelling

### a. Literature Research on Similar Problems

### b. Define Quality Measures of the Model
1. Robustness
2. Explainability
3. Scalability
4. Resource Demand
5. Model Complexity

### c. Model Selection

### d. Incorporate Domain Knowledge

### e. Model Training

### f. Model Compression

### g. Ensemble Methods

### h. Result Reproducibility
- Experimental Documentation

## 4. Evaluation 

### a. Validate Performance
- Come up with a plan to validate the performance

### b. Determine Robustness

### c. Increase Explainability

### d. Compare Results with Defined Success Criteria
  
## 5. Deployment 

### a. Define Inference Hardware
  
### b.Model Evaluation under Production Condition
  
### c.Assure User Acceptance and Usability
  
### d.Minimize Risks of Unforeseen Errors
  
### e.Deployment Strategy
  
## 6.Monitoring and Maintenance 

### a.Identity Risks for Performance Degradation 
1.Non-stationary data distributions/data drift 
2.Degradation of hardware 
3.System updates 
  
### b.Monitor 
1.Monitor all input signals and compared to training data -> in this way, updates in the input data could be caught.
2.What to do with anomalies in the input? 
3.Monitoring History of Performance 
  
### c.Update
