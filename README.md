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
## Coding on Google colab

1. Importing the necessary libraries.

2. Re-size all the images to 224x224
<img target="_blank" src="https://64.media.tumblr.com/522c98f2afe8d5cbcaf9632d69548f42/fa5cfac4f5044686-22/s1280x1920/b654e98e786a0b3931e24a27559c6a8e59d21f56.png">

3. Choosing weights as imagenet and a for loop to remove the existing weights from InceptionV3
<img target="_blank" src="https://64.media.tumblr.com/a6917fea505af6ea040efc02f4881a25/fa5cfac4f5044686-04/s1280x1920/d2c0f237b6be77fdf44bd05e6ce58db3fbc7f92d.png">

4. Flattening and defining prediction and model
<img target="_blank" src="https://64.media.tumblr.com/a3b470f19772a9624fdc8c6d3e7046d3/fa5cfac4f5044686-4c/s1280x1920/41c6f16116638dc64b51d3417e21e7905fb6b0fb.png">

5. Assigning cost and optimization
<img target="_blank" src="https://64.media.tumblr.com/ae80081fd5454539c57a45f7bdca2741/fa5cfac4f5044686-14/s1280x1920/7097d9108de2fe77c57c0f0da9ce0021e094917d.png">

6. Use the Image Data Generator to import the images from the dataset
<img target="_blank" src="https://64.media.tumblr.com/653d023273e81aee5d69c02ce46fed61/5da56777df81066d-d9/s1280x1920/50a952410e931ec92feda8442da14e8bf57b8398.png">

7. Fitting the model
<img target="_blank" src="https://64.media.tumblr.com/e4c2db7be8b020739859483a0b4f3827/5da56777df81066d-f7/s1280x1920/07f7bafd049b18ff61b9384e3c812a7b017ca0e1.png"> 

8. Analysing Accuracy loss and validation loss based on epochs
<img target="_blank" src="https://64.media.tumblr.com/c3c75eb90617e8a551bfcb673a402c45/5da56777df81066d-a7/s1280x1920/bfb5933c1b47a8aebfa03eb333957c1e36e8614c.png">

9. Saving the model
<img target="_blank" src="https://64.media.tumblr.com/ec6dd568b973b8984eb219f08b9e3c00/5da56777df81066d-e1/s1280x1920/f6871a8130971d540f83574a815b6dbe93a81100.png">

## Demo


## Technologies Used
[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" height=50>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://www.gstatic.com/devrel-devsite/prod/vbd0faab6c0701e17b2f66039dd03326fc0e1627ecbcddaec4cd383df8dda622c/tensorflow/images/lockup.svg" height=50>](https://www.tensorflow.org/) [<img target="_blank" src="https://keras.io/img/logo-small.png" height=50>](https://keras.io/) [<img target="_blank" src="https://numpy.org/doc/stable/_static/numpylogo.svg" height=50>](https://numpy.org/doc/stable/user/index.html) [<img target="_blank" src="https://werkzeug.palletsprojects.com/en/1.0.x/_static/werkzeug.png" height=50>](https://werkzeug.palletsprojects.com/en/1.0.x/)
<br>
[![made-with-python](https://img.shields.io/badge/made%20with-Python-yellow)](https://www.python.org/) [![made-with-colab](https://img.shields.io/badge/made%20with-Google%20Colab-yellowgreen)](Colabcolab.research.google.com)

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
