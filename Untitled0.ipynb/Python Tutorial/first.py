{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNtbGvua5wu68Dy+npt/ykk",
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
      "execution_count": null,
      "metadata": {
        "id": "fWoFN6Un2sFl"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "source": [
        "# to find out hcf\n",
        "\n",
        "# input two numbers\n",
        "num1 = int(input(\"Enter first number: \"))\n",
        "num2 = int(input(\"Enter second number: \"))\n",
        "\n",
        "# -----------------\n",
        "\n",
        "if num2 == 0:\n",
        "    print(\"HCF:\", num1)\n",
        "\n",
        "else:\n",
        "    while num2 != 0:\n",
        "        rem = num1 % num2\n",
        "        num1 = num2\n",
        "        num2 = rem\n",
        "\n",
        "    print(\"HCF:\", num1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QryC3eEG4NDI",
        "outputId": "2aef10bc-eddd-4c7c-a31c-ee522619f5d5"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter first number: 2\n",
            "Enter second number: 3\n",
            "HCF: 1\n"
          ]
        }
      ]
    }
  ]
}