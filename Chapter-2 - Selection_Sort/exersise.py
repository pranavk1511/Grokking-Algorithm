# 2.1 :  Lots of inserst and few reads : Link-List 

# # 2.2:  Suppose you’re building an app for restaurants to take customer
# orders. Your app needs to store a list of orders. Servers keep adding
# orders to this list, and chefs take orders off the list and make them.
# It’s an order queue: servers add orders to the back of the queue, and
# the chef takes the first order off the queue and cooks it. You should use link list 
# inserion and deletion is O(1) . 

# 2.3 : Let’s run a thought experiment. Suppose Facebook keeps a list of
# usernames. When someone tries to log in to Facebook, a search is
# done for their username. If their name is in the list of usernames,
# they can log in. People log in to Facebook pretty often, so there are
# a lot of searches through this list of usernames. Suppose Facebook
# uses binary search to search the list. Binary search needs random
# access—you need to be able to get to the middle of the list of
# usernames instantly. Knowing this, would you implement the list
# as an array or a linked list? Array 

# 2.4 People sign up for Facebook pretty often, too. Suppose you decided
# to use an array to store the list of users. What are the downsides
# of an array for inserts? It takes more timr 
# In particular, suppose you’re using binary
# search to search for logins. What happens when you add new users
# to an array? binary search remains uneffected , given that array is sorted afer insert 

# Ideally an array of link-list is used . 

