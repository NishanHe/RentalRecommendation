import argparse
import pandas as pd
import re
import math

info = pd.read_csv("combined.csv")  # will change the name to the real csv file
# rating it the scores for ranking
#info = info.sort_values(by=['rating']) # with change to the real column name

parser = argparse.ArgumentParser(description='Example with long option names')

parser.add_argument('--latest', action="store_true", default=False, help="default is False, input True to see cache")
parser.add_argument('--property', action="store", dest="witharg", help="to see property ")
parser.add_argument('--witharg2', action="store", dest="witharg2", type=int)
parser.add_argument('-o', '--output', action='store_true', help="shows output")

args = parser.parse_args()

while True:
    view_choice = input("Show the top 5 properties we recommend? choose y/n (enter exit to quit)\n")
    if view_choice == "exit":
        break
    elif view_choice == "y":

        house_item = "{}. {}  \n" \
                    "Neighborhood: {}\n" \
                    "Size: {} sqft\n" \
                    "Number of bedrooms: {}\n" \
                     "Price: {}$/month"

        # do we have address?
        for i in range(1, 6):

            num_bed = info.loc[i]["number bedrooms"]
            if math.isnan(num_bed):
                num_bed = "Unknown"
            else:
                num_bed = int(num_bed)
            print("\n", house_item.format(i, info.loc[i]["post title"], info.loc[i]["neighborhood"].strip()[1:-1],
                                           info.loc[i]["sqft"], num_bed,info.loc[i]["price"] ), "\n")

    elif view_choice == "n":
        # will call the fetch function
        break

    house_choice = input("\nSelect a property for more information : (type 'exit' to quit)\n")
    if house_choice == "exit":
        break

    elif int(house_choice) in range(1, 6) :
        t_str = "Transport Information"
        print("\n", t_str.center(50, "-"), "\n")
        trans_item = "Distance to nearest bus stop: {} meters\n" \
                    "Distance to CMU: {} meters\n" \
                    "Distance to downtown: {} meters\n" \
                    "Distance to nearest shuttle stop: {} meters"
        print(trans_item.format(info.loc[i]['bus_distance_CMU'], info.loc[i]['distance_to_CMU'],
                                info.loc[i]['distance_to_downtown'], info.loc[i]['nearest_shuttle_stop'][2]))

        r_str = "Restaurant"
        print("\n", r_str.center(50, "-"), "\n")
        print("5 restaurants near by")
        res_item = "Restaurant name: {}\n" \
                    "Rating: {}"
        restaruant = info.loc[i]['nearest_restaurants']
        restaruant = restaruant.split(",")

        for i in range(0, len(restaruant), 3):
            pat = r'[\[()\"\]]'
            name = ""
            for letter in restaruant[i]:
                if not re.search(pat, letter):
                    name = name + letter
            for index in range(len(name)):
                if name[index] == "'" and index not in range(1, len(name)-1):
                    name = name.replace("'", "")
            score = ""
            for c in restaruant[i+2]:
                if not re.search(pat, c):
                    score = score + c
            print(res_item.format(name.strip(), score))

        action = input("\nPress 'b' to go back to properties listing or type 'exit' to quit\n")
        if action == "b":
            continue
        elif action == "exit":
            break

#print(parser.parse_args())
