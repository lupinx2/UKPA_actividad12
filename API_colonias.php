<?php
// CONFIGURAR DE ACUERDO A SU SERVIDOR
$servername = "localhost";
$username = "UKINO_API";
$password = "";
$dbname = "Sonora";
$conn = new mysqli($servername, $username, $password, $dbname);


if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// checamos el codigo postal en la DB
$cp = $_GET['cp'];
$sql = "SELECT colonia FROM codigos_postales WHERE cp = $cp";
$result = $conn->query($sql);

// si no hay resultados, evitamos un error, pero avisamos al frontend
if ($result->num_rows > 0) {
    $rows = array();
    while($row = $result->fetch_assoc()) {
        $rows[] = $row;
    }
    echo json_encode($rows);
} else {
    echo "Zero";
}

$conn->close();
?>