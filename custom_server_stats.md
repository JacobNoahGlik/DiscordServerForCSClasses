# Custom Server Stats
###### Using the `Server Stats` Discord Bot

## Basics
Running `/setup channel:voice channel (recommended) template:Default counters` will result in a counter of All members (`Users` + `Bots`), Members (`Users`), and Bots (`Bots`)

![image](https://github.com/user-attachments/assets/7fe6a21c-6333-454f-8ebb-0cb8db3a691e)

![image](https://github.com/user-attachments/assets/1ade3201-11e5-44d3-8f70-fae576627c78)

## Edit The Counters
You can edit the channel's name to anything as long as the number is in the name and there are no other numbers.

![image](https://github.com/user-attachments/assets/20640e7b-0471-43ec-b7a2-384366f00059)


## Configure For Classes
The most important counters should count the number of staff members and students. You can achieve this by creating a custom counter for `members with certain roles` using the roles `@student` and `@Teaching Staff`. You can also create four counters instead of two, counting the number of Students, SAs, TAs, and Professors.

![image](https://github.com/user-attachments/assets/ea1abfe1-857d-4bf3-84f3-992a81aafd5c)

* Run `/counter create counter:members with certain roles channel:voice channel (recommended) additional:@Student`
* Run `/counter create counter:members with certain roles channel:voice channel (recommended) additional:@SA`
* Run `/counter create counter:members with certain roles channel:voice channel (recommended) additional:@TA`
* Run `/counter create counter:members with certain roles channel:voice channel (recommended) additional:@Professor`

![image](https://github.com/user-attachments/assets/075e75e5-b37c-458c-8222-283e1ff94144)

Change the names of the voice channels to the name you prefer and feel free to change the order too.

