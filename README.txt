This variables will let you change the form of the tree:
rdt_factor_angle1, rdt_factor_angle2, rdt_factor_branch1, rdt_factor_branch2.

They are equals to 1/2 by defect, but I recommend change rdt_factor_branch1 and rdt_factor_branch2 to random.uniform(0.8, 0.9) and play with it :)

Important: 
    -If you use a very small reduction factor (like random.uniform()), you should change the min_branch_lenght to a bigger number.
    -Take care with the inicial branch´s lenght too

The colors are selected randomly
