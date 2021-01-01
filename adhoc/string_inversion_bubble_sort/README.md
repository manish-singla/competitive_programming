# Programming challenge description: 
Recommender System is capable of predicting the preferences of an active user for a set of items. For example, an online store can suggest a product to the shopper based on a history of purchases or page views. 

One of the traditional approaches to construct such a system is to use Collaboralive Filtering. it does not require any information about the items themselves and makes recommendations based on the past behavior of the users. Usually, collaborative filtering can be reduced to two steps:
- Look for users with similar interests as the active user.
- Ratings from the other users identified above to make a prediction for the active user.
 
Your task is to implement the first step using the number of inversions in the lists of user ratings as a numerical similarity measure. An Inverslon is a pair of elements (Si, Sj)) of the sequence, such that i < j and Si<Sj).
- Array (1,2,3,4,5) has zero inversions. 
- Array (5,1,2,3,4) has four inversions: (5,1), (5,2), (5,3), (5,4)
- Array (1,3,5,2,4) has three inversions (3,2), (5,2), (5,4)
The maximum possible number of inversions in the array with n elements is = n* (n-1) / 2


Now suppose that we asked several people to select three music genres. Now, we can form lists with ratings for each person from the most favorite genre to the least favorite. If a person in this set has identical preferences and ranks items exactly the same way as the active user, the number of inversions in the array would be zero. In general, the more inversions the array has, the more varied preferences are.

### Input
Bob:Rock,Blues,Jazz

Alice:Rock,Jazz,Blues

John:Jazz,Blues,Rock


Each line contains a user name and a list of their preferences separated by a colon. Items in the list are comma-separated. The first line of the input has an active user (the user whom a prediction is for).
Output: Print the list of users to be considered for making a recommendation. The list must be sorted by the number of inversions in ascending order. If two users have the same count of inversions sort them alphabetically.

In our example, Alice has 1 inversion compared to Bob. Meanwhile, John has 3 inversions compared to Bob. So, Alice has more preferences in common with Bob and she is more suitable as the basis of a prediction.

### Output
Print the list of users to be considered for making a recommendation. The list must be sorted by the number of inversions in ascending order. If two users have the same count of inversions sort them alphabetically.
Alice 1, John 3

### Algorithm
1. Assign numbers to First user choice in First come first way - O(n)
2. For each subsequent user - O(n * m)
    1. Map user choices to numbers assigned in first step and save choices in an array.
    2. Use bubble sort on array created in above step and count the number of swap required to sort the array.
    3. Append user count to save it for later use.
3. sort the user count list in acsending order - O(n log(n))
