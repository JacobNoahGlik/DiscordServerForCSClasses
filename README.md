# Create A Discord Server For CS Classes
A description of how to create fun and helpful discord servers for CS classes ( as a TA, professor, or student )

<br>

Fork the [WPI CS Course discord server template](https://discord.new/yqVYn72DAEk5) to auto-create server structure and roles.

<br>

## Recommended Features of an Engaging Discord Server
1. Clear distinction between students and teaching staff
    1. For custom links for individual groups (`Students` VS `TAs` VS `SAs` VS `Professors`), see the [custom invite auto-role guide](https://github.com/JacobNoahGlik/DiscordServerForCSClasses/blob/main/custom_invite_auto-role_guide.md)
2. Reaction roles
    1. For reaction role presets, see the [role assignor folder](https://github.com/JacobNoahGlik/DiscordServerForCSClasses/tree/main/role_assignor)
3. Clear welcome message/rules
4. Get teaching staff attention easily

<br>

## Recommended Text Chats - Overview
###### [More details can be found in the In-Depth Section](#In-Depth-Section---Text-Chat)

###### `INFORMATION`
* welcome-and-rules &nbsp;( students: `react only` )
  * sample `welcome-and-rules` post attached [found in welcome-and-rules.md](welcome-and-rules.md)
* roles &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ( students: `react only` )
  * sample `roles` posts attached [found in roles.md](roles.md)
* announcements &nbsp; &nbsp; &nbsp; ( students: `react only` )
  * sample `announcements` posts attached [found in announcements.md](announcements.md)
* bot-commands &nbsp; &nbsp; &nbsp; &nbsp;( students: `not viewable` )
  * sample `bot-commands` posts attached [found in roles.md](roles.md)


###### `OFFICE HOURS`
* notifications &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;( students: `react only` )
* upcoming-office-hours &nbsp; ( students: `view only` )
* support &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;( ( students: `not viewable` ), ( `@helpRole`: {`view` / `react` / `message`} ) )


###### `TEXT CHANNELS`
* general &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ( students: {`view` / `react` / `message`} )
* homework-help &nbsp; &nbsp; &nbsp; ( students: {`view` / `react` / `message`} )
* notes-resources &nbsp; &nbsp; &nbsp; ( students: {`view` / `react` / `message`} )
* code-spam &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ( students: {`view` / `react` / `message`} )
* off-topic &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ( students: {`view` / `react` / `message`} )
* admin-chatroom &nbsp; &nbsp; &nbsp;( non-admin: `not viewable` )
* TA-Only &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;( students: `not viewable` )

<br>

table:

| Category      | Text Chat                 | Default Permissions           | View | View Exempt Roles         |
|---------------|---------------------------|-------------------------------|------|---------------------------|
| INFORMATION   | welcome-and-rules         | `react only`                  |  ✅  | `@Admin`                  |
| INFORMATION   | roles                     | `react only`                  |  ✅  | `@Admin`                  |
| INFORMATION   | announcements             | `react only`                  |  ✅  | `@Admin`                  |
| INFORMATION   | bot-commands              | `not viewable`                |  ❌  | `@Admin`                  |
| |
| OFFICE HOURS  | notifications             | `react only`                  |  ✅  | `@Admin`                  |
| OFFICE HOURS  | upcoming-office-hours     | `react only`                  |  ✅  | `@Admin`                  |
| OFFICE HOURS  | support                   | `not viewable`                |  ❌  | `@Admin` / `@HELP_NEEDED` |
| |
| TEXT CHANNELS | general                   | `view` / `react` / `message` |  ✅  | `@Admin`                  |
| TEXT CHANNELS | homework-help             | `view` / `react` / `message` |  ✅  | `@Admin`                  |
| TEXT CHANNELS | notes-resources           | `view` / `react` / `message` |  ✅  | `@Admin`                  |
| TEXT CHANNELS | code-spam                 | `view` / `react` / `message` |  ✅  | `@Admin`                  |
| TEXT CHANNELS | off-topic                 | `view` / `react` / `message` |  ✅  | `@Admin`                  |
| TEXT CHANNELS | admin-chatroom            | `not viewable`               |  ❌  | `@Admin`                  |
| TEXT CHANNELS | TA-Only                   | `not viewable`               |  ❌  | `@Admin`                  |

<br>


## Roles
* Vital Roles
  * Professor (Use their name if it's one person, but use "Professor" if it's multiple)
  * TA (Or another name for teaching assistant)
  * Student (Should be auto-applied to anyone who joins the server)
  * Bot (Used to hide the presence of bots in the server)
* Permission Roles
  * Admin (Should give all permissions)
  * Aditional permissions if needed
* Self-Expression Roles
  * Grade roles (Freshmen, Sophomore, Junior, Senior, Grad-Student, etc ...)
  * Prefered Programming Language Role (Java, C/C++, Python, etc ...) - should be funny
  * Major Roles (Comp-Sci, Data Science, IMGD, Robotics, Mech-Eng, Bio-Eng, etc ...)

<br>

## Bots
* [Arcane](https://arcane.bot/) &ensp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;(Used for Leveling)
* [Carl-bot](https://carl.gg/) &ensp; &nbsp; &nbsp; &nbsp; &nbsp;(Used for assigning self-expression roles)
* [ChronicleBot](https://chroniclebot.com/) &ensp; (Used for keeping track of office hours and creating Discored events)
* [ServerStats](https://serverstatsbot.com/) &ensp; &nbsp; &nbsp;(Used to keep track of the population in the server. i.e. number of members)
* [YAGPDB.xyz](https://yagpdb.xyz/) &ensp; &nbsp; (Used to automatically assign the `@Student` role to those that join)
* [TicketsBot](https://ticketsbot.net/) &ensp; &nbsp; &nbsp; (Used to create private tickets to ask TAs questions) [YouTube tutorial](https://www.youtube.com/watch?v=lz3VR4ptqhU)

<br>

## In-Depth - Roles

Role hierarchy: 

1. "bot roles" here (`@YAGPDB.xyz`, `@carl-bot`, `@ServerStats`, `@Arcane`, `@ChronicleBot`, etc)
2. `@Admin`
3. "other permission roles" here if needed (`@allow write anywhere`, `@allow timeout`, `@allow kick`, `@allow ban`, etc)
4. `@Professor` (use prof name if possible)
5. `@TA`
6. "yapp roles" here (more info in the [in-depth section for yapp roles](#Yapp-Roles-In-Depth))
7. `@Student` (should be auto-assigned by bot)
8. `@Bot` (to keep the bots at the bottom of the list on the right)
9. "self-expression roles" here (`@Freshmen`, `@Major::ComputorScience`, `@JavaEnjoyer`, etc)

<br>

## Yapp Roles In-Depth
The goal of yapp roles is to incentivize people to participate in your Discord server. The idea is that the more they interact with others, the higher their points (use a bot to track) and they can level up every `x` points. When they level up a bot assigns them a yapp role. This could change the color of their name and give them a badge to collect. Your goal is to create a good balance of new roles to achieve without taking away from the topic of the Discord server itself.

Yapp roles used in the past: \
Level 1: &ensp;`@Entry Level Yapper 🏅 (Level 1)` (color code: `#3787e9`) \
Level 5: &ensp;`@Yap City 🏙️ (Level 5)` (color code: `#10c9be`) \
Level 10: `@Yap Nobility 🏰 (Level 10)` (color code: `#0cc0a2`) \
Level 15: `@Social Royalty 👑 (Level 15)` (color code: `#05b112`)

These were found to be too difficult to achieve as most students were level 2-4 by the end of the term (7 weeks) and TAs were level 5-9 by the end of the term (7 weeks). With the highest recorded student level being level 6, you should decrease the levels needed to achieve these roles (unless a class lasts longer than 7 weeks).

<br>


<br>


## In-Depth Section - Text-Chat
text


text


text


text
