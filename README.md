# Machine-Learning-Project-With-Deployement

This Particular Machine Learning Project Was Attempted In Our Early First Year Of CSE Which Was Based On The Fact That Teenagers Tend To Have Confusion In Deciding Which Field/Hobby They Fit In Or Love To Do , So We Attempted In Making Classification Model Which Could Help The Parents In Deciding Their Child's Area Of Interest.

## Classification Algorithm:
We Implemented Support Vector Classification Algorithm, In Short we performed classification by finding the hyper-plane that differentiates the classes very well,now ,to find the right hyper-plane we maximize the distances between nearest data point (either class) and it will help us to decide the right hyper-plane. 

You Can find the jupyter notebook code in the main directory as well as the dataset used for it containing 13 attributes and 3 labels

## Deployement:
When It Comes To Deploying Our Model Into Production , Flask a micro web framework helps us in doing ,pickle is used for serialzing the object structures or simply we can transfer the particular pickle file on any system without worrying about writing the whole code again and easily deploying it through web.

You can find the .pkl file as well App.py in the Flask directory
