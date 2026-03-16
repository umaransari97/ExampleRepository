{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPPa2pSfD4EjP5CK4+i3grR",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/umaransari97/ExampleRepository/blob/master/FirstNotebook.ipynb/Python%20Tutorial/EvenFactor.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "fWoFN6Un2sFl",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "76c89f30-8359-482b-bcd7-9203b4435435"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter any number: 7\n"
          ]
        }
      ],
      "source": [
        "num = int(input(\"Enter any number: \"))\n",
        "\n",
        "for x in range(1, num + 1):\n",
        "    if (num % x == 0 and x % 2 == 0):\n",
        "        print(x, end=\",\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "N5UQqnwd0-tg"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}