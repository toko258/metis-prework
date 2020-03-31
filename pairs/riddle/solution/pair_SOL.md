**Problem 1:**

Three wise men are told to stand in a straight line, one in front of the other. A hat is put on each of their heads. They are told that each of these hats was selected from a group of five hats: two black hats and three white hats. The first man, standing at the front of the line, can’t see either of the men behind him or their hats. The second man, in the middle, can see only the first man and his hat. The last man, at the rear, can see both other men and their hats.

None of the men can see the hat on his own head. They are asked to deduce its color. Some time goes by as the wise men ponder the puzzle in silence. Finally the first one, at the front of the line, makes an announcement: “My hat is white.”

He is correct. How did he come to this conclusion?

>[Answers in comments here.](https://tierneylab.blogs.nytimes.com/2009/03/16/the-puzzle-of-the-3-hats/)

**Problem 2:**

A man lives on the 14th floor of an apartment. Every morning, when he goes to work, he gets on the elevator at the 14th floor and goes down to the lobby. In the evening, if he is on his own, he takes the elevator from the lobby to the 8th floor and then walks up 6 flights. But if there are other people, or if it's a rainy day, he goes straight to the 14th floor. Why does he do that?

> He's short and uses an umbrella to hit higher buttons than level 8

**Problem 3:**

Can you draw [this pattern](square.gif) without taking your hand off the paper? If so, how? If no, why not?

> No, due to more odd than even nodes; we are assuming no tracing.

**Problem 4:**

Three kids visit their grandmother. The first kid sees a jar of candy. She counts the candy and makes three equal piles. There is one extra. So she eats the extra candy and also her share. And returns the rest to the jar. The second walks by the candy jar. Not knowing one of his cousins has gone through it, he too makes three equal piles, and there is one extra. He eats the extra one and his presumed share. Of the remaining candy, the third cousin does the same (again there is one extra, which is eaten along with a third). Later in the evening, the grandmother calls the three kids and takes out the candy jar. What's in the jar gets evenly split between the three. And this time it's perfect! How many candies were originally in the bottle?

Think recursion!

> There are four layers in our system of equations, so we should start at the end and work backwards:

- 3e = 2d
- 3d + 1= 2c
- 3c + 1 = 2b
- 3b + 1 = 2a

>Then solve for 3a to determine the original candy amount. We can note that only even values for `e` provide `int` values for `d`. This check can be coded in Python to allow solution checks using for loops.