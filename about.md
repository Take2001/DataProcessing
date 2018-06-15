---
layout: default
title: Dataprocessing Groep24
---
<head>
      <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>

## Grafiek en plotprobeersels
hier zie je een aantal grafieken  die duidelijke correlatie geven tussen voedselprijs en hoeveelheid vluchtelingen.

<div id="tester" style="width:600px;height:600px;"></div>
<script>
	TESTER = document.getElementById('tester');
	Plotly.plot( TESTER, [{
	x: [1, 2, 3, 4, 5],
	y: [1, 2, 4, 8, 16] }], {
	margin: { t: 0 } } );
</script>
<div id="tester2" style="width:600px;height:600px;"></div>
<script>
var trace1 = {
  x: [1, 2, 3, 4],
  y: [10, 15, 13, 17],
  mode: 'markers'
};

var trace2 = {
  x: [2, 3, 4, 5],
  y: [16, 5, 11, 10],
  mode: 'lines'
};

var trace3 = {
  x: [1, 2, 3, 4],
  y: [12, 9, 15, 12],
  mode: 'lines+markers'
};

var data = [ trace1, trace2, trace3 ];

var layout = {};

Plotly.newPlot('myDiv', data, layout);
</script>
