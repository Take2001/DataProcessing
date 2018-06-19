---
layout: default
title: Dataprocessing Groep24
---
<head>
<style>

.node {
  stroke: #fff;
  stroke-width: 1.5px;
}

.link {
  stroke: #999;
  stroke-opacity: .6;
}

</style>
</head>
## Grafiekprobeersels en geleuter
hallo beste meneertj/mevrouwtj ik zie dat je mijn grafieken hebt gevonden ik weet nog niet hoe je onze database/scripts koppelt aan deze grafiek noch hoe ik het interactive kan maken. Ik zal mijn best doen om dit wel te kunnen en dan zien we hopelijk resultaat. groetjs
<script src="https://d3js.org/d3.v4.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/4.11.0/d3.min.js"></script>
<script src="https://d3js.org/d3-selection-multi.v1.min.js"></script>
<script>
const w = 400, h = 250;
const padding = 4;
const data = [50,100,150,200,250,130,210,30,170];

let svg = d3.select('body')
            .append('svg')
            .attr('width', w)
            .attr('height', h);

svg.selectAll('rect')
  .data(data)
  .enter()
    .append('rect')
    .attrs({
      x: (d, i) => i * (w / data.length),
      y: d => h - d,
      width: w / data.length - padding,
      height: d => d,
      fill: 'green'
});

svg.selectAll('text')
  .data(data)
  .enter()
    .append('text')
    .text((d) => d)
    .attrs({
      x: (d,i) => i * (w / data.length) + (w / data.length - padding) / 2,
      y: (d) => h - d + 20
});
</script>
