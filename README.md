# IRF_LLM
## 1 How to config the environments:
- on Ubuntu 20.04.5 
- cikit-learn==1.1.0
- matplotlib==3.7.4
- numpy==1.24.4
- numexpr==2.8.1
- python 3.8
- scipy==1.10.1
- sympy==1.10.1
- sympytorch==0.1.4
- typing_extensions==4.9.0
- torch==1.11.0
## 2 Prepare training data and model:
* Download the ```model.pt``` and ```data``` folder from the website ```https://drive.google.com/drive/folders/1PU-XqvDr2KSjpeaPBKGJNb8O4z0pu_up?usp=sharing```.  
* Download ```model.pt``` and put the ```model.pt``` and ```Example.py``` in the same folder.
* The ```data``` folder contains two folders, representing two types of high-frequency trading data for the stock market (the data has been preprocessed, without leaking any important information): the ```SSE50``` folder and the ```SP500``` folder. Both folders contain  ```5 input features(open,high,low,close and vwap) and one target```, respectively.
## 3 How to train model:
```python Example.py ```
