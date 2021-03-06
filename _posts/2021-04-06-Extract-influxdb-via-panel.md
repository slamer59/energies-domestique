---
keywords: fastai
description: An easy to use blogging platform with extra features for <a href="https://jupyter.org/">Jupyter Notebooks</a>.
title: Introducing fastpages with hvplot
toc: true 
badges: true
comments: true
sticky_rank: 1
author: Thomas PEDOT
image: images/diagram.png
categories: [fastpages, jupyter]
nb_path: _notebooks/2021-04-06-Extract influxdb via panel.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2021-04-06-Extract influxdb via panel.ipynb
-->

<div class="container" id="notebook-container">
        
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">query_api</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">query_api</span><span class="p">()</span>
<span class="n">query</span> <span class="o">=</span> <span class="s1">&#39;&#39;&#39;from(bucket: &quot;energie&quot;)</span>
<span class="s1">  |&gt; range(start: -1d)</span>
<span class="s1">  |&gt; filter(fn: (r) =&gt; r[&quot;_measurement&quot;] == &quot;solarmanpv&quot;)</span>
<span class="s1">  |&gt; filter(fn: (r) =&gt; r[&quot;_field&quot;] == &quot;Courant DC PV1&quot; or r[&quot;_field&quot;] == &quot;Courant DC PV2&quot;)</span>
<span class="s1">  </span>
<span class="s1">  |&gt; yield(name: &quot;mean&quot;)&#39;&#39;&#39;</span>
<span class="n">result</span> <span class="o">=</span> <span class="n">client</span><span class="o">.</span><span class="n">query_api</span><span class="p">()</span><span class="o">.</span><span class="n">query_data_frame</span><span class="p">(</span><span class="n">org</span><span class="o">=</span><span class="n">ORG</span><span class="p">,</span> <span class="n">query</span><span class="o">=</span><span class="n">query</span><span class="p">)</span>
<span class="n">result</span><span class="o">.</span><span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;result&#39;</span><span class="p">,</span> <span class="s1">&#39;table&#39;</span><span class="p">,</span> <span class="s1">&#39;start&#39;</span><span class="p">,</span> <span class="s1">&#39;stop&#39;</span><span class="p">,</span> <span class="s1">&#39;time&#39;</span><span class="p">,</span> <span class="s1">&#39;value&#39;</span><span class="p">,</span> <span class="s1">&#39;field&#39;</span><span class="p">,</span>
       <span class="s1">&#39;measurement&#39;</span><span class="p">,</span> <span class="s1">&#39;host&#39;</span><span class="p">,</span> <span class="s1">&#39;topic&#39;</span><span class="p">]</span>
<span class="n">result</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">


<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>result</th>
      <th>table</th>
      <th>start</th>
      <th>stop</th>
      <th>time</th>
      <th>value</th>
      <th>field</th>
      <th>measurement</th>
      <th>host</th>
      <th>topic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>mean</td>
      <td>0</td>
      <td>2021-04-18 11:52:40.951513+00:00</td>
      <td>2021-04-19 11:52:40.951513+00:00</td>
      <td>2021-04-18 11:52:52.548802+00:00</td>
      <td>6.55</td>
      <td>Courant DC PV1</td>
      <td>solarmanpv</td>
      <td>telegraf1</td>
      <td>SolarmanPV/realTimeDataImp</td>
    </tr>
    <tr>
      <th>1</th>
      <td>mean</td>
      <td>0</td>
      <td>2021-04-18 11:52:40.951513+00:00</td>
      <td>2021-04-19 11:52:40.951513+00:00</td>
      <td>2021-04-18 11:53:11.810644+00:00</td>
      <td>6.55</td>
      <td>Courant DC PV1</td>
      <td>solarmanpv</td>
      <td>telegraf1</td>
      <td>SolarmanPV/realTimeDataImp</td>
    </tr>
    <tr>
      <th>2</th>
      <td>mean</td>
      <td>0</td>
      <td>2021-04-18 11:52:40.951513+00:00</td>
      <td>2021-04-19 11:52:40.951513+00:00</td>
      <td>2021-04-18 11:53:32.162518+00:00</td>
      <td>6.55</td>
      <td>Courant DC PV1</td>
      <td>solarmanpv</td>
      <td>telegraf1</td>
      <td>SolarmanPV/realTimeDataImp</td>
    </tr>
    <tr>
      <th>3</th>
      <td>mean</td>
      <td>0</td>
      <td>2021-04-18 11:52:40.951513+00:00</td>
      <td>2021-04-19 11:52:40.951513+00:00</td>
      <td>2021-04-18 11:53:50.681999+00:00</td>
      <td>6.55</td>
      <td>Courant DC PV1</td>
      <td>solarmanpv</td>
      <td>telegraf1</td>
      <td>SolarmanPV/realTimeDataImp</td>
    </tr>
    <tr>
      <th>4</th>
      <td>mean</td>
      <td>0</td>
      <td>2021-04-18 11:52:40.951513+00:00</td>
      <td>2021-04-19 11:52:40.951513+00:00</td>
      <td>2021-04-18 11:54:10.911786+00:00</td>
      <td>6.55</td>
      <td>Courant DC PV1</td>
      <td>solarmanpv</td>
      <td>telegraf1</td>
      <td>SolarmanPV/realTimeDataImp</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
    {% endraw %}
{% include influxdb_hvplot.html %}
<div class="cell border-box-sizing text_cell rendered"><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">

</div>
</div>
</div>
</div>
 

