<?php
//part two

//read input file

$input = file_get_contents("input.txt");
$handle = fopen("input.txt", "r");

if ($handle) {

  $data_array = [];
  while (($data = fgets($handle)) !== false) {
    $data = preg_replace("/\r|\n/", "", $data);
    $data_array[] = $data;
  }

  fclose($handle);
  $rows = count($data_array);
  $columns = strlen($data_array[0]);
  $oxygen_generator_r = oxygen_generator_rating(0, $data_array, $columns);
  $oxygen_generator_r_decimal = bindec($oxygen_generator_r); 
  print($oxygen_generator_r_decimal."\n");
  $co2_scrubber_r = co2_scrubber_rating(0, $data_array, $columns); 
  $co2_scrubber_r_decimal = bindec($co2_scrubber_r);
  print($co2_scrubber_r_decimal."\n");
  print($oxygen_generator_r_decimal * $co2_scrubber_r_decimal); 
}

//index = column, length = length of each binary measurement, data = the array with the measurements

function oxygen_generator_rating(int $index, array $data, int $length){
    $zero_array = [];
    $one_array = [];
    for ($i = 0; $i < count($data); $i++) {
      if ($data[$i][$index]) {
        $one_array[] = $data[$i];
      } else {
        $zero_array[] = $data[$i];
      }
    }
    if (count($data) == 1) {
        return $data[0];
    }
    //if there are 2 left, the number of occurencies are equal, so the last column determines the winner 
    else if (count($data) == 2) {
      if ($data[0][($length - 1)] == 1) {
          return $data[0];
        } 
      else {
        return $data[1];
      } 
    }
    else {
      $index++;
      if (count($zero_array) <= count($one_array)) {
        return oxygen_generator_rating($index, $one_array, $length);
      } else if (count($zero_array) > count($one_array)) {
        return oxygen_generator_rating($index, $zero_array, $length);
      }
    }
}

function co2_scrubber_rating(int $index, array $data, int $length){
    $zero_array = [];
    $one_array = [];
    for ($i = 0; $i < count($data); $i++) {
      if ($data[$i][$index]) {
        $one_array[] = $data[$i];
      } else {
        $zero_array[] = $data[$i];
      }
    }
    if (count($data) == 1) {
        return $data[0];
    }
    else if (count($data) == 2) {
      if ($data[0][($length - 1)] == 0) {
          return $data[0];
        } 
      else {
        return $data[1];
      } 
    }
    else {
      $index++;
      if (count($zero_array) <= count($one_array)) {
        return co2_scrubber_rating($index, $zero_array, $length);
      } else if (count($zero_array) > count($one_array)) {
        return co2_scrubber_rating($index, $one_array, $length);
      }
    }
}

?>