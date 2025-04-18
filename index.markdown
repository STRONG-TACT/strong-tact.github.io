---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
thumbnail: "/files/welcome.png"
---

<p align="center">
<img src = "/files/welcome.png"></p>


> 📢 News! <br>
> Jan 31 --- We are hosting the 2nd iteration of Dice Adventure Competition at Conference on Games 2025! \\
> Join us on [Slack](https://join.slack.com/t/dice-adventure/shared_invite/zt-2ia9cgtkn-VAKxgzLBYlS9tzKWmE8ePA) channel for most up-to-date information. \\
> ~~Jan 19 --- We are preparing for the Dice Adventure Competition 2025, stay tuned!~~ \\
<!-- > ~~Daily virtual match making session available at **8am - 10am EST, 12pm-2pm EST, 8pm - 10pm EST** from **July 16, 2024** to **July 27, 2024**. [Sign up](https://gatech.co1.qualtrics.com/jfe/form/SV_bqqsRdimotXh8nI) to [compete](https://cmu-tact.itch.io/dice-adventure)!~~ \\
> ~~June 25 --- Agent submission deadline has been extended to July 7.~~ \\
> ~~May 8 --- Dice Adventure is online! See [Game](/game) for more details.~~ \\
> ~~May 1 --- The agent submission portal is open! See [Submission](submission.markdown) for details.~~ -->


|[Submit an Agent](/submission/) 🤖       |[Play the Game](/play/) 🌐         |
|----------------------|---------------------|----------------------|
|Design, develop and train AI agents that can play the game.                |Play the game online at multiple virtual match-making event.                 |



* TOC
{:toc}



Welcome to the second Dice Adventure Human-AI Teaming Competition! We ran the first iteration of the competition in 2024 as one of the game-AI competitions hosted at 2024 [Conference on Games](https://2024.ieee-cog.org/) and we are returning this year. In this competition, we are using an in-house developed game called Dice Adventure as the environment and encourage participants to explore human-AI teaming effects. Dice Adventure is a multi-player turn-based dungeon crawling game that takes three players to play. Detailed information on game rules, game tutorial and frequently asked questions can be found at [Game](game.markdown) page.

We offer two tracks and welcome participantas at all levels. To participate, you must sign up for one or both track(s). If you are interested in developing an agent, please check out the guidelines in [Submit AI](submission.markdown) page for *agent development track*. The starter code and training environment can be accessed at the [Dice-Adventure-Agents](https://github.com/STRONG-TACT/Dice-Adventure-Agents) repo on GitHub. If you do not wish to submit an agent but are still interested in this competition, please check out the details on the [Play](/play/) page for signing up as a player in the *player track*. We will be hosting a few virtual and in-person matchmaking events to bring players together.

<!-- As part of the match-making events, we will be hosting an in-person hackathon event at Georgia Institute of Technology in Atlanta, GA in the United States. The hackathon is a free event that welcomes students, researchers, developers and anyone interested in our game and competition to get together. We will be organizing a series of tutorial sessions, interactive demos, working sessions and game tournaments during the two-day event. RSVP information, event schedule and accommodation suggestions can be found at the [Hackathon](/hackathon/) page. -->

The following video provides an overview to the competition tracks, rules, short game tutorial and information on setting up the training environment. We hope to bring exciting experiences to the participants and exploring critical human-AI teaming questions to gain a better understanding in team communication, coordination, and adaptation.

<iframe width="640" height="360" src="https://www.youtube.com/embed/cvV_hTAYgy4?si=qu2tJ5bUwP8vhw-x" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<!-- [![Watch the video](/files/timeline.png)](https://www.youtube.com/watch?v=cvV_hTAYgy4) -->
<!-- https://www.dropbox.com/request/5Fnu21FIHgVk9pnTmxId -->


## Key Dates

| Key Dates<br/>All deadlines are 11:59pm UTC-12:00 (anywhere on Earth) |                     |
|---------------------------------------------------|---------------------|
|~~Release competition tracks and rules~~               |~~January 1, 2025~~         |
|~~Release evaluation criteria~~                        |~~January 1, 2025~~         |
|~~Release leaderboard design~~                         |~~January 1, 2025~~         |
|~~Release game tutorial~~                              |~~January 15, 2025~~        |
|~~Release game play demo videos~~                      |~~Januray 15, 2025~~        |
|~~Release training environment set up tutorial~~       |~~January 15, 2025~~        |
|Release a local build of the game                  |March 1, 2025       |
|Release the Unity project for the game             |March 1, 2025       |
|Release agent submission template                  |March 1, 2025       |
|Relase competition registration links              |March 1, 2025       |
|Agent submission portal opens                      |March 1, 2025       |
|Agent submission portal closes                     |May 31, 2025        |
|CoG auxiliary paper deadline                       |June 1, 2025        |
|Online matchmaking portal opens                    |June 1, 2025        |
|Online matchmaking portal closes                   |June 30, 2025       |
|Release competition results                        |July 31, 2025       |
|Winners announced on the website                   |July 31, 2025       |
|Release competition report                         |August 20, 2025     |
|Conference on Games                                |August 26-29, 2025  |


## Evaluation Criteria

As the goal of the competition is to better understand human-AI teaming dynamics, the submitted agents will not be evaluated by running against benchmarks or through bot fight. All the agents will be selected at least once and play with players in the player track as a team. Below are the scoring function showing how a team score is calculated. The score consists of a base score with a decaying factor and bonuses for each character. For each level, each character gets a bonous of 10 and they lose the bonus proportional to losing the health. If a character lose all the health in a level, it will not be eligible for the bonus.

<img src="https://latex.codecogs.com/svg.latex?\Large&space;S_i = 100 \times d^{r_i} + \sum_{j=1}^{3} \frac{h_{ij}}{h\_max_{ij}} \times rs_{ij} \times 10" title="\Large S_i = 100 \times d^{r_i} + \sum_{j=1}^{3} \frac{h_{ij}}{h\_max_{ij}} \times rs_{ij} \times 10"/>

<img src="https://latex.codecogs.com/svg.latex?\Large&space;team\_score = \sum_{i=1}^{n}S_i" title="\Large team\_score = \sum_{i=1}^{n}S_i"/>

- d: decaying factor, we are using d=0.95 for competitions
- i: the current level the team is at
- j=(1, 2, 3) representing each of the three characters
- r: the number of rounds the team took to clear a level
- rs: if a character lose all lives (rs=0) in a level 
- h: the health a character remains
- h_max: the maximum health a character has
- n: the total number of levels the team has cleard


## Prizes

Details will be released soon.

<!-- Our competition is sponsored by the IEEE Computational Intelligence Society Education Competition Fund with a total cash prize of **$1,000 USD**, which will be awarded to participating teams ranking at the top three places on the [leaderboard](leaderboard.markdown). The prize will be equally distributed among team members --- human players and agent developers of agents. Below is the distribution of prizes:

🥇 1st place - $500 USD<br>
🥈 2nd place - $300 USD<br>
🥉 3rd place - $200 USD<br> -->


## Form and Links

Registration link and agent submission link will be released in March, 2025.

<!-- Player track signup form: [https://gatech.co1.qualtrics.com/jfe/form/SV_bqqsRdimotXh8nI
](https://gatech.co1.qualtrics.com/jfe/form/SV_bqqsRdimotXh8nI
)\\
~~Hackathon signup form:[https://gatech.co1.qualtrics.com/jfe/form/SV_cBkazbWRdGRW9y6](https://gatech.co1.qualtrics.com/jfe/form/SV_cBkazbWRdGRW9y6)~~ \\
~~Agent submission form: [https://gatech.co1.qualtrics.com/jfe/form/SV_6Qd51ZHWarDyzu6](https://gatech.co1.qualtrics.com/jfe/form/SV_6Qd51ZHWarDyzu6)~~ \\
~~Agent file submission link: [https://www.dropbox.com/request/5Fnu21FIHgVk9pnTmxId](https://www.dropbox.com/request/5Fnu21FIHgVk9pnTmxId)~~ -->


## Related Publications

## Organizers
Qiao Zhang, [qzhang490@gatech.edu](qzhang490@gatech.edu) \\
Glen Smith, [glensmith@gatech.edu](glensmith@gatech.edu) \\
Varun Girdhar, [vgirdhar@andrew.cmu.edu](vgirdhar@andrew.cmu.edu) \\
Ziyu Li, [ziyul@andrew.cmu.edu](ziyul@andrew.cmu.edu) \\
Avery Gong, [xgong80@gatech.edu](xgong80@gatech.edu) \\
Shreyas Ravishanker, [sravishanker3@gatech.edu](sravishanker3@gatech.edu) \\
Erik Harpstead, [harpstead@cmu.edu](harpstead@cmu.edu) \\
Christopher J. MacLellan, [cmaclellan3@gatech.edu](cmaclellan3@gatech.edu)

Last updated on January 19, 2025.

<!-- Dice Adventure is a multi-player, turn-based, dungeon crawling adventure game developed at Carnegie Mellon University. This is the first time for us to host the Dice Adventure Human-AI teaming competition. There are two tracks of the competition - (1) participants can submit their agents to the agent track;  (2) participants can play with other players and submitted agents in the player track. Agents submitted to the agent track will play with players in the player track and be evaluated on the team score they achieved after running multiple levels of games. Winners will be declared based on overall teaming performance. We hope to bring exciting experiences to the participants as well as exploring critical human-AI teaming questions and gain a better understanding in team communication, coordination and adaptation. An introduction of the competition can be found in [this video](https://www.youtube.com/watch?v=cvV_hTAYgy4). -->
