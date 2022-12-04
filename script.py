"""
Some descriptive statistics of the founding father's ages on 7/4/1776

Inspired by the interview of actor James Wood, available here, with timestamp at 573 seconds: https://youtu.be/9RsedoC_PN4?t=573

Age of founding fathers copied from here: https://allthingsliberty.com/2013/08/ages-of-revolution-how-old-1776
"""

import matplotlib.pyplot as plt
import pandas as pd
import re
from IPython import get_ipython

# Script settings
ipython = get_ipython()  # For running IPython magic commands (e.g., %matplotlib)
ipython.magic("matplotlib")  # Display plots inline

# Script
text = """Andrew Jackson, 9
(Major) Thomas Young, 12
Deborah Sampson, 15
James Armistead, 15
Sybil Ludington, 15
Joseph Plumb Martin, 15
Peter Salem, 16*
Peggy Shippen, 16
Marquis de Lafayette, 18
James Monroe, 18
Charles Pinckney, 18
Henry Lee III, 20
Gilbert Stuart, 20
John Trumbull, 20
Aaron Burr, 20
John Marshall, 20
Nathan Hale, 21
Banastre Tarleton, 21
Alexander Hamilton, 21*
John Laurens, 21
Benjamin Tallmadge, 22
Robert Townsend, 22
George Rogers Clark, 23
David Humphreys, 23
Gouveneur Morris, 24
Betsy Ross, 24
William Washington, 24
James Madison, 25
Henry Knox, 25
John Andre, 26
Thomas Lynch, Jr., 26^
Edward Rutledge, 26^
Abraham Woodhull, 26
Isaiah Thomas, 27
George Walton, 27*^
John Paul Jones, 28
Bernardo de Galvez, 29
Thomas Heyward, Jr., 29^
Robert R. Livingston, 29
John Jay, 30
Tadeusz Kosciuszko, 30
Benjamin Rush, 30^
Abigail Adams, 31
John Barry, 31
Elbridge Gerry, 31^
Casimir Pulaski, 31
Anthony Wayne, 31
Joseph Brant, 33
Nathanael Greene, 33
Thomas Jefferson, 33^
Thomas Stone, 33*^
William Hooper, 34^
Arthur Middleton, 34^
James Wilson, 34*^
Benedict Arnold, 35
Samuel Chase, 35^
Thomas Knowlton, 35
William Paca, 35^
John Penn, 35^
Hercules Mulligan, 36
Andrew Pickens, 36
Haym Salomon, 36
John Sullivan, 36
George Clymer, 37^
Charles Cornwallis, 37
Thomas Nelson, Jr., 37^
Ethan Allen, 38
Charles Carroll, 38^
King George III, 38
Francis Hopkinson, 38^
Carter Braxton, 39^
George Clinton, 39
John Hancock, 39^
Daniel Morgan, 39
Thomas Paine, 39
Patrick Henry, 40
Enoch Poor, 40
John Adams, 40^
Daniel Boone, 41
William Floyd, 41^
Button Gwinnett, 41*^
John Lamb, 41*
Francis Lightfoot Lee, 41^
Paul Revere, 41
Thomas Sumter, 41
Robert Morris, 42^
Thomas McKean, 42^
George Read, 42^
John Dickinson, 43
John Glover, 43
Benjamin Edes, 43
Samuel Huntington, 44^
Richard Henry Lee, 44^
Charles Lee, 44
Francis Marion, 44
Lord North, 44
George Washington, 44
Joseph Galloway, 45
Robert Treat Paine, 45^
Friedrich von Steuben, 45
Richard Stockton, 45^
Martha Washington, 45
William Williams, 45^
(Dr.) Thomas Young, 45*
Josiah Bartlett, 46^
Henry Clinton, 46
Joseph Hewes, 46^
William Howe, 46
George Ross, 46^
William Whipple, 46^
Caesar Rodney, 47^
John Stark, 47
Mercy Otis Warren, 47
William Ellery, 48^
Horatio Gates, 48
Artemas Ward, 48
Oliver Wolcott, 49^
Abraham Clark, 50^
Benjamin Harrison, 50^
George Mason, 50
Lewis Morris, 50^
Lord Stirling, 50
George Wythe, 50*^
Guy Carleton, 51
John Morton, 51*^
Comte de Rochambeau, 51
Lyman Hall, 52^
James Rivington, 52*
Samuel Adams, 53^
Comte de Grasse, 53
John Witherspoon, 53^
John Burgoyne, 54
Johann de Kalb, 55
Roger Sherman, 55^
Thomas Gage, 56
James Smith, 56^
Israel Putnam, 58
Comte de Vergennes, 58
Lewis Nicola, 59*
George Germain, 60
Philip Livingston, 60^
George Taylor, 60*^
Matthew Thornton, 62^
Francis Lewis, 63^
John Hart, 65*^
Stephen Hopkins, 69^
Benjamin Franklin, 70^
Samuel Whittemore, 81"""

li = text.split("\n")

di = {}
for it, el in enumerate(li):
    di2 = {}
    pattern1 = r"(.+),"  # Captures name
    obj1 = re.search(pattern1, el)
    pattern2 = r"([0-9]+)"  # Captures age
    obj2 = re.search(pattern2, el)
    pattern3 = r"[0-9]+(.*)"  # Captures notes
    obj3 = re.search(pattern3, el)
    di2["name"] = obj1.groups()[0]
    di2["age"] = obj2.groups()[0]
    di2["notes"] = obj3.groups()[0]
    di[it] = di2
    
df = pd.DataFrame.from_dict(di, orient="index")
df.iloc[:,1] = df.iloc[:,1].astype(int)  # Convert from string to integer

# Descriptive statistics
mask = df["notes"].apply(lambda x: "^" in x)  # "^" Denotes those who signed the Declaration of Independence
series = df[mask].iloc[:,1]
series.hist()
plt.show()

statistics = {}
statistics["Minimum"] = series.min()
statistics["Q1"] = series.quantile(.25)
statistics["Q2"] = series.quantile(.5)  # Same as median
statistics["Mean"] = round(series.mean(), 2)
statistics["Q3"] = series.quantile(.75)
statistics["Maximum"] = series.max()

summary = pd.DataFrame.from_dict(statistics, orient="index").T
print(summary)
#    Minimum    Q1    Q2   Mean    Q3  Maximum
# 0     26.0  36.5  44.0  44.27  50.0     70.0

# NOTE: In conclusion, we see that most founding fathers were middle aged, with half 
# being between 36 and 44 years of age. A quarter were 36 or younger, which is fairly young
# in my opinion. At least one founding father was 26 years old at signing, quite an 
# accomplishment for that age. In the original data we see that James Monroe, the 4th
# US president, was 18 at the age of signing, however, he himself did not sign it,
# according to the data from the cited websited.
# 
# Actor James Wood brought up James Monroe when talking about how some people complain
# about how the constitution was written by "a bunch of old white men". It seems his
# statemenet is poorly structured because the declaration of independence and the
# US constitution are two different things. On top of that the US constitution is
# the sequel to its original incarnation, the Articles of Confederation. However,
# there is a kernel of reason in James Woods broaching of the subject; the relative age
# of the founding fathers is fairly young: 44 is younger than 60, and definitely younger than 
# either Trump or Biden when either first became president in 2016 and 2020,
# respectively.

# TODO: Plot summary statistics on histogram
for name, value in statistics.items():
  pass
