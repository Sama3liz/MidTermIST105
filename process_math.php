<?php

$a = escapeshellarg($_POST['num1']);
$b = escapeshellarg($_POST['num2']);
$c = escapeshellarg($_POST['operation']);

$command = escapeshellcmd("python3 math_operations.py $a $b $c");
$output = shell_exec($command);

echo "<h2>Calculation Results:</h2>";
echo "<div>$output</div>";

?>
