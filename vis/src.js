/* This doesn't handle resizes very well. */
var width = window.innerWidth;
var height = window.innerHeight; 

var svg = d3.select("#d3").append("svg")
  .attr('width', width)
  .attr('height', height)
  .call(d3.zoom().on("zoom", function () {
      svg.attr("transform", d3.event.transform)
  }))
  .append("g")

var color = d3.scaleOrdinal(d3.schemeCategory20);

var simulation = d3.forceSimulation()
    .force("link", d3.forceLink().id(function(d) { return d.id; }).distance(50))
    .force("charge", d3.forceManyBody().strength(-100).distanceMax(400))
    .force("center", d3.forceCenter(width / 2, height / 2))


d3.json("data.json", function(error, graph) {
  if (error) throw error;
  
  let ids = {}
  let count = 0
  graph.nodes.forEach(function(d) {
    ids[d.id] =  count;
    count += 1;
    d.degree = 0;
  });

  graph.links.forEach(function(d) {
    graph.nodes[ids[d.source]].degree += 1;
    graph.nodes[ids[d.target]].degree += 1;
  });

  var link = svg.append("g")
      .attr("class", "links")
    .selectAll("line")
    .data(graph.links)
    .enter().append("line")
      .attr("stroke-width", function(d) { return 3; });


  var node = svg.append("g")
      .attr("class", "nodes")
    .selectAll("g")
    .data(graph.nodes)
    .enter().append("g")
    
  var circles = node.append("circle")
      .attr("r", function (d) { return 5+d.degree})
      .attr("fill", function(d) { return color(d.degree); })
      .call(d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended));

  var lables = node.append("text")
      .text(function(d) {
        return d.id;
      })
      .attr('x', 0)
      .attr('y', 10);

  node.append("title")
      .text(function(d) { return d.id; });

  simulation
      .nodes(graph.nodes)
      .on("tick", ticked);

  simulation.force("link")
      .links(graph.links);

  function ticked() {
    link
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node
        .attr("transform", function(d) {
          return "translate(" + d.x + "," + d.y + ")";
        })
  }
});

function dragstarted(d) {
  if (!d3.event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(d) {
  d.fx = d3.event.x;
  d.fy = d3.event.y;
}

function dragended(d) {
  if (!d3.event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}
