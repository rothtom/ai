I started with a neural network very simillar to the one from the lecture and already got kinda good results.
Then i tried increasing the maxpooling area as i thought that the colors might be a pretty good info that may substitute for the exact palcement of the colours.
    That tourned out to be a great dissappontment. So i changed it back to a 2x2 area.

I then tried increasing the neurons in the first hidden layer, which only made it worse, so i added a second hidden layer.

I then increased the number of neurons per layer drastically (from 256 to 1024) on the first and from 96 to 256 on the second layer.
    This really improved the accuracy but also the cost.
