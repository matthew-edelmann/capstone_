# capstone_

Give a why first. 

AirBnB has been ...
This project aims to ...


## Problem Statement:
AirBnB is a company founded in 2008. It allows home owners/renters to temporarily use their places as a hotel. The user has to put their own value per night for the guest to pay. I wanted to see if I could predict the price of an AirBnB in the New York City area. I was aiming at someone who has a space in the New York City area, and may want to use it for an AirBnB. I will try to give them an estamated price based on the borough they live in and other factors. I will also give them the errors with the model, as there are many factors I may not have such as their rent price or living expenses.

## The Data
The data was colected from http://insideairbnb.com/get-the-data/. This is some data released from AirBnB. I downloaded the calendar and listings data from their New York file. A brief explaination of both is as follows. We are given an ID for both to merge them together. The calendar has all the dates that the AirBnB is available. They give dates, wheather or not it is available, price, and the minimum and maximum nights one can stay. The listings has much more information. We get information about its location, the host, specs about the AirBnB such as bedrooms and bathrooms, the type of stay, info about the reviews and much more.

The files to the csv are here:

* [`calendar.csv`](./data/calendar.csv)

* [`listings.csv`](./data/listings.csv)

## Cleaning

To clean the data, I had to fix or delete much of the entries as well as merge the 2 dataframes together. First I dealt with the calendar dataset. This one was much simpilar as it had less columns. Here are the steps I took:

1. I turned the date column into a datetime type.
2. The avaliable column had entries t and f for true or false. I changed t to 1 and f to 0.
3. Fixed the price column into being a float type.
4. Droped the adjusted_price column.

With that the calendar dataframe is done. Now we will look at the listings data frame. Here are the steps I took to clean it up.

1. Drop unneccisary columns. I droped at different parts of the cleaning but will only put it here once. Here is a full list of the columns that I droped: 'listing_url', 'scrape_id', 'last_scraped', 'name', 'listing_url', 'scrape_id', 'last_scraped', 'name', 'picture_url', 'host_url', 'host_name', 'host_since', 'host_thumbnail_url', 'host_picture_url', 'calendar_last_scraped', 'host_location', 'description', 'neighborhood_overview', 'host_about', 'host_response_rate', 'host_acceptance_rate', 'neighbourhood', 'bathrooms', 'bathrooms_text', 'bedrooms', 'calendar_updated', 'first_review', 'last_review', 'license', 'host_neighbourhood', 'reviews_per_month', 'host_total_listings_count', 'minimum_minimum_nights', 'maximum_minimum_nights', 'minimum_maximum_nights', 'maximum_maximum_nights', 'minimum_nights_avg_ntm', 'maximum_nights_avg_ntm', 'availability_30', 'availability_60', 'availability_90', 'number_of_reviews_ltm', 'number_of_reviews_l30d', 'calculated_host_listings_count_entire_homes', 'calculated_host_listings_count_private_rooms', and 'calculated_host_listings_count_shared_rooms'.
2. Filling nan values with the word 'unknown' in the following columns: host_response_time colunm, 'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness', 'review_scores_checkin', 'review_scores_communication', 'review_scores_location', and 'review_scores_value'
3. I fixed the price value to be a float value type
4. Then droped nan values

With that finished I then merged the 2 dataframes together. The new dataframe is called df_full. Naturally there was some null values. I dropped them since it took up less than 1% of the data. Lastly, I created a month column that was derived from the date columns.

Finally, I exported the data. You can view it here:

* [`df_full.csv`](./data/df_full.csv)

## Exploratory Data Analysis

Here, we will be looking at some EDA. let's look at some of the findings:

Price vs host_response_time:

![Alt text](./pics/host_response_time_graph.jpg)

A host that responds in a few days or more has the highest priced AirBnBs. The rest are roughly the same.

Price < $1000 vs host_is_superhost:

![Alt text](./pics/host_is_superhost_graph.jpg)







