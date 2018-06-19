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
<button type="button" onclick="myFunction()">try</button>
<p id="demo2"></p>
<script>
function myFunction(){
	var person = prompt("Hier met die voornaam", "LOSER");

	if (person =! null){
		document.getElementById("demo2").innerHTML=
		"Hello " + person + "! wassbrackin B";
	}
}
</script>

<script src="http://d3js.org/d3.v3.min.js"></script>
<script src="http://d3js.org/topojson.v1.min.js"></script>
<script>
var width = 1000, height = 728;

var svg = d3.select("body").append("svg")
  .attr({ width: width, height: height });
var mainGroup = svg.append("g");
mainGroup.style({ stroke: "white", "stroke-width": "2px", "stroke-opacity": 0.0 });

var projection = d3.geo.mercator();

var path = d3.geoPath().projection(null);

var url = 'https://gist.githubusercontent.com/bricedev/3905007f1794b0cb0bcd/raw/ad5c995f6990f7c3c7fad5c6206bc6fd5462f1fb/africa.json';
d3.json(url, function (error, africa) {
  var countries = topojson.feature(africa, africa.objects.countries).features;
  var neighbors = topojson.neighbors(africa.objects.countries.geometries);

  var color = d3.scale.category20();
  mainGroup.selectAll("path", "countries")
      .data(countries)
      .enter().append("path")
      .attr("d", path)
      .style("fill", function (d, i) {
          return color(d.color = d3.max(neighbors[i],
              function (n) { return countries[n].color; }) + 1 | 0);
      });

  mainGroup.selectAll("path")
      .on("mouseover", function () {
          console.log("mouseover");
          d3.select(this).style("stroke-opacity", 1.0);
      });
  mainGroup.selectAll("path")
      .on("mouseout", function () {
          d3.select(this).style("stroke-opacity", 0.0);
      });
});

</script>
