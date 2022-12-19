<?php
$input = file('input.txt');

//part one

//variable declarations
$epsilon = ''; 
$gamma = ''; 
$rows = count($input); 
$cols = count(str_split($input[0]));
$array = []; 
//turn binary string lines into arrays, stripping any non-numeric characters
$c = 0;
foreach ($input as $line) {
	$digits = str_split(preg_replace('/[^0-9.]+/', '', $line));
	$array[$c] = $digits;
	$c++;
}
//count 0s and 1s per column
function most_common($j, $rows, $array) {
	$c0 = 0;
	$c1 = 0;
		for ($i = 0; $i < $rows-1; $i++) {
			if ($array[$i][$j] == 0) {
				$c0++;
			}
			else {
				$c1++;
			}
		}

	if ($c0 > $c1 ){
		return 0;
	}
	else {
		return 1;
	}
}
	//append the correct number/char to gamma and epsilon depending on the most common digit in this column
for ($j = 0; $j < $cols-1; $j++) {
	if ( !most_common($j, $rows, $array) ) {
		$gamma.='0';
		$epsilon.='1';
	}
	else {
		$gamma.='1';
		$epsilon.='0';
	}

}
//convert gamma and epsilon into decimals
$g = bindec($gamma);
$e = bindec($epsilon);
print($g * $e); 

?>