---
title: GetConnector blocked
author: EZW
date: 2024-07-22
tags: GetConnector, troubleshoot
---
Have you received a message that a GetConnector in your environment has been blocked? Then this article is for you.

AFAS maintains a Fair Use policy for API usage. In practice, this means that every day the 10 heaviest users receive a message that they need to adjust their process.
In some cases it's different: AFAS blocks a GetConnector because so many calls are made that other users experience performance problems.

## Problem analysis

A GetConnector is always called by another process; this is often an external application that connects with AFAS, but it can also be something running internally, for example a script from a colleague. Find out which process this is:
1. From the name of the GetConnector you can often already tell which application or process it belongs to. 
2. Check if there's an integration with AFAS that hasn't worked since the GetConnector was blocked. Is management complaining that the figures aren't being updated, for example?
3. Check if there's an integration with AFAS that's now giving errors. Because the GetConnector is blocked, the AFAS API gives an error message when the GetConnector is called. You'll see these errors in the log of the external application.

## Solve the problem

1. Is it an external application? Contact the supplier and explain that their GetConnector has been blocked by AFAS. If it's a certified integration with AFAS, the supplier can then contact AFAS to solve the problem.
2. Is it an internal process? Discuss with the responsible colleague that fewer calls need to be made, or look at how the calls can be improved so they consume fewer resources on AFAS servers. If necessary, contact AFAS via a [System Integrator Request](https://klant.afas.nl/systemintegrators). Note, there are costs involved.

## Unblock the GetConnector

Once the problem is solved, you can unblock the GetConnector. You unblock a GetConnector via the following path: **General / Output / Management / GetConnector**. Then choose the action **Definition**. With this action you open the properties of the GetConnector. You uncheck the **Blocked** field. Are the blocked rows not visible in the view? Then click the gear wheel at the top right and click **Show blocked rows**.
*source: https://help.afas.nl/meldingen/NL/SE/99797.htm*
