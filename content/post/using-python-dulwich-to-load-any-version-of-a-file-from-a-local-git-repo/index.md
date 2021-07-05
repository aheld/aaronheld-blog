---
title: "Using python-dulwich to load any version of a file from a local git repo"
date: "2011-04-02"
categories: 
  - "code"
  - "professional"
  - "python"
tags: 
  - "labweek2011"
  - "python"
---

On Monday we are kicking off an innovation week (more to come on that topic) and I've devised a little project that includes nearly every buzzword I'm interested in.

I'm spending some time doing some technical spikes to see what is possible and I found a need to load a particular file from a git repo given the path and tree hash.

I grabbed my trusty python, dulwich (native python-git library) and gave it a shot. After a few minutes writing complicated looking recursive code I jumped over to irc where the friendly author pointed me to a convenience function that does what I needed.

Here is the short answer:

from dulwich.repo import Repo
from dulwich.object\_store import tree\_lookup\_path

r = Repo('/Documents/projects/gitdep/rails')
def get\_file(tree, path):
    (mode,sha) = tree\_lookup\_path(r.get\_object,tree,path)
    return r\[sha\].data

tree = '7e7331fce169bbe1d6be71a30c1e1f7ab2e6ceba'
path = 'activemodel/examples/validations.rb'

print get\_file(tree,path)

This gives me a rails validation file from last year. Nothing special about this file, I just find the rails git repo an interesting playground for git experimentation.
