# MythicalArcOps

## Description

A Use Case for Edge Computing is about these capabilities:

- Signal acquisition
- Signal Contextualization
- Signal Processing
- Signal Action
- Signal Visualization
- Signal Storage
- Signal Learning

Many of the Digital Manufacturing or general Edge use cases tend to solve for this idea of acquisition of multiple signals and processing it for Actions.  Model based Controllers using the Edge for decision making.

As the Signal(s) converge to an answer (decision) it is then delivered to required systems for further processing.

Examples:
a.  Condition based process control. A signal from a sensor is acquired and processed to determine if the process is in control or out of control.  If out of control, then the signal is sent to a controller to make a decision to take an action to bring the process back in control.  The controller is either PLC, DCS, or a Model based controller running on the Edge. A combination of using OPC Publisher for acquiring the signals, and using Edge processing modules to contextualize, process and send to the controller for action or detect and raise an alert, etc. integrate to other systems for further processing.

b. Vision based Quality process control. A signal from a vision system is acquired and processed to determine if the product is good or bad.  If bad, then the signal is sent to a controller to make a decision to take an action.  The controller is either PLC, DCS, or a Model based controller running at the Edge. A combination of using AKRI brokers with ONVIF connectivity or RTSP or native drivers for acquiring  multi media signals, and using Edge processing modules to contextualize, process and send to the controller for action or detect and raise an alert, etc. integrate to other systems for further processing.


To package these digital solutions (use cases - Acquisition to Actions to Learning), we  need to be able to define the following:

- Solution definition : A DAG that describes the main trunk of the Signal pipeline - Acquisition to Actions - the Outcome needed at the Edge.
- Solution deployment : A set of artifacts to be deployed to the Edge to operate the solution.

This specific work is about Solution deployment. 

## Solution Deployment 

A path from individual artifact builds to gitops based deployment to Edge devices.

This repo has 1 application that is built and deployed to Edge devices.

- application level CI, CD [ unittest, build, test, publish]
- solution level CI, CD [ unittest, build, test, publish]

A demonstration of artifact(CI,CD),Solution Packaging, Release using Azure Services :
Azure DevOps
Azure Arc enabled Kubernetes
Azure KeyVault
GitHub
