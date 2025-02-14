<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>MidTerm</title>
</head>

<body>
	<h1>Welcome to a mid term</h1>
	<?php
        // Fetch EC2 instance public IP
        $ip = file_get_contents("http://checkip.amazonaws.com/");
        echo "<p>Welcome! Your EC2 instance IP is: <strong>$ip</strong></p>";
    ?>
	<p>Enter two numbers and select the operation.</p>
	<form action="process_math.php" method="post">
		<label>Number #1: </label>
		<input type="number" name="num1" required>
		<br>
		<label>Number #2: </label>
		<input type="number" name="num2" required>
		<br>
		<select name="operation" id="operation">
			<option value="Addition">Additon</option>
			<option value="Subtraction">Substraction</option>
			<option value="Multiplication">Multiplication</option>
			<option value="Division">Division</option>
		</select>
		<br>
		<input type="submit" value="Calculate">
	</form>
</body>

</html>
