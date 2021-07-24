#"""
#Foundation-
#Create an app that helps people out in the world:

#- The app helps you determine or gives you
#options if you need to go see a doctor
#depending on how your feeling.

#-
#With this app more people are able to get more
#health professional advice or tips.
#Also the doctors get benefits from this app, since they are able
#to determine if patient needs help or they just need a
#pharmachy medication.

#Elevator pitch:
#Our group is (Kevin, and Walter). We created this product (healthcare advice) for (people),
#to (help determine if they need a doctor or give advice of what they should do instead).
#It is unlike (other apps that only give you advice of what to do and do not give you
#a diognostic.) because (our apps give you specific diognostic of you're symptoms and provides
#proffessional advice.
#this app helps you determine any medical issues no matter where
#you are in the world and provides solutions to treat the issue).
#We are passionate about this because(we believe this will unlock ways in which people
#don't have to go see a doctor but instead be provided a solution right away if it is a
#minor isssue). For the future,we would like to develop a new feature that's able to do a
#doctors job anywhere you go.

#Core :
#1. opening question-
#input: Basic question - "Are you seeking serious medical attention?"

opening_question = input("Are you seeking serious medical attention? \n")

if opening_question == "yes":
    print("Please call 911!!!")
elif opening_question == "no":
  print("Please choose one of the reasons for this interaction: ")
  print("headaches", "pains", "broken bones", "sprains", "cold", "flu", "stomachache", "burns", "fainting","depression", "feeling down")

  user_response = input("what is your interaction?")
  print("youre interaction is: " + user_response)

 
  if user_response == "headaches":
      headache_input = input(
        "How would you describe the pain; mild, severe, worst pain ever? \n"
        )

      if headache_input == "mild":
        print(
              'We would recommned you to get some rest and try to stay of the electornic device to let the headache calm down.'
              )
      elif headache_input == "severe":
          print("We would recommend for you to go see a doctor")
      elif headache_input== "worst pain ever":
          print(
                  "We would like for you to go to the hosipital and seek medical professional advice emmidietly!!!"
              )

  if user_response == "pains" or user_response == "broken bones":
      print(
            "Please seek professional medical help at a hospital or call 911 right away!!!"
            )

  if user_response == 'sprains':
      sprains_input = input("On a scale of 1 - 10, how bad is the sprain. \n")

      if sprains_input >= 5:
        print("go to the hospital")
      elif sprains_input <= 4:
        print("rest")
      sprains_input = input("Is the sprain swollen or just in pain?")

  if user_response == "cold" or user_response == "flu":

      cold_flu_input = float(input("can you descrive your temperature? \n")) 

      if cold_flu_input <= 98.6:
          print(
                "We would recommend you to drink something hot and try to stay away from cold places and get to somewhere that is warmer"
                      )
      elif cold_flu_input >= 98.6:
          print(
                  "We would like for you to take some cold/flu medicine like Advil or Night/Day Quil, but at the same time we would also like to recommend you go to the emergency room"
                      )

  if user_response == "stomach ache":
      stomache_input = input(
          "On a scale of 1 - 10, how bad is your stomache pain. \n")
      if stomache_input >= "5":
        print(
          "We would advise you to go to the emergency to seek professional help for the pain."
                  )
      elif stomache_input <= "4":
        print(
              "Try to take Over-the-Counter Medications like Pepto Bismol, Gas-X, Gaviscon, Tums, and Rolaids."
              )

  if user_response == "depression" or user_response == "feeling down":
      depre_feeldown_input = input(
          "What is making you feel depressed or feeling down?")
      print(
        "we would recommend you talk to a threapist or you can talk to someone close to you about it and see what is the issue you are facing? "
            )
  if user_response == "fainting":
   print("If you keep fainting you should seek medical attentinon, if it does not, rest, and let someone near you know what happened.")


#2.if/else statements -
#- if say yes, print please call 911 to get your medical attention you need.
# if no, "what is your reason for your interaction?"

#3.list of questions for them to answer -
#- where are you feeling the pain
# scale of 1 - 10 how bad is the pain
#- if not, what issues are you experiencing
#-What are you experiencing any syptoms? please provide the list of symptoms your having...
#- Do you feel like you need a doctor or a surtain type of medication?

#secondary :
#4. Possible solutions -
#if/else statements

possible_solutions = {
    "headaches": "drink water, exercise, relax yourself",
    "pains": "take advil, seek medical attention",
    "broken bones": "need medical attention right away",
    "sprains":
    "option 1. take pain killers or advil. option 2. go to the ER to get an x-ray",
    "cold" : "take Robafen, advil, or tylenol" , "flu": "take NyQuil and DayQuil",
    "fainting": "position yourself on your back and don't get up to quickly, and seek medical attention ",
    "stomachache": "take medication, eat something, rest" ,
    "burns": "Cool the burn, apply lotion, bandage the burn, and seek medical attention please" ,
    "depresion": "talk to someone about it, seek medical attention if worsening",
    "feeling down": "hangout with some friends, talk to someone"
}

user_response = input("Please remind me of what your feeling?, to help provide you with other solutions: ")

if user_response in possible_solutions:
  print(possible_solutions[user_response])



# user_answer = input("input pls")
# if usrinput in possible_solutions:
#   print(possible_solutions[usrinput])


# if opening_question == "yes":
#   print("We would like for you to call 911! ")
 
# elif opening_question == "no":
#   print("Please remind me of what youre feeling?" + "to help provide you with better solution.")



#if
#- experiencing headache: (search solutions online: Drink Water, get some exercises, soothe Pain with a cold compress, get sleep)
#- pain/broken bones: (need emmidiate medical attention)
#- sprains: option 1. take pain killers or advil. option
#2. going to the ER to get an x-ray
#- cold/flu : if not that serious find pharmacy medication like: tylenol,
#list possible medications to help with a cold/flu to take,
#if serious go to the hospital or doctors for professional help.
#- Stomach ache: if not serious take medication, if serious seek professional help
#- take medication, eat something, rest
#- burns : seek medical attention please
#- depresion/feeling down: hangout with some friends, play sport, or seek medical attention

#- else statement: if your not experiencing any of these, please descrive what you're feeling.




#Tertiary: API's
#5. Take them to a nearby hospital-
#if seeking medical attention seek a nearby hospital:
#input: are you trying to seek medical attention at a nearby hospital
#input: what area do you live in?

nearby_hospital = input("would you like to be directed to an available hospital near you? \n")

import googlemaps

gmaps = googlemaps.Client(key = 'PUT_YOUR_API_KEY_HERE')

hospital = input(
    "Hi! It looks like you need medical attention. Is it an emergency? \n")
if hospital == "yes":
    highest_rating = 0
    hospital = ""
    hospital_address = ""
    for place in gmaps.places(query = "hospital",
    type="hospital").get("results"):
        if int(place.get("rating")) > highest_rating:
            hospital = place.get("name")
            hospital_address = place.get("formatted_address")
            highest_rating = place.get("rating")
    print(
        "Here is the name and address of the hospital near you with the highest rating:"
    )
    print(hospital)
    print(hospital_address)
