---
layout: inner
title: 'Adapting Splotch for the TAO Pipeline'
date: 2018-02-26 13:20:00
tags: 
 - C++
 - Data Visualisation
lead_text: "Producing cosmological images via HPC"
categories: portfolio
permalink: /:categories/:title
project_link: portfolio/splotchTao

card_video: '../video/posts/sage.mp4'
feature_video: ../video/posts/taoFeature.mp4
link: https://github.com/splotchviz/splotch
link_type: github
link_text: Github
---

Working with the Centre for Astrophysics and Supercomputing at the Swinburne University of Technology in Melbourne Australia, as well as collaborating with persons at Swiss National Supercomputing Centre, I adapted the high performance volume rendering tool [Splotch](http://wwwmpa.mpa-garching.mpg.de/~kdolag/Splotch/) to work on the [gSTAR supercomputer](http://supercomputing.swin.edu.au/) for the purposes of the [Theoretical Astronomical Observatory (TAO)](https://tao.asvo.org.au/tao/). This work has formed the basis for a paper that was published at the [Astronomical Data Analysis Software and Systems (ADASS)](http://www.adass2016.inaf.it/index.php/participants-all/4-poster/226-ayling-elliott) 2016 conference. A link to the paper can be found [here](https://www.aspbooks.org/publications/521/600.pdf).

This work has a focus on optimisation whilst also adding functionality to automate parts of the Splotch software, with the aim of lowering the level of accessibility to produce the visualisation images. I also added support for HDF5 compound data.

This project formed part of my University dissertation which can be found [here](../documents/Dissertation.pdf).
