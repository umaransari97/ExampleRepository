{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNi3sRE5MV9wZ9qC47F3Jxj",
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
        "<a href=\"https://colab.research.google.com/github/umaransari97/ExampleRepository/blob/master/Untitled0.ipynb/Python%20Tutorial/first.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "fWoFN6Un2sFl",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "69c1eaee-f153-430d-fec7-29ad982b530e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 654\n",
            "Greatest digit is: 6\n"
          ]
        }
      ],
      "source": [
        "# find greatest digit\n",
        "\n",
        "#taking input from user\n",
        "num1 = int(input(\"Enter a number: \"))\n",
        "greatest = 0\n",
        "\n",
        "while num1 > 0:\n",
        "    a = num1 % 10\n",
        "    if a > greatest:\n",
        "        greatest = a\n",
        "    num1 = num1 // 10\n",
        "\n",
        "print(\"Greatest digit is:\", greatest)"
      ]
    }
  ]
}