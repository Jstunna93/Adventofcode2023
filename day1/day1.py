#!/usr/bin/env python3

import pandas as pd
from argparse import ArgumentParser

def getFile(path=''):
    df = pd.read_csv(path)
    return df

def getList(df):
    l1=[]
    for col in df.columns:
        l1.append(col)
    return l1

def findNum1(s=''):
    numList=[]
    for c in s:
        if c.isnumeric():
            numList.append(c)
    return numList


def getSum(nList=[]):
    n0=str(nList[0])
    n1=str(nList[-1])
    sum=n0+n1
    sum=int(sum)
    return sum

def part1(path=''):
    df = getFile(path)
    l1 = getList(df)
    tList=[]
    totalSum=0
    for item in l1:
        nums=findNum(item)
        for num in nums:
            sumNum = getSum(num)
            totalSum+=sumNum
            tList.append(sumNum)
    return sumNum, tList

def get_args():
    parser = ArgumentParser(description='Get args')
    parser.add_argument('--path', default=None, help='Path to AOC file')
    return parser.parse_args()

def main():
    args = get_args()
    path = str(args.path)
    num,tlist = part1(path)
    print(num)


if __name__ == "__main__":
    main()
