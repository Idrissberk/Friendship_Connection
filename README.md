## Friendship Connections

#### ** Prepared Dataset **
  The dataset consists of 'friend pairs' from Facebook. Facebook data was collected from survey participants using the Facebook app. For privacy issues, Facebook data 
has been anonymized by replacing the Facebook-internal IDs with new dummy values.

  In each line of the file containing this dataset, there are two integer values. Here, each integer value represents the IDs of the users.
  
  Facebook has an undirected relationship format which means that when you become a friend of a user, then this user also becomes your friend as well. For instance, if 
you see the line given below in the file, it means that the user with ID 10 is a friend of the user with ID 158, and it also means that the user with ID 158 is a friend of the user with ID 10.

#### ** Input / Output **
  My program will prompt for a single input, which is an integer that corresponds to the ID of the user, to whom the friend suggestion will be made. You may assume that this input is really an integer, i.e. it consists only of digits. If this user does not exist in our dataset, i.e. the input user ID does not appear in the prepared dataset file, then your program will prompt “There is no such user”. Otherwise, your program will suggest the most frequent user(s) among the friends of the friends of the input user. In other words, it will suggest the most frequent user among the 2nd degree connections of the input user.
