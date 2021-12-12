<?php
$aksi="user/prosesk.php";
                    $p=isset($_GET['aksi'])?$_GET['aksi']:null;
                    switch($p){
default:
echo "<div class='panel panel-border panel-success'>
                                    <div class='panel-heading'> 
                                        <h3 class='panel-title'><i class='fa fa-list'></i> Olah Admin</h3> 
                                    </div>  <div class='panel-body'> 
		 <hr>
                                <table id='datatable' class='table table-hover'>
                                    <thead>
                                        <tr>
										<th><i class='icon-terminal'></i> No.</th>
									<th><i class='icon-terminal'></i> Id Admin</th>
                                            <th><i class='icon-terminal'></i> Nama</th>
                                            <th><i class='icon-time'></i> Username</th>
										<th><i class='icon-chevron-right'></i> Aksi</th>
                                        </tr>
                                    </thead>
                                    <tbody>";
							$i=1;
							$tp=mysql_query("SELECT * FROM pengguna WHERE level='Administrator' ORDER BY nik");
							while($r=mysql_fetch_array($tp)){
						    //$hargaa = $r['harga'];
                             echo"<tr>
							  <td>$i</td>
							   <td>$r[nik]</td>
							    <td>$r[nama]</td>
								 <td>$r[username]</td>
                                    <td><a class='btn btn-success' href='?p=olahk&aksi=edit&nik=$r[nik]'><i class='icon-edit'></i>Edit</a>
									 <a class='btn btn-danger' href='$aksi?act=hapus&nik=$r[nik]'><i class='icon-trash'></i>Hapus</td>
                                    
                                </tr>";
								$i=$i+1;
							}
                               
                                        
                        echo"</tbody>
                        </table>
                                     </div><!-- /.box-body -->
          </div><!-- /.box -->   ";    

break;
case "edit":
	$edit = mysql_query("SELECT * FROM pengguna WHERE nik='$_GET[nik]'");
    $r    = mysql_fetch_array($edit);
echo "<form method='post' action='user/prosesk.php?act=update' enctype='multipart/form-data'>";
echo "<div class='panel panel-border panel-primary'>
                                    <div class='panel-heading'> 
                 <h3 class='panel-title'><i class='fa fa-list'></i> Edit Admin</h3> 
                                    </div>  <div class='panel-body'> 
					<input type='hidden' name='nik' value='$r[nik]'>
					 <div class='control-group'>
					   <div class='form-group'>
                            <label>NIK</label>
                            <div class='span9'><input class='form-control' value='$r[nik]'  type='text' name='nik' disabled/></div>
                        </div>
					   <div class='form-group'>
                            <label>Nama</label>
                            <div class='span9'><input class='form-control' value='$r[nama]'  type='text' name='nama' /></div>
                        </div>						
					   <div class='form-group'>
                            <label>Username</label>
                            <div class='span9'><input class='form-control' size='16' type='text' value='$r[username]' name='username' disabled/></div>
                        </div>
											   
					<Br>

			<input type='submit' class='btn btn-success' value='Update'> <a class='btn btn-danger' href='?p=olahk'>Batal</a>
		  </form>
		</div> 
		                  
		                  
                    </div></div>
					
		";
echo "";
break;
			}
?>    
</body>

</html>