# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 21:37:33 2016

@author: cycleuser
@email: cycleuser@cycleuser.org

Copyright 2016 cycleuser

This file is part of GeoPython.

GeoPython is a set of fTrace softwares for geology related daily work: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the FTrace Software Foundation, either version 3 of the License, or (at your option) any later version.
GeoPython is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with GeoPython. If not, see http://www.gnu.org/licenses/.

This file is a module of Trace-plot.



"""
#!/usr/bin/env python

# coding=utf-8

lang = "python"



#You need to install numpy and matplotlib to use this module

import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math




class Point:
     x=0.0
     y=0.0
     Color = 'black'
     Size = 1
     Alpha = 0.5
     Marker='o'
     
     def __init__(self,X=0,Y=0,Color = 'black', Size = 1,Alpha = 0.5,Marker='o'):
           self.x=X
           self. y=Y
           self.Color=Color
           self.Size=Size
           self.Alpha=Alpha
           self.Marker=Marker

     def __del__(self):
         pass
    


class Line:   
    # Head= Point(0,0)
     Points=[]
     #Mid= []
     #End= Point(0,0)
     Length=0
     x=[]
     y=[]
     Color = 'black'
     Size = 1
     Alpha = 0.5
     Style='_'
     
     def __init__(self, Head= Point(),End= Point (),Mid=[],Color = 'black', Width = 1,Alpha = 0.5,Style='_'):
      #     self.Head.x= A.x
       #    self.Head.y= A.y
        #   self.Mid=C
             #  self.End.x= B.x
          # self.End.y= B.y
           
           self.Points.append(Head)
           
           for k in Mid:
               self.Points.append(k)
           
           self.Points.append(End)           
           
           self.Color=Color
           self.Width=Width
           self.Alpha=Alpha
           self.Style=Style
                         
           for index, i in enumerate(self.Points):
               self.x.append(i.x)
               self.y.append(i.y)
               
               if(index!=0):
                   self.Length+= Distance(self.Points[index-1],self.Points[index])
            
          
          #self.Length=math.sqrt(math.pow(self.Head.x-self.End.x, 2)+math.pow(self.Head.y-self.End.y, 2))

     def __del__(self):
         pass
 
     def AddPoint(self,NewPoint= Point(0,0)):       
         self.Length+= Distance(self.Points[-1],NewPoint)
         self.Points.append(NewPoint)  
         self.x.append(NewPoint.x)
         self.y.append(NewPoint.y)
        
#     def Draw(self):         
#         return (self.Head,self.End, self.Width,self.Color,self.Style)


def CrossPoint(x0,y0,x1,y1,x2,y2,x3,y3): 
    a = y1-y0 
    b = x1*y0-x0*y1 
    c = x1-x0 
    d = y3-y2 
    e = x3*y2-x2*y3 
    f = x3-x2 
    y = float(a*e-b*d)/(a*f-c*d) 
    x = float(y*c-b)/a 
    print(x,y)
    return([x,y])



def Distance(A= Point(3,4),B= Point(3,5)): 
    return(math.sqrt((A.x-B.x)**2+(A.y-B.y)**2))
    
def LineFormula(A= Point(3,4),B= Point(3,5)): 
    #Find formula of a line with Two given Points ky = m*x +n   
    k=1
    m=0
    n=0
   

    if(A.x==B.x):
        k=0
        m=1
        n=-A.x
    elif(A.y==B.y):        
        k=1
        m=0
        n=A.y  
    else: #(A.x!=B.x or A.y!=B.y):
        m=(B.y-A.y)/(B.x-A.x)
        n=A.y-m*A.x                   
    
    return(k,m,n)
        
def Cross(A= Point(3,4),B= Point(3,5),C= Point(4,4.5),D= Point(2,3.5)):
    #Find the cross point of two lines
    a = B.y-A.y 
    b = B.x*A.y-A.x*B.y 
    c = B.x-A.x
    d = D.y-C.y 
    e = D.x*C.y-C.x*D.y 
    f = D.x-C.x 
    
    if ((a*f-c*d)==0):    
        return("No Cross!")
    elif(a==0):
        y=A.y
        tmp= LineFormula(C,D)
        x= (tmp[0]*y)-tmp[2]/tmp[1]
        Answer= Point (x,y)
        return(Answer)    
    else:# ((a*f-c*d) !=0):
        y = float(a*e-b*d)/(a*f-c*d) 
        x = float(y*c-b)/a        
        Answer= Point (x,y)
        return(Answer)




def DrawPoint(a=Point(0,0)):
    plt.scatter(a.x,a.y,marker=a.Marker,c=a.Color,s=a.Size,alpha=a.Alpha)

def DrawLine(X=[0,1],Y=[0,1],LineColor='k',LineWidth=1,LineStyle="-",LineAlpha=0.3,LineLabel= ''):
    plt.plot(X,Y,color=LineColor, linewidth=LineWidth, linestyle=LineStyle,alpha= LineAlpha,label = LineLabel)




Element= [u'Rb',u'Ba',u'Th',u'U',
          u'Nb',u'Ta',u'K',u'La',
          u'Ce',u'Pr',u'Sr',u'P',
          u'Nd',u'Zr',u'Hf',u'Sm',
          u'Eu',u'Ti',u'Tb',u'Dy',
          u'Y',u'Ho',u'Er',u'Tm',
          u'Yb',u'Lu']





def DrawTraceFrame(LineWidth=1,LineColor='k'):
    
#This DrawTheLines function is used to draw the lines in the figure
    plt.figure(figsize=(12,6), dpi=80)
    plt.xlim(0,27)
    
    
    plt.xticks(np.linspace(1,26,26,endpoint=True),
       Element)
    plt.ylim(-6,4)
    
    
    plt.yticks(np.linspace(-1,7,9,endpoint=True),
               [u'',u'1',u'10',u'100',u'1000',u'10000',u'10000']
               )
    plt.xlabel(r'$Trace-Standardlized-Pattern$',fontsize=16)

#ax is used to set the axies
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',-6))


    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))



def PlotData(TraceRaw,Width=1,Color='b',Style="-"):
    DrawTraceFrame(LineWidth=1,LineColor='k')
    #TraceBase= pd.read_excel("Trace.xlsx")   

    
    for l in range(len(TraceRaw)):
        if(TraceRaw.at[l,'DataType']=='Standard' or TraceRaw.at[l,'DataType']=='standard' or TraceRaw.at[l,'DataType']=='STANDARD'):
            k=l
    
    
    for i in range(len(TraceRaw)):
        if(TraceRaw.at[i,'DataType']=='User' or TraceRaw.at[i,'DataType']=='user'or TraceRaw.at[i,'DataType']=='USER'):
            LineX =[]    
            LineY =[] 
            for j in range(len(Element)-1):
                 TmpPoint=(Point(j+1, math.log(abs((TraceRaw.at[i,Element[j]])/TraceRaw.at[k,Element[j]])),Color=TraceRaw.at[i,'Color'],Size=TraceRaw.at[i,'Size'],Alpha=TraceRaw.at[i,'Alpha'],Marker=TraceRaw.at[i,'Marker'])) 
                 LineX.append (TmpPoint.x)
                 LineY.append (TmpPoint.y)
                 DrawPoint(TmpPoint)
                        
            DrawLine(LineX,LineY,LineColor= TraceRaw.at[i,'Color'], LineWidth = TraceRaw.at[i,'Width'],LineStyle=TraceRaw.at[i,'Style'],LineAlpha=TraceRaw.at[i,'Alpha'],LineLabel=TraceRaw.at[i,'Label'])
    plt.legend(loc='upper right', frameon=False)
    plt.savefig("TraceFromChaiHui-Plot.png",dpi=600)
    plt.savefig("TraceFromChaiHui.svg",dpi=600)
    plt.show()
    



if __name__ == '__main__':
    TraceRawData= pd.read_excel("TraceFromChaiHui.xlsx")
    PlotData(TraceRawData)







