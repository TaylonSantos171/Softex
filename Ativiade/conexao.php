<?php 
$hostname='localhost';
$usuario='root';
$senha='root';
$banco='profpaulo';


$conexao=mysqli_connect( $hostname, $usuario, $senha, $banco);
if(!$conexao){
        die("houve um erro: ".msqli_connect_error());
}


?>