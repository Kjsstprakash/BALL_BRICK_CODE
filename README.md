# BALL_BRICK_CODE
CODE FOR ZOHO QUESTION
============================================================= ***BALL_BRICK*** ================================================================
This code is related to the Ball_Brick.Before going to the coding part , We should know the TERMS & Conditions as well as Passing Input details. Below instructions kept in mind while executing the program.
1 ) G  -  Ground Level
 2 ) W  -  Wall
 3 ) O  -  Ball
 4 ) _  -  Safe Plate
 5) DE -  Which clears the entire row elements when ball was hit to DE
 6) DS -  Which clears the surrounding elements one step of it when ball was hit to DS
 7) B  -  Which makes the Ground Level(G) as Safe plate when ball was hit B.(Making Safe plate gives first priority to Right of the ball then Left of ofthe ball then Right then Left and so on)
 8 ) LD - Which clear the Left Diagonal element if no brick is there it keep on going left diagonal side. When it was hit the Wall then it moves horizantally and clears the brick.If the respected column groun level of the broken brick is Safe Plate( _ ), Ball Count is not reduced otherwise reduced.
 9 ) RD -  Which clear the Right Diagonal element if no brick is there it keep on going Right diagonal side. When it was hit the Wall then it moves horizantally and clears the brick.If the respected column groun level of the broken brick is Safe Plate( _ ), Ball Count is not reduced otherwise reduced.
 10 ) ST -  Which clear the Straight element if no brick is there it keep on going straight Way. Ball Count does not change in any case.
   If ball count is zero , all bricks are not cleared and cleared we got GAME OVER and HURRAY respectively. 
Finally if all the bricks are cleard then we got the HURRAY.

SIMPLE EXAMPLE OF THE BALL_BRICK CODE MAY HELP TO EASY UNDERSTAND
```Enter N x N Matrix: 7
Enter the brick's position and the brick type: 1 2 1
Do you want to continue Y/N: Y
Enter the brick's position and the brick type: 1 3 DE
Do you want to continue Y/N: Y
Enter the brick's position and the brick type: 1 4 1
Do you want to continue Y/N: Y
Enter the brick's position and the brick type: 2 2 1
Do you want to continue Y/N: Y
Enter the brick's position and the brick type: 2 3 1
Do you want to continue Y/N: Y
Enter the brick's position and the brick type: 2 4 1
Do you want to continue Y/N: Y
Enter the brick's position and the brick type: 3 2 1
Do you want to continue Y/N: Y
Enter the brick's position and the brick type: 3 3 DS
Do you want to continue Y/N: Y
Enter the brick's position and the brick type: 3 4 1
Do you want to continue Y/N: N
Enter The Ball Count: 3
W W W W W W W
W   1 DE 1   W
W   1 1 1   W
W   1 DS 1   W
W           W
W           W
W G G O G G W
Ball Count 3
Enter the Direction: ST
W W W W W W W
W   1 DE 1   W
W           W
W           W
W           W
W           W
W G G O G G W
Ball count 3
Enter the Direction: ST
W W W W W W W
W           W
W           W
W           W
W           W
W           W
W G G O G G W
 === * HURRAY * ===
