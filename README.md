# Brick_Out_Simple_Clone
This is a simple clone of the famous game BrickOut 
it is built with python's pygame library 

# Game Description
* The main screen was actually a mistake i made but i saw that it would be great to be used as a main screen menu
* The bricks are actually a 2D array of pygame rects that once collided with the ball they are deleted out of the array
* The bar took me a good time to figure out how to make each portion of it reflects the ball into the desired and logical direction
  ### For Example :
  * The ball bounces in the right direction if it fell on the right portion of the bar
  * The ball bounces in the left direction if it fell on the left portion of the bar
  * The ball bounces horizontally if it fell on the middle portion of the bar
  ## Gifts and Curses
  * These things falls randomly in different places , they are like rewards and penalties
  ### More Explanation
  * if the bar managed to collide with this ![](giftbox.png) which is the gift in our game
  the ball will be invincible for 5 seconds which means it will not bounces back when it hits a brick
  * if the bar managed to collide with this ![](curse.png) which is the curse in our game
  the bar would flash on and off for 5 seconds and directions are reversed (right would be left and left would be right)
  
# Video
here is a video of me playing the game





https://user-images.githubusercontent.com/97110015/230616415-4c6a24c5-1cfe-474c-bf70-ecfb1b49172b.mp4





# Installation
if you would like to try it feel free to install this exe from [here](https://github.com/YUSUF-SELEIM/Brick_Out_Simple_Clone/blob/main/Brick_Out_Simple_Clone.exe)