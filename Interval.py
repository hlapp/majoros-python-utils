#=========================================================================
# This is OPEN SOURCE SOFTWARE governed by the Gnu General Public
# License (GPL) version 3, as described at www.opensource.org.
# Copyright (C)2016 William H. Majoros (martiandna@gmail.com).
#=========================================================================
from __future__ import (absolute_import, division, print_function, 
   unicode_literals, generators, nested_scopes, with_statement)
from builtins import (bytes, dict, int, list, object, range, str, ascii,
   chr, hex, input, next, oct, open, pow, round, super, filter, map, zip)
import sys

#=========================================================================
# Attributes:
#   begin
#   end
# Methods:
#   i=Interval(begin,end)
#   print(file=STDOUT)
#   bool=interval.overlaps(other)
#   bool=interval.contains(position)
#   bool=interval.containsInterval(other)
#   intersection=interval.intersect(other)
#   union=interval.union(other) # returns an array of intervals
#   diff=interval.minus(other)  # returns an array of intervals
#   length=interval.getLength()
#   length=interval.length()
#   bool=interval.equals($other)
#   other=interval.clone()
#   bool=interval.isEmpty()
#   d=interval.relativeDistanceFromBegin(pos)
#   d=interval.relativeDistanceFromEnd(pos)
#   interval.shift(delta)
#=========================================================================

class Interval:
   """"Interval represents an interval (a,b] in which a is inclusive and
       b is not
   """
   def __init__(self,begin=0,end=0):
      self.begin=begin
      self.end=end

   def print(self,file=sys.stdout):
      print("(",self.begin,",",self.end,")",sep="",end="",file=file)

   def overlaps(self,other):
      return self.begin<other.end and other.begin<self.end

   def contains(self,index):
      return index>=self.begin and index<self.end

   def containsInterval(self,other):
      return self.begin<=other.begin and self.end>=other.end

   def isEmpty(self):
      return self.begin>=self.end

   def clone(self):
      return Interval(self.begin,self.end)

   def intersect(self,other):
      if(self.isEmpty()): return self.clone()
      if(other.isEmpty()): return other.clone()
      begin=max(self.begin,other.begin)
      end=min(self.end,other.end)
      return Interval(begin,end)

   def length(self):
      L=self.end-self.begin
      return 0 if L<0 else L

   def getLength(self):
      return self.length()

   def equals(self,other):
      return self.begin==other.begin and self.end==other.end

   def relativeDistanceFromBegin(self,pos):
      if(not self.contains(pos)): raise IndexError(pos)
      return (pos-self.begin)/self.length()

   def relativeDistanceFromEnd(self,pos):
      if(not self.contains(pos)): raise IndexError(pos)
      return (self.end-pos)/self.length()

   def union(self,other):
      s=[]
      if(self.overlaps(other)):
         s.append(Interval(self.begin,other.end))
      else:
         s.append(self,other)
      return s

   def minus(self,other):
      if(not self.overlaps(other)): return [self]
      s=[]
      if(self.begin<other.begin):
         s.append(Interval(self.begin,other.begin))
      if(self.end>other.end):
         s.append(Interval(other.end,self.end))
      return s

   def __str__(self):
      return "("+str(self.begin)+","+str(self.end)+")"

   def __repr__(self):
      return "("+str(self.begin)+","+str(self.end)+")"

   def shift(self,delta):
      self.begin+=delta
      self.end+=delta
