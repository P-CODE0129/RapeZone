RapeZone Classification – Machine Learning Project

                                                                Project Overview

RapeZone Classification is a machine learning-based crime analysis system designed to identify areas with different levels of rape crime risk using historical data.

The project analyzes rape crime statistics across multiple years and classifies districts into different risk zones such as High Risk, Medium Risk, and Low Risk. The aim is to help identify potentially dangerous areas and improve public awareness and preventive planning.

The system uses historical crime data and machine learning techniques to detect patterns and generate predictions about crime risk levels

                                                                  Problem Statement

Rape is a serious public safety concern. Although crime data is available, it is often not used effectively for predictive analysis.
This project aims to analyze historical rape crime data and classify regions into future rape risk zones (High, Medium, Low) using machine learning techniques. 

The system can help:

-Identify high-risk areas

-Improve safety awareness

-Support preventive measures

Project Objectives

The main objectives of this project are:

-Analyze historical rape crime data across multiple years

-Identify patterns in crime occurrence

-Classify districts into High, Medium, and Low risk zones

-Provide safety alerts and awareness information based on risk level 

                                                                Methodology

The project follows a multi-step machine learning pipeline.

1. Data Collection

Crime data was collected from:
Rajasthan Police Dashboard
https://police.rajasthan.gov.in/portal/dashboard
The dataset includes crime data from 2016 – 2024. 

2. Data Parameters

The dataset contains the following features:

-District

-Year

-Age-wise rape victim counts:
    
    -Below 6 years
    
    -6–11 years
    
    -12–15 years
    
    -16–17 years
    
    -18–29 years
    
    -30–44 years
    
    -45–59 years
    
    -60+ years

-Total number of rape victims

3. Data Preprocessing

Before applying machine learning algorithms, the dataset is processed through:

-Data cleaning

-Handling missing values

-Feature selection

-Data normalization

-Splitting data into training and testing sets

4. Machine Learning Model

Machine learning algorithms are used to classify districts into rape risk zones.
The model analyzes historical crime patterns and predicts risk categories such as:

-High Risk Zone

-Medium Risk Zone

-Low Risk Zone

                                                                Project Focus

Although crime data across multiple Indian states was reviewed during the initial analysis, Rajasthan was identified as one of the states with relatively higher reported rape crime cases. Therefore, this project focuses specifically on analyzing Rajasthan crime data to study district-level and area-level patterns.

Using the available historical dataset from 2016–2024, the model first analyzes rape crime trends across districts of Rajasthan and classifies them into different risk zones (High, Medium, and Low).

To further refine the analysis, the project also examines the city or district within Rajasthan that shows the highest crime risk, and then applies the machine learning model at a more granular level to identify specific areas that fall under high-risk, moderate-risk, or low-risk categories.

This layered analysis helps in identifying both state-level and local-level risk patterns, allowing a better understanding of crime hotspots and potentially dangerous zones.

                                                              Output of the System

The final output of the system is a district-wise risk classification.

Each district is categorized into:

-High Risk Zone

-Medium Risk Zone

-Low Risk Zone

After identifying the district with the highest number of cases, the system further analyzes that district to identify specific areas that fall under highly risky, moderately risky, and safer zones.

Based on the classifications, the system can also provide safety alerts and helpline information to improve awareness and prevention.
