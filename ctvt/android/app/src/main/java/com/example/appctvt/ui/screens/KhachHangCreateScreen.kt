package com.example.appctvt.ui.screens

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import com.example.appctvt.network.RetrofitClient
import com.example.appctvt.network.models.KhachHangRequest
import com.example.appctvt.network.models.KhachHangResponse
import com.example.appctvt.ui.components.AppScaffold
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

@Composable
fun KhachHangCreateScreen(
    navController: NavController
) {
    var maKh by remember { mutableStateOf("") }
    var tenKh by remember { mutableStateOf("") }
    var tenBietDanh by remember { mutableStateOf("") }
    var sdt by remember { mutableStateOf("") }
    var diaChi by remember { mutableStateOf("") }
    var mst by remember { mutableStateOf("") }

    var loading by remember { mutableStateOf(false) }
    var error by remember { mutableStateOf<String?>(null) }

    AppScaffold(
        title = "Thêm khách hàng",
        showBack = true,
        onBack = { navController.popBackStack() }
    ) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp)
        ) {

            OutlinedTextField(
                value = maKh,
                onValueChange = { maKh = it },
                label = { Text("Mã khách hàng") },
                modifier = Modifier.fillMaxWidth()
            )

            OutlinedTextField(
                value = tenKh,
                onValueChange = { tenKh = it },
                label = { Text("Tên khách hàng *") },
                modifier = Modifier.fillMaxWidth()
            )

            OutlinedTextField(
                value = tenBietDanh,
                onValueChange = { tenBietDanh = it },
                label = { Text("Tên gọi / biệt danh") },
                modifier = Modifier.fillMaxWidth()
            )

            OutlinedTextField(
                value = sdt,
                onValueChange = { sdt = it },
                label = { Text("Số điện thoại") },
                modifier = Modifier.fillMaxWidth()
            )

            OutlinedTextField(
                value = diaChi,
                onValueChange = { diaChi = it },
                label = { Text("Địa chỉ") },
                modifier = Modifier.fillMaxWidth()
            )

            OutlinedTextField(
                value = mst,
                onValueChange = { mst = it },
                label = { Text("Mã số thuế") },
                modifier = Modifier.fillMaxWidth()
            )

            if (error != null) {
                Text(
                    text = error!!,
                    color = MaterialTheme.colorScheme.error
                )
            }

            Button(
                onClick = {
                    if (tenKh.isBlank()) {
                        error = "Tên khách hàng không được để trống"
                        return@Button
                    }

                    loading = true
                    error = null

                    val request = KhachHangRequest(
                        ma_kh = maKh.ifBlank { null },
                        ten_kh = tenKh,
                        ten_khach_bi_danh = tenBietDanh.ifBlank { null },
                        sdt = sdt.ifBlank { null },
                        dia_chi = diaChi.ifBlank { null },
                        mst = mst.ifBlank { null }
                    )

                    RetrofitClient.apiService.createKhachHang(request)
                        .enqueue(object : Callback<KhachHangResponse> {

                            override fun onResponse(
                                call: Call<KhachHangResponse>,
                                response: Response<KhachHangResponse>
                            ) {
                                loading = false
                                if (response.isSuccessful) {
                                    navController.popBackStack()
                                } else {
                                    error = "Tạo khách hàng thất bại"
                                }
                            }

                            override fun onFailure(
                                call: Call<KhachHangResponse>,
                                t: Throwable
                            ) {
                                loading = false
                                error = "Lỗi kết nối server"
                            }
                        })
                },
                modifier = Modifier.fillMaxWidth(),
                enabled = !loading
            ) {
                Text(if (loading) "Đang lưu..." else "Lưu khách hàng")
            }
        }
    }
}
