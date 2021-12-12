<?php
			include "../koneksi.php";
                    $p=isset($_GET['act'])?$_GET['act']:null;
                    switch($p){
                        default:

	                            break;
                        case "hapus":
mysql_query("DELETE FROM pengguna WHERE nik='$_GET[nik]'");
  header('location:../index.php?p=olahk');
	                            break;
                        case "update":
    mysql_query("UPDATE pengguna SET nama='$_POST[nama]' WHERE nik='$_POST[nik]'");
							 
  header('location:../index.php?p=olahk');  
	}
                    ?>
      