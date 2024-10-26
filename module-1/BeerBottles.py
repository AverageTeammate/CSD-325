# Jacob Cannamela
# CSD325
# 10/26/2024

# Create the function to handle counting the bottles and display the song text
def bottles_of_beer_song(bottles):
    # Countdown loop
    while bottles > 0:
        # Print current bottle lyrics
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        else:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
        
        # Take one down and pass it around
        bottles -= 1
        
        # Print remaining bottle(s) of beer
        if bottles > 1:
            print(f"Take one down and pass it around, {bottles} bottles of beer on the wall.\n")
        elif bottles == 1:
            print("Take one down and pass it around, 1 bottle of beer on the wall.\n")
        else:
            print("Take one down and pass it around, 0 bottles of beer on the wall.\n")

    # End of song reminder
    print("Time to buy more bottles of beer")

# Main program
try:
    num_bottles = int(input("Enter the number of bottles: "))

    # Pass the user input into the bottles_of_beer_song function
    bottles_of_beer_song(num_bottles)
    
except ValueError:
    print("Please enter a valid number.")
