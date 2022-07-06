---
layout: inner
title: OrreyVk
permalink: /portfolio/orreyVk
---

## Orrey Vk

<iframe width="100%" height="auto" src="https://www.youtube.com/watch?v=TtgKBqT9Ksk" frameborder="0" allowfullscreen></iframe>

A solar system simulation written for Vulkan in C++. This is an updated Vulkan version of a similar project I created in OpenGL (found [here](orreygl)).

My main aim for this project was to implement real time gravity calculations on a compute shader, whilst drawing all objects via a single draw call. My system (with a 2080ti) can manage ~500,000 objects whilst maintaining >30fps- with the bottleneck being the graphics draw.

This project implements features such as compute shaders, instancing, texture arrays, mipmapping, uniform and storage buffers, multisampling, specialization constants, query pools etc.

Distances are in astronomical units, scaled down. Masses are in solar masses. The size of the sun is not to scale and has been scaled down to make viewing planets easier. Moon distances have also been exaggerated for effect.

Texture images from: https://www.solarsystemscope.com/textures/

<a href="https://github.com/EllAyling/OrreyVK" class="project-link"><button class="btn btn-default btn-lg"><i class="fa fa-github fa-lg"></i>Github</button></a>
 