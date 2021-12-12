
<div class='panel panel-border panel-success'>
                                    <div class='panel-heading'> 
                                        <h3 class='panel-title'><i class='fa fa-user-plus'></i> Tambah Admin</h3> 
                                    </div>  <div class='panel-body'> <?php
if(isset($_POST['username'])){
$passasli=$_POST['password'];
$password=md5($passasli);
$username		= $_POST['username'];
$nama		= $_POST['nama'];
$nik		= $_POST['nik'];
$cekuser = mysql_query("SELECT * FROM pengguna WHERE username = '$username'");  
  if(mysql_num_rows($cekuser) <> 0) {
 echo "ERROR : Username sudah terdaftar";
  }else{
	
	$input = mysql_query("INSERT INTO pengguna VALUES('$nama','$username', '$password', 'Administrator', '$nik')") or die(mysql_error());
	if($input){
		
		echo '<div class="alert alert-success alert-dismissable">
                                <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button><h4><b>Tambah Admin Berhasil!</b></h4>';		//Pesan jika proses tambah sukses
		echo '
		============================<Br>
		<b>Info Admin</b><br>
		Id Admin : <b>'.$nik.'</b><br>
		Nama : <b>'.$nama.'</b><br>
		============================<Br>
		<b>Info Akun </b><br>
		Username : <b>'.$username.'</b><br>
		Password : <b>'.$passasli.'</b><br>
		</div>
		
		';	
		
	}else{
		
		echo 'Gagal menambahkan data! ';	
		echo '<a href="tambah.php">Kembali</a>';	
		
	}
  }
}
?>
									<form method="post">
																		 <div class="form-group">
                                                <label>Id Admin</label>
                                                <input type="text" class="form-control" name="nik" placeholder="Masukan Id Admin" required>
                                            </div>
									 <div class="form-group">
                                                <label>Nama</label>
                                                <input type="text" class="form-control" name="nama" placeholder="Masukan Nama Admin" required>
                                            </div>

 <div class="form-group">
                                                <label>Username</label>
                                                <input type="text" class="form-control" name="username" placeholder="Masukan Username" required>
                                            </div>
 <div class="form-group">
                                                <label>Password</label>
                                                <input type="password" class="form-control" name="password" placeholder="Masukan Password" required>
                                            </div>
<button type="submit" class="btn btn-success waves-effect waves-light">Tambah</button>
</form>
                                     </div>
									 
          </div>
		 