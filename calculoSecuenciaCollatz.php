<?php 

$numero = $_GET["numero"]; 


function calculo($numero){
	if(is_numeric($numero)){
		$numEntrada = $numero;
		while ($numero != 1) {
		
			if ($numero % 2 == 0){
				$numero = $numero /2;
				}
			else{
				$numero = ($numero * 3) + 1;
				}

			$numeros[] = $numero;
			}

		$json = array('numero' => $numEntrada, "secuencia" => $numeros );

		$respuesta = json_encode($json);
		return $respuesta;
		
		
	}else{
		$nota =  array('numero' => " ");
		$respuesta =  json_encode($nota);
		return $respuesta;
	
	}
}

echo calculo($numero);
?>
