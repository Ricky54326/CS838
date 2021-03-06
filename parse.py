#!/usr/bin/python

# convert reviews in format [number] [number] review [number] [number] into sep files.
# CS 838 - project stage 2
# Riccardo Mutschlechner, Jale Dinler, Steven Lamphear

import re


def main():

    # file to open
    filename = "testReviews.csv"

    # regex for start/end of review
    # [\s] is any whitespace
    # regex = "[0-9]+[\s][0-9]+" # use this one for the tagged_reviews.csv
    regex = "[0-9]+,[0-9]+" # use this one for the finalized trainReview/testReview.csv

    # reviews will be list of list of string
    # words will be list of string (one review)
    reviews = []
    words = []

    # open reviews as read only
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split(" "):

                # if we find the start of a review, start a new one.
                if re.search(regex, word):
                    reviews.append(" ".join(words)); # append review to review list
                    words = [] # reset words array
                    #print "Found! ", word;

                words.append(word);
        reviews.append(" ".join(words)); # one final append

    count = 0
    print "Reviews found: ", len(reviews)

    inp = raw_input("Write them to files? y/n\n")
    if(inp == "n" or inp == "N"):
        return;

    for review in reviews:
        fn = "reviews_individual/"+filename+"."+str(count)+".txt"
        with open(fn, 'w+') as f:
            f.write(review)
        count = count + 1

if __name__ == "__main__":
    main();
