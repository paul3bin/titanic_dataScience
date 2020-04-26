"""
Example Project for Titanic Dataset
"""
import numpy as np 
import pandas as pd 
from pandas import Series,DataFrame
import matplotlib.pyplot as plt 
import seaborn as sns 

titanic_df = pd.read_csv('train.csv')
print(titanic_df.head())
print(titanic_df.info())

#Questions
"""
Q1 - Who are the passengers in the titanic?(Gender,Age,Class,..etc)
Q2 - What deck were the passengers  on and how does that  relate to their class?
Q3 - Where did the passengers come from?
Q4 - Who was alone and who was with family?
Q5 - What factors helped someone survive the sinking?
"""

#Q1 

#getting the count of males and females and plotting them
sns.catplot(x='Sex',kind='count',data=titanic_df)
plt.show()

#to get a refresher on apply() method go to lecture 45

def male_female_child(passenger):
    age,sex = passenger
    if age<16:
        return 'child'
    else:
        return sex

#to apply the function to a column pass axis=1 as argument
titanic_df['person'] = titanic_df[['Age','Sex']].apply(male_female_child,axis=1)
print(titanic_df.head())

sns.catplot(x='Pclass',hue='person',kind='count',data=titanic_df)
plt.show()

titanic_df['Age'].hist(bins=70)
plt.show()

#Viewing the number of males,females and children 
sns.catplot(x='person',kind='count',data=titanic_df)
plt.show() 

#FacetGrid allows multiple figures in one plot
fig = sns.FacetGrid(titanic_df,hue='Sex',aspect=4)
fig.map(sns.kdeplot,'Age',shade=True)
oldest = titanic_df['Age'].max()
fig.set(xlim=(0,oldest))
fig.add_legend()
plt.show()
#aspect is used to set the aspect ratios

fig = sns.FacetGrid(titanic_df,hue='person',aspect=4)
fig.map(sns.kdeplot,'Age',shade=True)
oldest = titanic_df['Age'].max()
fig.set(xlim=(0,oldest))
fig.add_legend()
plt.show()

fig = sns.FacetGrid(titanic_df,hue='Pclass',aspect=4)
fig.map(sns.kdeplot,'Age',shade=True)
oldest = titanic_df['Age'].max()
fig.set(xlim=(0,oldest))
fig.add_legend()
plt.show()

print(titanic_df['Age'].mean())
#--------------------------------------------------------------
#for different type of palettes go to the following link
url = 'https://matplotlib.org/users/colormaps.html'

#Q2

deck = titanic_df['Cabin'].dropna()
print(deck.head())

levels = []
for level in deck:
    levels.append(level[0])
cabin_df = DataFrame(levels)
cabin_df.columns = ['Cabin']
sns.catplot(x='Cabin',kind='count',data=cabin_df,palette='winter_d')
plt.show()

cabin_df = cabin_df[cabin_df.Cabin != 'T']
sns.catplot(x='Cabin',kind='count',data=cabin_df,palette='summer')
plt.show()

#--------------------------------------------------------------
#Q3
sns.catplot(x='Embarked',kind='count',data=titanic_df,hue='Pclass',order=['C','Q','S'])
plt.show()

#--------------------------------------------------------------
#Q4
titanic_df['Alone'] = titanic_df.SibSp+titanic_df.Parch

titanic_df['Alone'].loc[titanic_df['Alone']>0]= "With Family"
titanic_df['Alone'].loc[titanic_df['Alone']==0] = "Alone"
url_info = 'http://stackoverflow.com/questions/20625582/how-to-deal-with-this-pandas-warning'
print(titanic_df.head())

sns.catplot(x='Alone',kind='count',data=titanic_df,palette='Blues')
plt.show()

#what factors help someone to survive the crash

#checking how many people survived the crash by using catplot
titanic_df['Survivor'] = titanic_df.Survived.map({0:'no',1:'yes'})
#if there is a confusion regarding the concept of mapping go to lecture-36
print(titanic_df.head())

sns.catplot(x='Survivor',kind='count',data=titanic_df,palette='Set1')
plt.show()

sns.catplot(x='Survivor',hue='Pclass',kind='count',data=titanic_df)
plt.show()

# sns.catplot(x='Pclass',y='Survived',hue='person',data=titanic_df)
# plt.show()

sns.lmplot('Age','Survived',data=titanic_df)
plt.show()

sns.lmplot('Age','Survived',hue='Pclass',data=titanic_df,palette='winter')
plt.show()

#creating bins to clean up the plot a little bit 
#bins makes the plot more readable
generations = [10,20,40,60,80]
sns.lmplot('Age','Survived',hue='Pclass',data=titanic_df,palette='winter',x_bins=generations)
plt.show()

sns.lmplot('Age','Survived',hue='Sex',data=titanic_df,palette='winter',x_bins=generations)
plt.show()
#--------------------------------------------------------------

#extra questions 
#EQ-1 Did the deck have an effect on the survival of the passengers?
#EQ-2 Did having a family member increase the odds of survival?