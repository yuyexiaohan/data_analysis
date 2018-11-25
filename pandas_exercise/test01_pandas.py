# coding=utf-8 
# Time : 2018/11/25
# Author : achjiang
import pandas as pd


df = pd.read_csv("./dogNames2.csv")
print(df[(800<df["Count_AnimalName"])|(df["Count_AnimalName"]<1000)])
print(df)
"""打印结果：
          Row_Labels  Count_AnimalName
0                  1                 1
1                  2                 2
2              40804                 1
3              90201                 1
4              90203                 1
5             102201                 1
6            3010271                 1
7              MARCH                 2
8              APRIL                51
9             AUGUST                14
10          DECEMBER                 4
11            SUNDAY                13
12            MONDAY                 4
13            FRIDAY                19
14               JAN                 1
15               JUN                 1
16           JANUARY                 1
17              JUNE                24
18              JULY                 9
19               MON                 2
20               MAY                13
21          NOVEMBER                 1
22           TUESDAY                 7
23         SEPTEMBER                 2
24         WEDNESDAY                10
25               SUN                 5
26     &QUOT;G&QUOT;                 1
27       (LEELA)LILA                 1
28              166Y                 1
29           2CHAINZ                 1
...              ...               ...
16190           ZUKI                 3
16191          ZUKIE                 1
16192           ZUKO                 5
16193           ZULA                 3
16194           ZULI                 1
16195           ZULU                11
16196           ZULY                 2
16197           ZUMA                 5
16198          ZUMBA                 3
16199           ZUNI                 3
16200          ZUREE                 1
16201           ZURI                 5
16202           ZUSA                 1
16203          ZUSHI                 1
16204           ZUSY                 1
16205           ZUTY                 1
16206           ZUZI                 1
16207          ZUZIA                 1
16208           ZUZU                16
16209       Z-WILLOW                 1
16210            ZYU                 1
16211             ZZ                 2
16212           ???Y                 1
16213           TRUE                 3
16214          37846                 1
16215          37916                 1
16216          38282                 1
16217          38583                 1
16218          38948                 1
16219          39743                 1

[16220 rows x 2 columns]
"""


