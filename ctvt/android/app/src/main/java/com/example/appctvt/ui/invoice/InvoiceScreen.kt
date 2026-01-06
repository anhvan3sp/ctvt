package com.example.appctvt.ui.invoice

import android.util.Log
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.example.appctvt.network.RetrofitClient
import com.example.appctvt.network.models.KhachHangResponse
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

@Composable
fun InvoiceScreen() {

    var customerText by remember { mutableStateOf("") }
    val customers = remember { mutableStateListOf<KhachHangResponse>() }
    var customerExpanded by remember { mutableStateOf(false) }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {

        OutlinedTextField(
            value = customerText,
            onValueChange = { text ->
                customerText = text
                if (text.isNotEmpty()) {
                    RetrofitClient.apiService
                        .searchKhachHang(text)
                        .enqueue(object : Callback<List<KhachHangResponse>> {

                            override fun onResponse(
                                call: Call<List<KhachHangResponse>>,
                                response: Response<List<KhachHangResponse>>
                            ) {
                                customers.clear()
                                customers.addAll(response.body() ?: emptyList())
                                customerExpanded = customers.isNotEmpty()
                            }

                            override fun onFailure(
                                call: Call<List<KhachHangResponse>>,
                                t: Throwable
                            ) {
                                Log.e("API", "Search khách hàng lỗi", t)
                            }
                        })
                } else {
                    customers.clear()
                    customerExpanded = false
                }
            },
            label = { Text("Khách hàng") },
            modifier = Modifier.fillMaxWidth()
        )

        DropdownMenu(
            expanded = customerExpanded,
            onDismissRequest = { customerExpanded = false }
        ) {
            customers.forEach { kh ->
                DropdownMenuItem(
                    text = { Text(kh.ten_kh) },
                    onClick = {
                        customerText = kh.ten_kh
                        customerExpanded = false
                    }
                )
            }
        }
    }
}
