<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <meta charset="utf-8">
    <title>About</title>
  </head>
  <body>
    <header>
      Grafiek en plotprobeersels
    </header>
  </body>
  <div id="tester" style="width:600px;height:600px;"></div>
  <script>
  	TESTER = document.getElementById('tester');
  	Plotly.plot( TESTER, [{
  	x: [1, 2, 3, 4, 5],
  	y: [1, 2, 4, 8, 16] }], {
  	margin: { t: 0 } } );
  </script>
  <?php
  echo "php is cool en hopelijk werkt onze website"
  $txt = "Kaas"
  echo "ik hou van $txt "
  $command = escapeshellcmd('/usr/custom/test.py');
  $output = shell_exec($command);
  echo $output;

  ?>
</html>
<head>
</head>
