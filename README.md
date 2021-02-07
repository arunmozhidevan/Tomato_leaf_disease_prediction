# Tomato disease predition using Keras
Possibly contains awesomeness and Tomato disease predition related files

## Overview
This is a Flask web app which predicts the Tomato plant diseases which developed using python(Jupyter Notebook).

## Installation
Here The Code is written in Python 3.6 using tensorflow_gpu-1.12.0 with cuda 9.0 and cuDNN 7.6.5 for GPU programming.
If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip, navigate into the installed python directory and open command promt:
```bash
python -m pip install --upgrade pip
```
1. If you have Nvidia and you are going to use GPU programming first find the cuda version of your graphics card. By navigating to NVidia control panel > Help > System Information and click on the components tab.
2. After finding the cuda version, click [here](https://developer.nvidia.com/cuda-toolkit-archive) to download specific cuda.
3. Next we have to download the cuDNN, click [here](https://developer.nvidia.com/rdp/cudnn-archive) to download specific cuDNN to you cuda.
4. Install cuda and copy and replace the cuDNN files in the cuda folder in your windows C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0
5. system properties > advanced system settings > environment variables > under system variables > Verify PATH has 'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\bin' and 'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\libnvvp', Note for me its v9.
6. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html#miniconda) or [Anaconda](https://www.anaconda.com/products/individual)
7. Install tensorflow-gpu using conda command prompt
```bash
conda create --name tf_gpu tensorflow-gpu 
```
8. Install keras
```bash
conda install -c conda-forge keras
```
9. Install pillow
```bash
conda install -c anaconda pillow
```
## Coding on Jupyter Notebook
1. After importing the necessary libraries, load the excel sheet using pandas read_excel
<img target="_blank" src="https://64.media.tumblr.com/cbffa66fec5375457ff0f5407b503f3b/494bc3862fd97b16-69/s1280x1920/78f12d4de2a2bebe03dcde4d67bd1d01f4e4e438.png">

2. Data cleaning: Since we have only a few NaN data, we are going to drop the NaN rows
<img target="_blank" src="https://64.media.tumblr.com/05f2274f5da35ccc3340dc2d7a1111ad/e134c79da8b817d9-b3/s1280x1920/bd08a5e0e23fc4478f93d9b8cd0186b8a5e4c59d.png">


3. Feature extraction: get the unique value of Airline, Source, Destination, Total_Stops of the catecorical data which will be doing one hot encoding and label encoding
<img target="_blank" src="https://64.media.tumblr.com/a1a2fa3f732cffeaccfa17d9d4fcb5eb/494bc3862fd97b16-aa/s1280x1920/2f52f00b5500ea729e63f8381d02bf0c40b9fd75.png">

4. Feature extraction: extracting day and month from the time stamp for arrival_time and dep_time
<img target="_blank" src="https://64.media.tumblr.com/b2bc203943b82b1ef9da2223548a7439/3621f30b68b85d4e-cd/s1280x1920/159aec8ed666c14db120e6dbd5ebd1f704dfc2ad.png">

5. Feature extraction: calculating duration from arrival_time and dep_time
<img target="_blank" src="https://64.media.tumblr.com/e72708d7e537fb1839691174c16a21a7/e134c79da8b817d9-ce/s1280x1920/4f7101283fd1507eefe55446e069e17c90696a1c.png">

5. Handling Categorical Data: performing one hot encoding on the nominal data (Airline, Source, Destination)
<img target="_blank" src="https://64.media.tumblr.com/5ab5dfb88e6c38308d92066d2c122d3e/e134c79da8b817d9-61/s1280x1920/fef1da728dc05585f82748b578e27b6dbe841fcb.png">

6. Handling Categorical Data: performing label encoding on the ordinal data (Total_Stops)
<img target="_blank" src="https://64.media.tumblr.com/65aa2c3de38ce9e1047887cd0734f2a6/3621f30b68b85d4e-e4/s1280x1920/c23835fbe2fde33d51e25c1dbe97a395f3d7c29b.png">

7. Feature selection: assigning indiviual and target variables for trainging
<img target="_blank" src="https://64.media.tumblr.com/57c247e4204e6a380a8d72126ccff0a5/3621f30b68b85d4e-c9/s1280x1920/c27e1592389a8595297f840d58604ef7cab24ac1.png">

8. Feature selection: finding the feature importance using ExtraTreesRegressor from sklearn
<img target="_blank" src="https://64.media.tumblr.com/3bf77f3a84d459e46d7ebd38340f9108/3621f30b68b85d4e-a9/s1280x1920/2088a0bb748a0fa239fb2029f55a9ab03fba2249.png">

9. Performing train test split
<img target="_blank" src="https://64.media.tumblr.com/fa9df9531b34fce274a6caafd3243a92/d0b9c2df5dd2d39c-dc/s1280x1920/18d448fdeda1bcdd94bc5dcf409a0ae1c3429e23.png">

10 Importing Randomized Search CV from sklearn and fitting the model
<img target="_blank" src="https://64.media.tumblr.com/81ce6365ac82b2a62cc57fd85a232d4e/d0b9c2df5dd2d39c-c5/s1280x1920/a31016ed66b98124ff716fe9ee6ff39628f6b846.png">

<img target="_blank" src="https://64.media.tumblr.com/5da96056f1f5e36b5a0a582471520555/3621f30b68b85d4e-f8/s1280x1920/1ec6ec21cdba1cab715b03851fd835abba73af6e.png">

11. Calculating MAE MSE RMSE 
<img target="_blank" src="https://64.media.tumblr.com/39f39c26de15129dc1523672027d802f/3621f30b68b85d4e-cc/s1280x1920/189c226f1d15d9e1a62933da17be2c972c6c7753.png">

12. Saving the trained model as pickel
<img target="_blank" src="https://64.media.tumblr.com/7b08b37f9d09afb8a55ede4ed93d6516/3621f30b68b85d4e-fb/s1280x1920/f02e06f1f5dc4c9c665dd83f63490be921aaf6dd.png">

## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.

1. click > create new app
<img target="_blank" src="https://64.media.tumblr.com/0aead3e6710612287f7c3586ae3eb80c/3fafd73153537ff9-e7/s2048x3072/ee701c63d62cb3a12f38a84f392a4337be25e6b7.png">

2. in "App name" give a suitable app name for your project and click create app
<img target="_blank" src="https://64.media.tumblr.com/835f2d919c97703be0b62e37fbb80acb/2bd18ddb098acf53-b0/s1280x1920/40f119edfa41fa3699d4becfe5161cdb8ed95687.png">

3. choose github, add your repository name and click search
<img target="_blank" src="https://64.media.tumblr.com/db7ad57dce8db4112c94d2cdecefbc0b/852e853e46f155de-47/s1280x1920/82f0c655ec4c6bd1731874bea5fa557c7fd89f52.png">

4. after successful connection, click on "Deploy branch"
<img target="_blank" src="https://64.media.tumblr.com/2913051a7c514e205d33f14bdbed5057/4f88ec94f7a9d379-56/s1280x1920/b8893bd33120476bd19f31a2175ad5cbc597626e.png">

5. on successful deployment you get this message and click to view your app
<img target="_blank" src="https://64.media.tumblr.com/029bdfc5d6ab73e7cb4c51998659426b/3a090db3c9309298-99/s1280x1920/35b30c80e25da93e4ce32e61e8e469b7d91952a0.png">

You also use this [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Website
Link: https://flight-fare-prediction-amd.herokuapp.com/
[<img target="_blank" src="https://64.media.tumblr.com/9d08ed10a0fcd8f4f1f396329cccf571/666d8646b4207c28-70/s2048x3072/31da05f4dae9aee4d8411d1bd00da29c1a824da0.png" >](https://flight-fare-prediction-amd.herokuapp.com/)

[<img target="_blank" src="https://64.media.tumblr.com/69c6bae50ea35e91495c148922a6176b/666d8646b4207c28-a4/s2048x3072/748e560ff86a10930763bad9aee4aa05f6c66492.png" >](https://flight-fare-prediction-amd.herokuapp.com/)

## Technologies Used
[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" height=50>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" height=50>](https://gunicorn.org) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" height=50>](https://scikit-learn.org/stable/) [<img target="_blank" src="https://www.gstatic.com/devrel-devsite/prod/vbd0faab6c0701e17b2f66039dd03326fc0e1627ecbcddaec4cd383df8dda622c/tensorflow/images/lockup.svg" height=50>](https://www.tensorflow.org/)
<br>
[![made-with-python](https://img.shields.io/badge/made%20with-Python-yellow)](https://www.python.org/) [![made-with-jupyter](https://img.shields.io/badge/made%20with-Jupyter-orange)](https://jupyter.org/)

## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue](https://github.com/arunmozhidevan/tomato_disease/issues) here by including your search query and the expected result.

## Directory Tree 
```
├── static
│   ├── css
│   │   ├── main.css
│   ├── js
│   │   ├── main.js
├── templates
│   ├── home.html
├── README.md
├── app.py
├── model_inception.h5
├── requirements.txt
├── tomato.ipynb
```
