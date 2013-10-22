<?php

function fib($n) {
	if ($n == 0) {
		return 0;
	} elseif ($n == 1) {
		return 1;
	}
	else {
		return fib($n-1) + fib($n-2);
	}
}

function findMax($arr) {
	$max = False;
	foreach ($arr as $val) {
		if ($val > $max) {
			$max = $val;
		}
	}
	return $max;
}

function iterativeFib($n) {
	$x = 0;
	$y = 1;
	$temp = NULL;
	if ($n == 0) {
		return $x;
	} elseif ($n == 1) {
		return $y;
	}
	else {
		for ($i = 0; $i < $n - 1; $i++) {
			$temp = $x + $y;
			$x = $y;
			$y = $temp;
		}
		return $y;
	}
}

function pickMovie($movieArray) {
	$randomKey = rand(0, sizeof($movieArray) - 1);
	echo $movieArray[$randomKey];
}

echo "\n";

echo fib(8);

echo "\n";

echo iterativeFib(8);

echo "\n";

/*pickMovie(array("Hercules", "101 Dalmations", "JungleBook"));

echo "\n";

$blankLine = false;
$movies = array();

while (!$blankLine) {
	$movie = readline("Movie: ");
	if ($movie) {
		$movies[] = $movie;
	} else {
		$blankLine = true;
	}
}
*/
function reverseArray($arr) {
	$newArr = array();
	foreach ($arr as $item) {
		$newArr = array_merge(array($item), $newArr);
	}
	return $newArr;
}

function reverseArray2($arr) {
	for ($i=0; $i < count($arr) / 2; $i++) {
		$temp = $arr[$i];
		$arr[$i] = $arr[count($arr) - 1 - $i];
		$arr[count($arr) - 1 - $i] = $temp;
	}
	return $arr;
}

var_dump(reverseArray2(array("Hercules", "101 Dalmations", "JungleBook", "One more time")));

?>
