{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "30c3fb4d",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'tensorflow'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_8556/3352972557.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mkeras\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdatasets\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mfashion_mnist\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mtrain_X\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mtrain_Y\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mtest_X\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mtest_Y\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfashion_mnist\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mload_data\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\keras\\__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     19\u001b[0m \"\"\"\n\u001b[0;32m     20\u001b[0m \u001b[1;31m# pylint: disable=unused-import\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 21\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mtensorflow\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpython\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mtf2\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     22\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mkeras\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mdistribute\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     23\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'tensorflow'"
     ]
    }
   ],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ad15c38e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: keras in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (2.6.0)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: You are using pip version 21.2.3; however, version 21.3.1 is available.\n",
      "You should consider upgrading via the 'C:\\Users\\sewel\\AppData\\Local\\Programs\\Python\\Python39\\python.exe -m pip install --upgrade pip' command.\n"
     ]
    }
   ],
   "source": [
    "!pip install keras"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ff15dda9",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'tensorflow'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_8556/684823904.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mkeras\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdatasets\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mfashion_mnist\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mtrain_X\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mtrain_Y\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mtest_X\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mtest_Y\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfashion_mnist\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mload_data\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\keras\\__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     19\u001b[0m \"\"\"\n\u001b[0;32m     20\u001b[0m \u001b[1;31m# pylint: disable=unused-import\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 21\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mtensorflow\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpython\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mtf2\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     22\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mkeras\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mdistribute\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     23\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'tensorflow'"
     ]
    }
   ],
   "source": [
    "from keras.datasets import fashion_mnist\n",
    "(train_X,train_Y), (test_X,test_Y) = fashion_mnist.load_data()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "36950491",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: tensorflow in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (2.6.0)\n",
      "Requirement already satisfied: wheel~=0.35 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (0.37.0)\n",
      "Requirement already satisfied: gast==0.4.0 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (0.4.0)\n",
      "Requirement already satisfied: absl-py~=0.10 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (0.15.0)\n",
      "Requirement already satisfied: wrapt~=1.12.1 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (1.12.1)\n",
      "Requirement already satisfied: grpcio<2.0,>=1.37.0 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (1.41.0)\n",
      "Requirement already satisfied: clang~=5.0 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (5.0)\n",
      "Requirement already satisfied: keras-preprocessing~=1.1.2 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (1.1.2)\n",
      "Requirement already satisfied: protobuf>=3.9.2 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (3.19.0)\n",
      "Requirement already satisfied: termcolor~=1.1.0 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (1.1.0)\n",
      "Requirement already satisfied: keras~=2.6 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (2.6.0)\n",
      "Requirement already satisfied: tensorboard~=2.6 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (2.7.0)\n",
      "Requirement already satisfied: astunparse~=1.6.3 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (1.6.3)\n",
      "Requirement already satisfied: tensorflow-estimator~=2.6 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (2.6.0)\n",
      "Requirement already satisfied: opt-einsum~=3.3.0 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (3.3.0)\n",
      "Requirement already satisfied: six~=1.15.0 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (1.15.0)\n",
      "Requirement already satisfied: numpy~=1.19.2 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (1.19.5)\n",
      "Requirement already satisfied: flatbuffers~=1.12.0 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (1.12)\n",
      "Requirement already satisfied: google-pasta~=0.2 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (0.2.0)\n",
      "Requirement already satisfied: h5py~=3.1.0 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (3.1.0)\n",
      "Requirement already satisfied: typing-extensions~=3.7.4 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorflow) (3.7.4.3)\n",
      "Requirement already satisfied: google-auth<3,>=1.6.3 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorboard~=2.6->tensorflow) (2.3.0)\n",
      "Requirement already satisfied: google-auth-oauthlib<0.5,>=0.4.1 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorboard~=2.6->tensorflow) (0.4.6)\n",
      "Requirement already satisfied: tensorboard-data-server<0.7.0,>=0.6.0 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorboard~=2.6->tensorflow) (0.6.1)\n",
      "Requirement already satisfied: requests<3,>=2.21.0 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorboard~=2.6->tensorflow) (2.26.0)\n",
      "Requirement already satisfied: markdown>=2.6.8 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorboard~=2.6->tensorflow) (3.3.4)\n",
      "Requirement already satisfied: werkzeug>=0.11.15 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorboard~=2.6->tensorflow) (2.0.2)\n",
      "Requirement already satisfied: setuptools>=41.0.0 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorboard~=2.6->tensorflow) (57.4.0)\n",
      "Requirement already satisfied: tensorboard-plugin-wit>=1.6.0 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from tensorboard~=2.6->tensorflow) (1.8.0)\n",
      "Requirement already satisfied: cachetools<5.0,>=2.0.0 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from google-auth<3,>=1.6.3->tensorboard~=2.6->tensorflow) (4.2.4)\n",
      "Requirement already satisfied: rsa<5,>=3.1.4 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from google-auth<3,>=1.6.3->tensorboard~=2.6->tensorflow) (4.7.2)\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from google-auth<3,>=1.6.3->tensorboard~=2.6->tensorflow) (0.2.8)\n",
      "Requirement already satisfied: requests-oauthlib>=0.7.0 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from google-auth-oauthlib<0.5,>=0.4.1->tensorboard~=2.6->tensorflow) (1.3.0)\n",
      "Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from pyasn1-modules>=0.2.1->google-auth<3,>=1.6.3->tensorboard~=2.6->tensorflow) (0.4.8)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard~=2.6->tensorflow) (2021.5.30)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard~=2.6->tensorflow) (1.26.7)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard~=2.6->tensorflow) (2.0.6)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard~=2.6->tensorflow) (3.2)\n",
      "Requirement already satisfied: oauthlib>=3.0.0 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<0.5,>=0.4.1->tensorboard~=2.6->tensorflow) (3.1.1)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: You are using pip version 21.2.3; however, version 21.3.1 is available.\n",
      "You should consider upgrading via the 'C:\\Users\\sewel\\AppData\\Local\\Programs\\Python\\Python39\\python.exe -m pip install --upgrade pip' command.\n"
     ]
    }
   ],
   "source": [
    "!pip install tensorflow\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2e47d32b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/train-labels-idx1-ubyte.gz\n",
      "32768/29515 [=================================] - 0s 1us/step\n",
      "40960/29515 [=========================================] - 0s 1us/step\n",
      "Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/train-images-idx3-ubyte.gz\n",
      "26427392/26421880 [==============================] - 2s 0us/step\n",
      "26435584/26421880 [==============================] - 2s 0us/step\n",
      "Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/t10k-labels-idx1-ubyte.gz\n",
      "16384/5148 [===============================================================================================] - 0s 0s/step\n",
      "Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/t10k-images-idx3-ubyte.gz\n",
      "4423680/4422102 [==============================] - 0s 0us/step\n",
      "4431872/4422102 [==============================] - 0s 0us/step\n"
     ]
    }
   ],
   "source": [
    "from keras.datasets import fashion_mnist\n",
    "(train_X,train_Y), (test_X,test_Y) = fashion_mnist.load_data()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9691fea1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training data shape :  (60000, 28, 28) (60000,)\n",
      "Testing data shape :  (10000, 28, 28) (10000,)\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "\n",
    "print('Training data shape : ', train_X.shape, train_Y.shape)\n",
    "\n",
    "print('Testing data shape : ', test_X.shape, test_Y.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a70b7133",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting matplotlib\n",
      "  Downloading matplotlib-3.4.3-cp39-cp39-win_amd64.whl (7.1 MB)\n",
      "Collecting cycler>=0.10\n",
      "  Downloading cycler-0.10.0-py2.py3-none-any.whl (6.5 kB)\n",
      "Requirement already satisfied: python-dateutil>=2.7 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from matplotlib) (2.8.2)\n",
      "Requirement already satisfied: pillow>=6.2.0 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from matplotlib) (8.3.2)\n",
      "Collecting kiwisolver>=1.0.1\n",
      "  Downloading kiwisolver-1.3.2-cp39-cp39-win_amd64.whl (52 kB)\n",
      "Requirement already satisfied: numpy>=1.16 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from matplotlib) (1.19.5)\n",
      "Requirement already satisfied: pyparsing>=2.2.1 in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from matplotlib) (2.4.7)\n",
      "Requirement already satisfied: six in c:\\users\\sewel\\appdata\\local\\programs\\python\\python39\\lib\\site-packages (from cycler>=0.10->matplotlib) (1.15.0)\n",
      "Installing collected packages: kiwisolver, cycler, matplotlib\n",
      "Successfully installed cycler-0.10.0 kiwisolver-1.3.2 matplotlib-3.4.3\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: You are using pip version 21.2.3; however, version 21.3.1 is available.\n",
      "You should consider upgrading via the 'C:\\Users\\sewel\\AppData\\Local\\Programs\\Python\\Python39\\python.exe -m pip install --upgrade pip' command.\n"
     ]
    }
   ],
   "source": [
    "!pip install matplotlib\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7899e50f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total number of outputs :  10\n",
      "Output classes :  [0 1 2 3 4 5 6 7 8 9]\n"
     ]
    }
   ],
   "source": [
    "# Find the unique numbers from the train labels\n",
    "classes = np.unique(train_Y)\n",
    "nClasses = len(classes)\n",
    "print('Total number of outputs : ', nClasses)\n",
    "print('Output classes : ', classes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "60a4ec64",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Ground Truth : 9')"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=[5,5])\n",
    "\n",
    "# Display the first image in training data\n",
    "plt.subplot(121)\n",
    "plt.imshow(train_X[0,:,:], cmap='gray')\n",
    "plt.title(\"Ground Truth : {}\".format(train_Y[0]))\n",
    "\n",
    "# Display the first image in testing data\n",
    "plt.subplot(122)\n",
    "plt.imshow(test_X[0,:,:], cmap='gray')\n",
    "plt.title(\"Ground Truth : {}\".format(test_Y[0]))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d0ada237",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
