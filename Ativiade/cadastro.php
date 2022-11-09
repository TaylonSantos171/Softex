<?php
include ("conexao.php");

$nome=$_POST['nome'];
$curso=$_POST['curso'];

$sql="INSERT INTO alunos(nome, curso)
            VALUES  ('$nome', '$curso')";

if (mysqli_query($conexao, $sql)){
    echo "usuário cadastrado com sucesso";
}
else{
    echo "erro" .mysqli_connect_error ($conexao);
}
mysqli_close($conexao);
?>