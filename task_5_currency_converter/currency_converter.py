import requests


API_URL = "https://api.frankfurter.dev/v1/latest"
TIMEOUT = 10


def get_exchange_rate(source_currency, target_currency):
    """Retrieve an exchange rate from the Frankfurter API."""
    if source_currency == target_currency:
        return 1.0, None

    try:
        response = requests.get(
            API_URL,
            params={"from": source_currency, "to": target_currency},
            timeout=TIMEOUT,
        )

        if response.status_code == 404:
            print("Invalid or unsupported currency code.")
            return None, None

        response.raise_for_status()
        data = response.json()
        rate = data.get("rates", {}).get(target_currency)

        if rate is None:
            print("The API did not return a rate for the selected currencies.")
            return None, None

        return float(rate), data.get("date")

    except requests.exceptions.RequestException as error:
        print(f"Unable to retrieve the exchange rate: {error}")
    except (ValueError, TypeError):
        print("The API returned invalid data.")

    return None, None


def is_valid_code(currency_code):
    """Check that a currency code contains exactly three letters."""
    return len(currency_code) == 3 and currency_code.isalpha()


def main():
    print("===== CURRENCY CONVERTER =====")

    amount_input = input("Enter the amount to convert: ").strip()

    try:
        amount = float(amount_input)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    source_currency = input("Enter the source currency code (for example, USD): ").strip().upper()
    target_currency = input("Enter the target currency code (for example, INR): ").strip().upper()

    if not is_valid_code(source_currency) or not is_valid_code(target_currency):
        print("Invalid currency code. Please enter a three-letter code.")
        return

    rate, rate_date = get_exchange_rate(source_currency, target_currency)
    if rate is None:
        return

    converted_amount = amount * rate

    print("\nConversion result:")
    print(f"Exchange rate: 1 {source_currency} = {rate:.4f} {target_currency}")
    print(f"{amount:.2f} {source_currency} = {converted_amount:.2f} {target_currency}")

    if rate_date:
        print(f"Rate date: {rate_date}")


if __name__ == "__main__":
    main()
