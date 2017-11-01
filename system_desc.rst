Based on the system
===================

- Introduction to Calculus, Paul Lutus
- http://arachnoid.com

Car Example
-----------
The key idea of calculus, on which the entire eld stands, is the relationship between a quantity and a rate of change in that quantity. 
For example, we might want to describe the position of a moving car as time passes:

- The car's acceleration, controlled by the accelerator pedal, is a rate of change in the car's velocity.
- The car's velocity, recorded by the speedometer, is a rate of change in the car's position.
- Expressed in everyday language, position is \where you are", velocity is \how fast you're moving", and acceleration represents \how velocity is changing."
- These three quantities { position, velocity and acceleration { are bound together in such a way that, with the methods of calculus, we can use any one of them to nd the other two.
- For example, we can note a car's speedometer (velocity) readings over time and use that to reconstruct the car's position, without any other information.


Equations
---------

key equation - p(t) = 1/2 * at^2

in Diff form p'(t) = ( p(t + Delta t) - p(t) ) / (Delta t)

Having assigned variable names for each of the data table's columns, we can write equations that describe and predict the table's numerical values:

- In the data table on page 4, acceleration is the same for any time argument { this is called a constant10, an unchanging value. Its very simple equation is:
1. a = 4 

- By examining the table's velocity values, readers may be able to guess the corresponding equation { it appears to be the acceleration constant times time, or:
2. v = at 

- The position equation's form isn't self-evident, but we'll add it to this list while promising to provide a denition below. It is:
3. p = 1/2 * at^2 

Here are some facts about these equations:

- Just like the numerical quantities described earlier, any of the equations in the above list can be obtained from the others.
- Moving up the list from position to acceleration, each equation is said to be the derivative with respect to time of the equation below it.
- Moving down the list from acceleration to position, each equation is said to be the integral with respect to time of the equation above it.
- When expressed in technical language, velocity is the time integral of acceleration, and position is the time integral of velocity.
- When expressed in everyday language, the velocity at time t is the sum of all prior accelerations, and the position at time t is the sum of all prior velocities.

- As before and consistent with the Fundamental Theorem of calculus5 introduced earlier, if we take the derivative 
of an equation and then integrate the derivative, we get back what we started with.
The calculus idea from the prior section { that all the numerical quantities can be acquired from any one of them
{ applies to equations as well: using the methods of calculus, we can acquire all the above equations from any one of them:

- Provided only with the position equation, we can dierentiate to acquire velocity and acceleration.
- Provided only with the acceleration equation, we can integrate to acquire velocity and position. But to do this, we need to understand functions.


