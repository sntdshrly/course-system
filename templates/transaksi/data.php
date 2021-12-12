<div class='panel panel-border panel-success'>
                                    <div class='panel-heading'> 
                                        <h3 class='panel-title'><i class='fa fa-clock-o'></i> Riwayat Transaksi</h3> 
                                    </div>  <div class='panel-body'> 
                                <table id='datatable' class='table table-hover'>
                                    <thead>
                                        <tr>
										<th><i class='icon-terminal'></i> No</th>
										<th><i class='icon-signal'></i> Siswa</th>
										<th><i class='icon-terminal'></i> Bahasa</th>
											<th><i class='icon-signal'></i> Tarif</th>
											<th><i class='icon-signal'></i> Total Waktu</th>
											<th><i class='icon-signal'></i> Tanggal Transaksi</th>
											<th><i class='icon-signal'></i> Tanggal Kursus</th>

											<th><i class='icon-signal'></i> Kuitansi</th>
                                        </tr>
                                    </thead>
                                    <tbody>
									<?php
							$i=1;
							$tp=mysql_query("SELECT * FROM transaksi WHERE pengguna='$usr' ORDER BY tgl_transaksi");
							while($r=mysql_fetch_array($tp)){
							?>
							<tr>
							 <td><?php echo $i;?></td>
				
                                    <td><?php echo $r['konsumen'];?></td>
                                    <td><?php echo $r['jenis'];?></td>
									<td><?php echo'Rp.' . number_format( $r['tarif'], 0 , '' , '.' ) . ',-'?></td>
									<td><?php echo $r['berat']?> Jam</td>
									<td><?php echo TanggalIndo($r['tgl_transaksi']);?></td>
									<td><?php echo TanggalIndo($r['tgl_ambil']);?></td>
									<td><a href="transaksi/kwitansi.php?id=<?php echo $r['id'];?>" target="_blank">Lihat Kuitansi</a></td>
                                    
							</tr>
							<?php $i=$i+1;?>
							<?php } ?>
							</tbody>
                        </table>
                                    </div>
          </div>