# Custom Invite Auto-Role Guide
###### Note: sometimes, the bot fails to add roles if a large influx of people joins at one time. In the case of classes where many students join at once you may have to go back and verify that all members who are not TAs or SAs have the `@student` role

## Step-By-Step Guide
1. Add the `BetterInvites` Discord bot to your server
    1. [Invite `BetterInvites` Bot](https://discord.com/oauth2/authorize?client_id=1076936873106231447&permissions=1101927548960&scope=bot%20applications.commands)
2. Generate multiple invites - you will need one invite per group.
    1. Example: 
        1. Group 1: Students (one invite link)
        2. Group 2: TAs (diferent invite link)
      
    2. You can create multiple distinct invite links by hitting the `create invite button` on the side of diferent text channels
3. Run the command: `/createinvite` this will prompt you to select one of the many invite links you've created. Select a link that has not yet been selected by the bot and assign roles for a group. Now send this link to members of that group.
    1. Example:
        1. Group 1: Students (Link: `https://discord.gg/abcdefg`) (roles: `@student`, `@member`)
        2. Group 2: TAs (Link: `https://discord.gg/12345`) (roles: `@Teaching Staff`, `@TA`, `@member`)
    2. Now send the link `https://discord.gg/abcdefg` to students and the link `https://discord.gg/12345` to TAs
4. Varify that the roles are assigned correctly by running `/display`. Note the response is only visable to you.


<br>

<br>

## Documentation
[thymedev documentation link](https://thymedev.github.io/docs/betterinvites/#invite-me)
