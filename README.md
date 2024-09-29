# Dementia AI Classification

![GitHub License](https://img.shields.io/github/license/Nishanth-Kunchala/Hack_AI_2024)
![GitHub repo size](https://img.shields.io/github/repo-size/Nishanth-Kunchala/Hack_AI_2024)

Copyright © 2024 RandomKiddo, Nishanth-Kunchala, Jacoube, danield33

___

### Motivation

We wanted to create a classification model that would be able to detect if a patient has dementia based on a set of 61 layers of an MRI scan. If successful, this model could be a support tool for doctors to detect if a patient has dementia. It may not be the definitive way to detect if a patient has dementia, but it could be helpful for doctors to see what the model thinks the patient has and with what confidence.

___

### Data

The data comes from the OASIS Alzheimer's dataset, a public dataset consisting of 80,000 MRI images. Since 61 MRI images are for a single patient, it means we have over 1300 patients worth of data in this dataset. The data was downloaded from [Kaggle](https://www.kaggle.com/datasets/ninadaithal/imagesoasis), but can also be accessed through the [OASIS website](https://sites.wustl.edu/oasisbrains/).

___

### The HackAI 2024 Model

As a part of the OSU AI Club Hack AI 2024, this project was selected by the team to try in complete in the 24-hour hackathon. We downsized the OASIS images and converted them to grayscale to decrease training time and complexity. We stacked each of the 61 MRI images per patient into a 3D tensor as a numpy `ndarray` and saved the patient's 3D MRI scan as an `.npz` file. We then amplified some of the moderate dementia and mild dementia samples through duplication, as there weren't many patients with that classification. We then created a Tensorflow functional model to train on the sample data. 

Although we had a good training accuracy, we had a relatively low testing accuracy (indicating overfitting). Unfortunately, due to not having access to a GPU at the hackathon, we could not GPU accelerate the model, and we did not have enough time to test a simpler model. The training accuracy was in the high 90% range, but the testing accuracy hovered around high 70%. 

___

### This Model & Results

The new model was created in a different repository and then integrated to this one. To see the other repository, visit [this page](https://www.github.com/RandomKiddo/DementiaAI). To see the older model, look back further in the commits.

We revisited this model to try and create a better model. We continued to use the stacked 3D tensors. The creation file for them is located in the `npz_generation.py` file. 

We created a simpler Tensorflow functional model and GPU accelerated with an NVIDIA RTX 3060 to decrease training time. We added training callbacks of `ModelCheckpoint` and `EarlyStopping` to save the best possible model. We got a training accuracy of 100% (it isn't really 100%, it is being rounded) with a testing accuracy of 97.31%, indicating that our model makes much better generalizations this time around.

Loss and accuracy graphs:

![Accuracy Graph](accuracy.png)
![Loss Graph](loss.png)

___

[Back to Top](#dementia-ai-classification)

<sub>This page was last edited on 09.28.2024</sub>