#!/bin/bash
# Script to experiment with the binary search method in FTDdriver.py
echo "Enter number of suits"
read numSuits
echo "Enter max value"
read maxVal
echo "Enter number of trials"
read numTrial

for ((counter = 1; counter <= $numTrial; counter++))
do
python3 FTDdriver.py
echo numSuits
echo maxVal
done
