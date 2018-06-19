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
<div id='d3div' width="960" height="500"></svg>
<script src="https://d3js.org/d3.v4.min.js"></script>
<script>

var width = $("#d3div").width(),
    height = 500;

var color = d3.scale.category20();

var force = d3.layout.force()
    .charge(-120)
    .linkDistance(30)
    .size([width, height]);

var svg = d3.select("#d3div").append("svg")
    .attr("width", width)
    .attr("height", height);

d3.json("../../../../scripts/miserables.json", function(error, graph) {
  if (error) throw error;

  force
      .nodes(graph.nodes)
      .links(graph.links)
      .start();

  var link = svg.selectAll(".link")
      .data(graph.links)
    .enter().append("line")
      .attr("class", "link")
      .style("stroke-width", function(d) { return Math.sqrt(d.value); });

  var node = svg.selectAll(".node")
      .data(graph.nodes)
    .enter().append("circle")
      .attr("class", "node")
      .attr("r", 5)
      .style("fill", function(d) { return color(d.group); })
      .call(force.drag);

  node.append("title")
      .text(function(d) { return d.name; });

  force.on("tick", function() {
    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node.attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
  });
});

</script>
