import os
import time

dollar_art ="""
   ||====================================================================||
   ||//$. /\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\//$. ||
   ||(1000)===============|octucode for programming|===============(1000)||
   ||. $//        ~         '------========--------'                  $//||
   ||<< /        /$\\              //|____|                           \\ >>||
   ||>>|  12    //L.             // ///$$)            L38036133B   12 |<<||
   ||<<|           //           || <||  >\\  ||                        |>>||
   ||>>|         \\$/            ||  $$ \\//  ||       One Thousand     |<<||
||====================================================================||>||
||//$. /\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\//$. ||<||
||(100)===============|octucode for programming|=================(100)||>||
||. $//        ~         '------========--------'                   $//||\\||
||<< /        /$\\              // \\|||      حراف امانة                 >>||)||
||>>|  12    //L.             // ///..)    /       L38036133B   12 |<<||/||
||<<|           //           || <||  >\\   /                        |>>||=||
||>>|         \\$/            ||  $$ --/  /||       One Hundred     |<<||
||<<|      L38036133B        *    |\\_/  //* series                 |>>||
||>>|  12                     *. /___\\_//*   1989                  |<<||
||<<\\      Treasurer     ______/AL-HERSH\\________     Secretary 12 />>||
||//$\\                 ~|UNITED STATES OF AL-RABAT|~              /$. ||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||. $//\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\. $//||
||====================================================================||
"""

currency_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'EGP': 30.9,
    'RMP': 6.5
}

def clear_screen():
    os.system('cls' if os.name == "nt" else "clear")
    print(dollar_art)

def calculate_exchange(amount, from_currency):
    while True:
        to_currency = input('Enter the currency you want to convert to: ').upper()
        if to_currency not in currency_rates:
            print(f"Sorry, but '{to_currency}' is not in the currency schedule.")
            continue
        else:
            rate = currency_rates[to_currency] / currency_rates[from_currency]
            return to_currency, rate

def start():
    while True:
        clear_screen()
        print("Welcome to the Currency Converter!")
        chosen_currency = input("Choose a currency (e.g. USD, EUR, EGP, RMP): ").upper()
        if chosen_currency not in currency_rates:
            print(f"Sorry, '{chosen_currency}' is not supported.")
            time.sleep(2)
            continue
        try:
            amount = float(input('Enter the amount you want to convert: '))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            time.sleep(2)
            continue
        confirm = input(f"Do you confirm to convert {amount} {chosen_currency}? (y/n): ").lower()
        if confirm != 'y':
            continue
        clear_screen()
        to_currency, rate = calculate_exchange(amount, chosen_currency)
        print("Analyzing your request...")
        time.sleep(2)
        print(f"Preparing the deal from {chosen_currency} to {to_currency}... please wait")
        time.sleep(2)
        print(f"Checking for the best available rate for {to_currency}... please wait")
        time.sleep(2)
        print(f"Exchange Rate: 1 {chosen_currency} = {rate:.4f} {to_currency}")
        final_amount = amount * rate
        print(f"\n{amount} {chosen_currency} is equal to {round(final_amount, 2)} {to_currency}")
        time.sleep(5)
        break

if __name__ == "__main__":
    start()
