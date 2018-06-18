---
layout: default
title: Dataprocessing Groep24
---
<head>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
## Grafiekprobeersels en geleuter
hallo beste meneertj/mevrouwtj ik zie dat je mijn grafieken hebt gevonden ik weet nog niet hoe je onze database/scripts koppelt aan deze grafiek noch hoe ik het interactive kan maken. Ik zal mijn best doen om dit wel te kunnen en dan zien we hopelijk resultaat. groetjs
<div id="tester" style="width:600px;height:600px;"></div>
<script>
	TESTER = document.getElementById('tester');
	Plotly.plot( TESTER, [{
	x: [1, 2, 3, 4, 5],
	y: [1, 2, 4, 8, 16] }], {
	margin: { t: 0 } } );
</script>

<div id="myDiv" style="width:600px;height:600px;"></div>
<script>
var trace1 = {
  x: [2000, 2002, 2003, 2004, 2005, 2006, 2007, 2008],
  y: [10, 15, 20, 30, 40, 50, 70, 100],
  mode: 'lines',
  name: 'Lines
};

var trace2 = {
  x: [1, 2, 3, 4],
  y: [16, 5, 11, 9],
  mode: 'lines+markers',
  name: 'Scatter and Lines'
};

var layout = {
  title: 'Mooien grafyk',
  xaxis: {
    title: 'Jaren'
  },
  yaxis: {
    title: 'Chilisaus op kapsalon'
  }
};

var data = [trace1, trace2];

Plotly.newPlot('myDiv', data);
</script>
