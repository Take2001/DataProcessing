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
