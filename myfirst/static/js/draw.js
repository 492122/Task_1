anychart.onDocumentLoad(function() {
  // create chart and set data
  var chart = anychart.column([
    ["Winter", 2],
    ["Spring", 7],
    ["Summer", 6],
    ["Fall", 10]
  ]);
  // set chart title
  chart.title("AnyChart Basic Sample");
  // set chart container and draw
  chart.container("container").draw();
});