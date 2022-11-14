guesses = ["Red"]
hats = ["Blue", "Blue"]

def guess_color(guesses, hats):
    total = (hats + guesses)
    if total.count("Blue") % 2 == 0:
        print("Blue")
        
guess_color(guesses, hats)
