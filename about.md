---
layout: default
title: Dataprocessing Groep24
---
<head>
<style>
.line {
	fill: none;
	stroke: steelblue;
	stroke-width: 2px;
}
</style>
</head>
<script src="https://d3js.org/d3.v4.min.js"></script>
## Grafiekprobeersels en geleuter
hallo beste meneertj/mevrouwtj ik zie dat je mijn grafieken hebt gevonden ik weet nog niet hoe je onze database/scripts koppelt aan deze grafiek noch hoe ik het interactive kan maken. Ik zal mijn best doen om dit wel te kunnen en dan zien we hopelijk resultaat. groetjs
update: d3 is een waardeloos hoopje code en ik snap niet dat iemand dat zou gebruiken. moraal is laag maar de zoektocht gaat door.

<script>
// set the dimensions and margins of the graph
var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

// parse the date / time
var parseTime = d3.timeParse("%d-%b-%y");

// set the ranges
var x = d3.scaleTime().range([0, width]);
var y = d3.scaleLinear().range([height, 0]);

// define the line
var valueline = d3.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.close); });

// append the svg object to the body of the page
// appends a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

// Get the data
d3.csv("testdata_website.csv", function(error, data) {
  if (error) throw error;

  // format the data
  data.forEach(function(d) {
      d.date = parseTime(d.date);
      d.close = +d.close;
  });

  // Scale the range of the data
  x.domain(d3.extent(data, function(d) { return d.date; }));
  y.domain([0, d3.max(data, function(d) { return d.close; })]);

  // Add the valueline path.
  svg.append("path")
      .data([data])
      .attr("class", "line")
      .attr("d", valueline);

  // Add the X Axis
  svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

  // Add the Y Axis
  svg.append("g")
      .call(d3.axisLeft(y));

});

</script>
<p id="demo">Ik oefen javascript</p>
<button type="button" onclick='document.getElementById("demo").innerHTML = "Ik stel mijn taken uit"'>KLIKKEN SNEL</button>
<button type="button" onclick="document.getElementById('demo').style.fontSize='35px'">verander grootte</button>
<button type="button" onclick="document.getElementById('demo').style.color='red'">verander kleur</button>
<button type="button" onlick="document.getElementById('demo').src='https://www.goedkoopsteautoverzekering.net/wp-content/themes/goedkoopsteautoverzekering/assets/img/happy-man.png'">blije man</button>
<img id="myImage" src="https://www.goedkoopsteautoverzekering.net/wp-content/themes/goedkoopsteautoverzekering/assets/img/happy-man.png" style="width:400px">
<button type="button" onclick="document.getElementById('demo').src='http://www.stickpng.com/assets/images/58909b725236a4e0f6e2f976.png'">boze man</button>
