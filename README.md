# Tomato leaf disease prediction using Keras

## Overview
This is a Flask web application where you can upload images of a tomato leaf to predict disease. The diseases are classified into ten categories, as follows

**Classification** <br>
we have 10 classification of tomato leaf disease. The datasets used here are from kaggle, you can find it [here](https://www.kaggle.com/noulam/tomato).
```
├── Tomato___Bacterial_spot
├── Tomato___Early_blight
├── Tomato___healthy
├── Tomato___Late_blight
├── Tomato___Leaf_Mold
├── Tomato___Septoria_leaf_spot
├── Tomato___Spider_mites Two-spotted_spider_mite
├── Tomato___Target_Spot
├── Tomato___Tomato_mosaic_virus
├── Tomato___Tomato_Yellow_Leaf_Curl_Virus
```
1. Bacterial leaf spot <br>
<img target="_blank" src="https://64.media.tumblr.com/8230b8fdcb9aae40d2226ad81293eaa4/818c76b468486cd4-33/s400x600/46ee0e63515008e750b78d91c94618acf134de81.png">

2. Early blight<br>
<img target="_blank" src="https://64.media.tumblr.com/7133efcbcfaa9a73e09694f535551935/60875737a88cf4a3-05/s400x600/2ddd83685f1df0b5650f53cd8c026d70ce130333.png">

3. Healthy<br>
<img target="_blank" src="https://64.media.tumblr.com/dc944f6150a2eafa9df80eddbda62ae2/4a1fa647137c377c-be/s400x600/ccdfd3f1095918d8639318fbd58ae9b10de8168c.png">

4. Late blight<br>
<img target="_blank" src="https://64.media.tumblr.com/bf55da9bec41aac6fe86e1c7cc7e1395/decd44a2c574b035-6e/s400x600/fb011146eb72a9e7503c41e053a7b0f9b6e53fd3.png">

5. Leaf Mold<br>
<img target="_blank" src="https://64.media.tumblr.com/fd46207c550a6f252e8622bea86149b4/f49d77f13d1f1aaf-4e/s400x600/2c7ad24081d12e02467c5e10ada8da683bfe2483.png">

6. Septoria leaf spot<br>
<img target="_blank" src="https://64.media.tumblr.com/6d3494411082db7d00454f19a8e08941/bc626da6a4ba077b-56/s400x600/fa9d2ce125468355cc401e16dcd4e2c4bf3c7fb7.png">

7. Two-spotted spider mite<br>
<img target="_blank" src="https://64.media.tumblr.com/bb1cb4fa98aff8088f20c8b81a084714/e64c6a41ee4f80b3-ec/s400x600/afa03f4da5feda6f662bb4f683bcce7438611a77.png">

8. Target Spot<br>
<img target="_blank" src="https://64.media.tumblr.com/56e4422683995807502b15eba9770437/ce8cb92df5bcb454-da/s400x600/51d02ccab6c871655001f4ae4462aa2be103f68a.png">

9. Mosaic virus<br>
<img target="_blank" src="https://64.media.tumblr.com/866b9cd688e7d84b65353d071c5d667c/df067f4bf4ec75ac-4a/s400x600/5d1bcf193334e96b1cdc90d4f5936472fb5e1c6e.png">

10. Yellow Leaf Curl Virus<br>
<img target="_blank" src="https://64.media.tumblr.com/a63357c6d4eaff57f97d45665a4939a4/902957b75b8cf86c-3b/s400x600/304dd101d0f52ff4f744d0acafbd4b0c2201c10a.png">

## Coded on Kaggle notebook
1. Importing the essential libraries.
<img target="_blank" src="https://64.media.tumblr.com/2653f8f5c8160b76e7e8732d8eac292d/f4b26b63d9bd44e6-0d/s1280x1920/f4f74f272de831eeaa3e1c01ccf769701569938f.png">

2. Setting up the augmentation confiuration for the training.
<img target="_blank" src="https://64.media.tumblr.com/2a2fcdfa8ba27755f4517ca45573fb97/f4b26b63d9bd44e6-80/s1280x1920/4507bfb6e83b3bfd241a67327b8cbf9cd176db87.png">

3. Setting up the training and validation data locations and their target sizes.
<img target="_blank" src="https://64.media.tumblr.com/cf912ee4d95ee894d5833dadc412480b/f4b26b63d9bd44e6-38/s1280x1920/cfc44f65a6c7132c19ad4725eed489558f2f8654.png">

4. Applying transfer learning and keeping the base_model.layers as it is until newly added resonable weights.
<img target="_blank" src="https://64.media.tumblr.com/c6f5dc2b1a502ff598c6f08580b65e91/f4b26b63d9bd44e6-15/s1280x1920/dba9d802fc3aec1a997ba1f737e9dc1e5f67faf2.png">

5. Excuting model summary to understand the output shape of our model laye.
<img target="_blank" src="https://64.media.tumblr.com/628903ae3d2d4d084c0a67af20c8f883/1dea12d48a35a1f9-0f/s1280x1920/3d4594dcafa07bc09c699d22d7891991537ac60b.png">

6. Setting the learning rate and optimizer.
<img target="_blank" src="https://64.media.tumblr.com/e51a26404f241d06224b840d80a8e93a/1dea12d48a35a1f9-2e/s1280x1920/7514f6dd83f00c75fd9906e00a48c107f5c7b7db.png">

7. Training model through fit method to get resonable weights.
<img target="_blank" src="https://64.media.tumblr.com/f7e543601e1ef7dd2ce920ba84c6ac60/1dea12d48a35a1f9-5f/s1280x1920/cd6cc0735b9080c95e02695adb65b4a5ca14c72a.png">

8. Training and validation, Accuracy and loss has been visualized using matplotlib.
<img target="_blank" src="https://64.media.tumblr.com/6efc9f32be266f2b2954ef69fa22eb32/1dea12d48a35a1f9-6b/s1280x1920/08a745ae1b6bf304be5060860d41fcd22820f0fc.png">

9. After the first model fitting our model, Validation accuracy rose to 90.89%.
<img target="_blank" src="https://64.media.tumblr.com/ed8148e0dc0423df13e28fba914851fa/d25520b80d2fbb17-18/s1280x1920/74f46e16091b1378c2c7179b40f4e4af1328f2b5.png">

10. Fitting the model again to improve the accuracy.
<img target="_blank" src="https://64.media.tumblr.com/3e1e4ebb5f637d893c1208e26802a7cf/d25520b80d2fbb17-4e/s1280x1920/529c6ec11242faa5fe00c76b7d8c42ef767ce78b.png">

11. Again after the model fitting our model, Validation accuracy rose to 98.62%.
<img target="_blank" src="https://64.media.tumblr.com/fe24a611adb4066146059a7b22dbc3f3/d25520b80d2fbb17-6c/s1280x1920/2fd6d7ce5f881b3b6ad745521a1ca5dea834b374.png">

12. Training and validation, new Accuracy and loss has been visualized.
<img target="_blank" src="https://64.media.tumblr.com/4972dce49a38af2acc89a16ffee3fbd7/d25520b80d2fbb17-7b/s1280x1920/cd3bbdf00d8a523bb2b8defb3b205d92a13bfb26.png">

13. Saving the weights.
<img target="_blank" src="https://64.media.tumblr.com/a8aa77cd841affb58843efa434e209de/d25520b80d2fbb17-31/s1280x1920/37e0bb04d0081a04198d21ba188678e42062bdbf.png">

## Demo
<img target="_blank" src="https://64.media.tumblr.com/acbfbd0d8e3fd727f06529acf8170892/960ca4f847eb658e-dd/s1280x1920/7cf1580b82948b22fd889faafb39770764f95440.png">

<img target="_blank" src="https://64.media.tumblr.com/9d6c747f9b4cf098660791a947ea5cba/960ca4f847eb658e-09/s1280x1920/56cc60abd93a13f4d725ba06150f5a0511c43e53.png">

## Technologies Used
[<img target="_blank" src="https://www.gstatic.com/devrel-devsite/prod/vbd0faab6c0701e17b2f66039dd03326fc0e1627ecbcddaec4cd383df8dda622c/tensorflow/images/lockup.svg" height=50>](https://www.tensorflow.org/) [<img target="_blank" src="https://keras.io/img/logo-small.png" height=50>](https://keras.io/) [<img target="_blank" src="https://numpy.org/doc/stable/_static/numpylogo.svg" height=50>](https://numpy.org/doc/stable/user/index.html) [<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" height=50>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://werkzeug.palletsprojects.com/en/1.0.x/_static/werkzeug.png" height=50>](https://werkzeug.palletsprojects.com/en/1.0.x/)
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
