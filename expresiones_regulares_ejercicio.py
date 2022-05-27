# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# Rules for a smiling face:

# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D


#solution

import re
def count_smileys(arr):
    return len([i for i in arr if re.findall('[:;][-~]?[)D]', i)])


# [:;] signifies that, we want only : or ; as eyes(As per Problem).
# [-~]? signifies that, either we want - or ~ as nose , or we don't want it(As per Problem).

#                    ? is used to match 0 or 1 occurrences.
# [)D] signifies that, we want ) or D as mouth(As per Problem).