/*********** Dataset informations ***********/ 

name : Skillcraft
Abstract: This data was used in Thompson et al. (2013). 
	  A list of possible game actions is discussed in Thompson,
	  Blair, Chen, & Henrey (2013) 
they aggregated screen movements into screen-fixations using a Salvucci & Goldberg (2000) dispersion-threshold algorithm, 
and defined Perception Action Cycles (PACs) as fixations with at least one action.

1. GameID: Unique ID number for each game (integer)
2. LeagueIndex: Bronze, Silver, Gold, Platinum, Diamond, Master, GrandMaster, and Professional leagues coded 1-8 (Ordinal)
3. Age: Age of each player (integer)
4. HoursPerWeek: Reported hours spent playing per week (integer)
5. TotalHours: Reported total hours spent playing (integer)
6. APM: Action per minute (continuous)
7. SelectByHotkeys: Number of unit or building selections made using hotkeys per timestamp (continuous)
8. AssignToHotkeys: Number of units or buildings assigned to hotkeys per timestamp (continuous)
9. UniqueHotkeys: Number of unique hotkeys used per timestamp (continuous)
10. MinimapAttacks: Number of attack actions on minimap per timestamp (continuous)
11. MinimapRightClicks: number of right-clicks on minimap per timestamp (continuous)
12. NumberOfPACs: Number of PACs per timestamp (continuous)
13. GapBetweenPACs: Mean duration in milliseconds between PACs (continuous)
14. ActionLatency: Mean latency from the onset of a PACs to their first action in milliseconds (continuous)
15. ActionsInPAC: Mean number of actions within each PAC (continuous)
16. TotalMapExplored: The number of 24x24 game coordinate grids viewed by the player per timestamp (continuous)
17. WorkersMade: Number of SCVs, drones, and probes trained per timestamp (continuous)
18. UniqueUnitsMade: Unique unites made per timestamp (continuous)
19. ComplexUnitsMade: Number of ghosts, infestors, and high templars trained per timestamp (continuous)
20. ComplexAbilitiesUsed: Abilities requiring specific targeting instructions used per timestamp (continuous)

/*********** Overview ************/

In a game called starcraft , there is a relation between the screen movement when a person plays the game 
and the league class which is the level that got into .

/*********** Problem *************/

in this project we tried to find the best model 
to predict the leagueindex 

/********** TASKS ***********/

After careful consideration, we decided to choose LeagueIndex as a Variable target. So the objective is to predict rank based on all of that data.
After selecting the Variable target, we performed a data cleaning because we found that in the Age, HoursPerWeek and TotalHours variables
There was corrupted data. So we fixed that and did the data exploration where we compared each of the variables with the target variable.
This led us to reject some variables that we felt were unnecessary for precision.
In the end, we threw out these variables:
1. GameID
2. Age
3. HoursPerWeek
4. TotalHours
5. ActionInPAC
6. UniqueUnitsMade
7. ComplexUnitsMade
8. ComplexAbilitiesUsed

Then we proceeded to normalize the data also called scalling and we chose normalized between 0 and 1 because some algorithms did not want to work with the standardScaller
The normalization of the data allowed us subsequently to be able to apply the machine learning algorithms:
1. Logistic regression
2. Naive Bayes
3. Random Forest
4. KNN

/********** CONCLUSIONS *********/

After applying these algorithms we noticed that the models were underfitted , and the scores 
were arround the 0.4 which is a very low score.
We were able to give as a conclusion that although there were more than 3000 lines of data it seems that it's not enough to get a good accuracy.
The curve from the learning_curve function demonstrates this well since we can see that the train curve and the validation curve do not cross each other which means that the model
is still able to learn again and so the score could improve.
So from our perspective we could recommend to merge the classes that have very low distribution of data with those who are near them so the data remain coherent