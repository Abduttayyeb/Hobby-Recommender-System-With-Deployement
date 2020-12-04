DEMO: https://hobby-recommender.herokuapp.com/
# Machine-Learning-Project-With-Deployement

This Machine Learning Project was attempted in our early first year of CSE which was based on the fact that tenagers tend to have confusion in deciding which Field/Hobby they fit in or love to do, so we attempted in making a classification model which could help the Parents in deciding their child's Area Of Interest.

## Classification Algorithm:
We Implemented Support Vector Classification Algorithm, In Short we performed classification by finding the hyper-plane that differentiates the classes very well,now ,to find the right hyper-plane we maximize the distances between nearest data point (either class) and it will help us to decide the right hyper-plane. 

You Can find the jupyter notebook code in the main directory as well as the dataset used for it containing 13 attributes and 3 labels

## Deployement:
Deployed our model successfully into production through Flask a micro web framework helps us in build web based applications, pickle is used for serialzing the object structures or simply we can transfer the particular pickle file on any system without worrying about writing the whole code again and easily deploying it through web.

You can find the .pkl file as well App.py in the Flask directory
