import numpy as np # linear algebra
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


import pandas as pd

test = pd.read_csv("test.csv")
train = pd.read_csv("train.csv")

#print train.iloc[:,:8].head()

print train.shape  # (1460, 81)
print test.shape   # (1459, 80)

#print train.isnull().sum()

'''
Id                  0
MSSubClass          0
MSZoning            0
LotFrontage       259
LotArea             0
Street              0
Alley            1369
LotShape            0
LandContour         0
Utilities           0
LotConfig           0
LandSlope           0
Neighborhood        0
Condition1          0
Condition2          0
BldgType            0
HouseStyle          0
OverallQual         0
OverallCond         0
YearBuilt           0
YearRemodAdd        0
RoofStyle           0
RoofMatl            0
Exterior1st         0
Exterior2nd         0
MasVnrType          8
MasVnrArea          8
ExterQual           0
ExterCond           0
Foundation          0
                 ... 
BedroomAbvGr        0
KitchenAbvGr        0
KitchenQual         0
TotRmsAbvGrd        0
Functional          0
Fireplaces          0
FireplaceQu       690
GarageType         81
GarageYrBlt        81
GarageFinish       81
GarageCars          0
GarageArea          0
GarageQual         81
GarageCond         81
PavedDrive          0
WoodDeckSF          0
OpenPorchSF         0
EnclosedPorch       0
3SsnPorch           0
ScreenPorch         0
PoolArea            0
PoolQC           1453
Fence            1179
MiscFeature      1406
MiscVal             0
MoSold              0
YrSold              0
SaleType            0
SaleCondition       0
SalePrice           0
Length: 81, dtype: int64'''

#sns.heatmap(train.isnull(),yticklabels=False,cbar=False)
#sns.heatmap(test.isnull(),yticklabels=False,cbar=False)
#plt.savefig('Null_values_before_EDA')
#plt.show()

count_MSZoning_attribs = train['MSZoning'].value_counts()
#print count_MSZoning_attribs 

'''
RL         1151
RM          218
FV           65
RH           16
C (all)      10
Name: MSZoning, dtype: int64'''

#print train.info()
'''
RangeIndex: 1460 entries, 0 to 1459
Data columns (total 81 columns):
Id               1460 non-null int64
MSSubClass       1460 non-null int64
MSZoning         1460 non-null object
LotFrontage      1201 non-null float64
LotArea          1460 non-null int64
Street           1460 non-null object
Alley            91 non-null object
LotShape         1460 non-null object
LandContour      1460 non-null object
Utilities        1460 non-null object
LotConfig        1460 non-null object
LandSlope        1460 non-null object
Neighborhood     1460 non-null object
Condition1       1460 non-null object
Condition2       1460 non-null object
BldgType         1460 non-null object
HouseStyle       1460 non-null object
OverallQual      1460 non-null int64
OverallCond      1460 non-null int64
YearBuilt        1460 non-null int64
YearRemodAdd     1460 non-null int64
RoofStyle        1460 non-null object
RoofMatl         1460 non-null object
Exterior1st      1460 non-null object
Exterior2nd      1460 non-null object
MasVnrType       1452 non-null object
MasVnrArea       1452 non-null float64
ExterQual        1460 non-null object
ExterCond        1460 non-null object
Foundation       1460 non-null object
BsmtQual         1423 non-null object
BsmtCond         1423 non-null object
BsmtExposure     1422 non-null object
BsmtFinType1     1423 non-null object
BsmtFinSF1       1460 non-null int64
BsmtFinType2     1422 non-null object
BsmtFinSF2       1460 non-null int64
BsmtUnfSF        1460 non-null int64
TotalBsmtSF      1460 non-null int64
Heating          1460 non-null object
HeatingQC        1460 non-null object
CentralAir       1460 non-null object
Electrical       1459 non-null object
1stFlrSF         1460 non-null int64
2ndFlrSF         1460 non-null int64
LowQualFinSF     1460 non-null int64
GrLivArea        1460 non-null int64
BsmtFullBath     1460 non-null int64
BsmtHalfBath     1460 non-null int64
FullBath         1460 non-null int64
HalfBath         1460 non-null int64
BedroomAbvGr     1460 non-null int64
KitchenAbvGr     1460 non-null int64
KitchenQual      1460 non-null object
TotRmsAbvGrd     1460 non-null int64
Functional       1460 non-null object
Fireplaces       1460 non-null int64
FireplaceQu      770 non-null object
GarageType       1379 non-null object
GarageYrBlt      1379 non-null float64
GarageFinish     1379 non-null object
GarageCars       1460 non-null int64
GarageArea       1460 non-null int64
GarageQual       1379 non-null object
GarageCond       1379 non-null object
PavedDrive       1460 non-null object
WoodDeckSF       1460 non-null int64
OpenPorchSF      1460 non-null int64
EnclosedPorch    1460 non-null int64
3SsnPorch        1460 non-null int64
ScreenPorch      1460 non-null int64
PoolArea         1460 non-null int64
PoolQC           7 non-null object
Fence            281 non-null object
MiscFeature      54 non-null object
MiscVal          1460 non-null int64
MoSold           1460 non-null int64
YrSold           1460 non-null int64
SaleType         1460 non-null object
SaleCondition    1460 non-null object
SalePrice        1460 non-null int64
dtypes: float64(3), int64(35), object(43)
memory usage: 924.0+ KB'''

#print train['Alley'].head()
'''
0    NaN
1    NaN
2    NaN
3    NaN
4    NaN'''

train['LotFrontage']=train['LotFrontage'].fillna(train['LotFrontage'].mean())
test['LotFrontage']=test['LotFrontage'].fillna(train['LotFrontage'].mean())
#print train['LotFrontage'].isnull().sum()  # 0

#print (train['MSZoning'].isnull().sum())   # 0
#print (test['MSZoning'].isnull().sum())   # 4

test['MSZoning']= test['MSZoning'].fillna(test['MSZoning'].mode()[0])
#print test['MSZoning'].isnull().sum()  # 0
# Dropping Alley column since it has more null values
train.drop(['Alley'],axis=1,inplace=True)
test.drop(['Alley'],axis=1,inplace=True)

train['BsmtCond'] = train['BsmtCond'].fillna(train['BsmtCond'].mode()[0])
train['BsmtQual'] = train['BsmtQual'].fillna(train['BsmtQual'].mode()[0])
test['BsmtCond'] = test['BsmtCond'].fillna(test['BsmtCond'].mode()[0])
test['BsmtQual'] = test['BsmtQual'].fillna(test['BsmtQual'].mode()[0])

train['FireplaceQu'] = train['FireplaceQu'].fillna(train['FireplaceQu'].mode()[0])
train['GarageType'] = train['GarageType'].fillna(train['GarageType'].mode()[0])
test['FireplaceQu'] = test['FireplaceQu'].fillna(test['FireplaceQu'].mode()[0])
test['GarageType'] = test['GarageType'].fillna(test['GarageType'].mode()[0])

train.drop(['GarageYrBlt'],axis=1,inplace=True)
test.drop(['GarageYrBlt'],axis=1,inplace=True)

train['GarageFinish'] = train['GarageFinish'].fillna(train['GarageFinish'].mode()[0])
train['GarageQual'] = train['GarageQual'].fillna(train['GarageQual'].mode()[0])
train['GarageCond'] = train['GarageCond'].fillna(train['GarageCond'].mode()[0])
test['GarageFinish'] = test['GarageFinish'].fillna(test['GarageFinish'].mode()[0])
test['GarageQual'] = test['GarageQual'].fillna(test['GarageQual'].mode()[0])
test['GarageCond'] = test['GarageCond'].fillna(test['GarageCond'].mode()[0])

train.drop(['PoolQC','Fence','MiscFeature'],axis=1,inplace=True)
test.drop(['PoolQC','Fence','MiscFeature'],axis=1,inplace=True)

train.drop(['Id'],axis=1,inplace=True)
test.drop(['Id'],axis=1,inplace=True)
#print train.shape   # (1460, 75)
#print test.shape   # (1459, 74)

train['MasVnrType']= train['MasVnrType'].fillna(train['MasVnrType'].mode()[0])
train['MasVnrArea']= train['MasVnrArea'].fillna(train['MasVnrArea'].mode()[0])
test['MasVnrType']= test['MasVnrType'].fillna(test['MasVnrType'].mode()[0])
test['MasVnrArea']= test['MasVnrArea'].fillna(test['MasVnrArea'].mode()[0])

train['BsmtExposure']= train['BsmtExposure'].fillna(train['BsmtExposure'].mode()[0])
test['BsmtExposure']= test['BsmtExposure'].fillna(test['BsmtExposure'].mode()[0])


train['BsmtFinType2']= train['BsmtFinType2'].fillna(train['BsmtFinType2'].mode()[0])
test['BsmtFinType2']= test['BsmtFinType2'].fillna(test['BsmtFinType2'].mode()[0])                                                

train.dropna(inplace=True)

#sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='YlGnBu')
#plt.savefig('after_remove_all_null_feature_engg')
#plt.show()

# Now finally check the shape

print train.shape  # (1422, 75)
print test.shape   # (1459, 74)

#colums = train.columns
#print colums       # to print all the columns
#print len(colums)  # 75

# Handling categorical features
  # Listed all categorical feature column names to get dummies
columns =['MSZoning','Street','LotShape','LandContour','Utilities','LotConfig',
          'LandSlope','Neighborhood','Condition2','BldgType','Condition1','HouseStyle',
          'SaleType','SaleCondition ','ExterCond','ExterQual','Foundation','BsmtQual',
          'BsmtCond','BsmtExposure','BsmtFinType1','BsmtFinType2','RoofStyle',
          'RoofMatl','Exterior1st','Exterior2nd','MasVnrType','Heating','HeatingQC',
          'CentralAir','Electrical','KitchenQual','Functional','FireplaceQu',
          'GarageType','GarageFinish','GarageQual','GarageCond','PavedDrive']

print len(columns)  # 39

#print test.shape  # (1459, 74)

# write our test to the seperate file

test.to_csv('formulatedtest.csv',index=False)
test_df = pd.read_csv('formulatedtest.csv')

print test_df.shape  #  (1459, 74)

# concatenate both datasets

final_df=pd.concat([train,test_df],axis=0)

def category_onehot_multcols(multcolumns):
    df_final =final_df
    i=0
    for field in multcolumns:
        print field
        df1= pd.get_dummies(final_df[field],drop_first=True)
        final_df.drop([field],axis=1,inplace=True)
        if i==0:
            df_fianl = df1.copy()
        else:
            df_final = pd.concat([df_final,df1],axis =1)
        i+=1

    df_final = pd.concat([final_df,final_df],axis=1)
    return df_final

main_dataset = train.copy()

# Read the same test data file and merge or concate with train dataset

test_df = pd.read_csv('formulatedtest.csv')
##
print test_df.shape  #  (1459, 74)
##
### concatenate both datasets
##
final_data=pd.concat([train,test_df],axis=0)

print final_data.shape   # (2881, 75)

# Now apply a function hers

final_df = category_onehot_multcols(columns)
##
print final_df.shape
##    





