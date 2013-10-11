<?php

function pickMovie($movieArray) {
	$randomKey = rand(0, sizeof($movieArray) - 1);
	echo $movieArray[$randomKey];
}

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

pickMovie($movies);
