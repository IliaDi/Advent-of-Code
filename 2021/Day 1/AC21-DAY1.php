<?php

$data = file('input.txt');
$counter = 0;
$prev_measurement = data[0];

//part one

foreach ($data as $measurement) {
	if ($prev_measurement < $measurement){
		$counter+=1;
		$prev_measurement = $measurement;

	}	
		
}

echo "part one ".$."\n";

//part two

$c = 0;
$prev_measurement = $data[0] + $data[1] + $data[2];

$counter = 0;

while (($c+2) < count($data)){
	$current_measurement = $data[$c] + $data[$c+1] + $data[$c+2];
	if ($prev_measurement < $current_measurement){
		$counter+=1
	}
	$c+=1;
	$prev_measurement = $current_measurement;
}

echo "part two ".$counter."\n";



?>





