# Takeaways from Clustering Overview

What is clustering?
Grouping a bunch of points based on their similar characteristics

Unsupervised Algorithm
No y values, b/c we don't have a label target
We have only X values (indepent variables)
We'll get cluster numbers back from the clustering model

With k-means, we define the K value == how many clusters?

There's an opportunity (really good one) for us to cluster, 
then really deeply consider/analyze those clusters
to see if we can name them ourselves (after the fact)

Who are our cloud customers?
How can I measure feature similarities between groups?
Maggie named the clusters logically
    - flat
    - sporatic
    - high volatilty
    - low/med volatility


The above gives us a brand new feature, that cluster name... 
Think of how many features it took to produce these 4 cluster names
"Dimensionality Reduction"

Feature engineering

Clustering helps us explore the data more

Hard to figure out what k value to use.


K-Means is clustering = each cluster has a centroid w/ a mean


Distance Metrics = How we measure distance matters
- Euclidean distance = as the crow flies = perfect if our data is drones and it's latitude, longitude.
- Manhattan distance = taxi cab distance = legend of zelda distance (only x and y, no hypoteneus)
    - Say we're an insurance company and we want to cluster on driver features
    - manhattan distance would be a good measure for how much they're driving (small, medium, large)
- Cosine similarity = angle between vectors
    - vectors that are parallel, have a cosine similarity of 1 indicating they are maximally "similar"
    - a = [100, 100, 100, 100], b = [100, 100, 100, 100]
    - a = [0, 0, 1], b = [0, 0, 0] 
    - [0, 0, 0] vs. [1, 1, 1] # orthogonal
    - if the cosine similiarity is 0, it means two vectors have nothing in common

```
    price, #_bedrooms, #_bathrooms, sqft
    180k, 3, 3, 1.7k
    200k, 4, 3, 2.4k
    200k, 4, 2, 2.4k
    999k, 14, 8, 6k
    759k, 8, 4, 5k
```

Outliers can have a really big (negative) impact when you're trying to cluster.
When we're clustering, we're measuring distancxe
And when we're measuring distance, our data needs to be scaled on the same units also.

