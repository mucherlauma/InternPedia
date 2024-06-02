{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPtmfiB1wPfT6lz5laPQP8x",
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
        "<a href=\"https://colab.research.google.com/github/mucherlauma/InternPedia/blob/main/CURRENCY_CONVERTER_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zoW5J7P1gpdC",
        "outputId": "40ffb086-2b9f-4505-bb67-b0690db91c91"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Welcome to the Currency Converter!\n",
            "Enter source currency (e.g., USD): USD\n",
            "Enter target currency (e.g., EUR): EUR\n",
            "Enter amount to convert: 100\n",
            "100.0 USD is equal to 92.22 EUR\n",
            "Do you want to convert another currency? (yes/no): yes\n",
            "Enter source currency (e.g., USD): GBP\n",
            "Enter target currency (e.g., EUR): AUD\n",
            "Enter amount to convert: 50\n",
            "50.0 GBP is equal to 95.74 AUD\n",
            "Do you want to convert another currency? (yes/no): no\n",
            "Exiting...\n"
          ]
        }
      ],
      "source": [
        "import requests\n",
        "\n",
        "def fetch_exchange_rates(base_currency):\n",
        "    \"\"\"\n",
        "    Fetch exchange rates from the Open Exchange Rates API.\n",
        "    \"\"\"\n",
        "    # Replace 'YOUR_APP_ID' with your actual app ID obtained by signing up at https://openexchangerates.org/signup\n",
        "    app_id = 'YOUR_APP_ID'\n",
        "    url = f'https://open.er-api.com/v6/latest/{base_currency}?app_id={app_id}'\n",
        "\n",
        "    try:\n",
        "        response = requests.get(url)\n",
        "        data = response.json()\n",
        "        return data['rates']\n",
        "    except Exception as e:\n",
        "        print(\"Error fetching exchange rates:\", e)\n",
        "        return None\n",
        "\n",
        "def convert_currency(amount, source_currency, target_currency):\n",
        "    \"\"\"\n",
        "    Convert the given amount from source currency to target currency.\n",
        "    \"\"\"\n",
        "    rates = fetch_exchange_rates(source_currency)\n",
        "\n",
        "    if rates is not None:\n",
        "        if target_currency in rates:\n",
        "            converted_amount = amount * rates[target_currency]\n",
        "            return converted_amount\n",
        "        else:\n",
        "            print(f\"Error: Target currency '{target_currency}' not found.\")\n",
        "            return None\n",
        "\n",
        "def main():\n",
        "    print(\"Welcome to the Currency Converter!\")\n",
        "    while True:\n",
        "        try:\n",
        "            source_currency = input(\"Enter source currency (e.g., USD): \").upper()\n",
        "            target_currency = input(\"Enter target currency (e.g., EUR): \").upper()\n",
        "            amount = float(input(\"Enter amount to convert: \"))\n",
        "\n",
        "            converted_amount = convert_currency(amount, source_currency, target_currency)\n",
        "            if converted_amount is not None:\n",
        "                print(f\"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}\")\n",
        "        except ValueError:\n",
        "            print(\"Error: Please enter a valid number for the amount.\")\n",
        "        except Exception as e:\n",
        "            print(\"An error occurred:\", e)\n",
        "\n",
        "        choice = input(\"Do you want to convert another currency? (yes/no): \").lower()\n",
        "        if choice != 'yes':\n",
        "            print(\"Exiting...\")\n",
        "            break\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()"
      ]
    }
  ]
}