# Step 1: Welcome the User
print("Hello User, Welcome to FIFO")

# Step 2: Use a loop to ask question until the user says yes
while True:
     # Step 3: Ask user a question and get the answer
     response = input("Have you eaten? (yes or no): ").lower()

     # Step 4: Check the response
     if response == "yes":

          # Step 5: If the answer is yes, we commend them.
          print("That’s good remember to stay hydrated")
          break # End the loop

     elif response == "no":

          # Step 6: If the answer is No, ask the to Go and Eat Something. Health First, then come back
          print("Go and Eat Something. Health First.. Try Again!")
     else:
          #Step 7: Catching Unexpected Answers
          print("Why are you too stubborn? yes or no")

# Step 8: Thank user for using our app
print("Thanks for checking in. Goodbye!_ FIFO Team")

#Thanks for coming