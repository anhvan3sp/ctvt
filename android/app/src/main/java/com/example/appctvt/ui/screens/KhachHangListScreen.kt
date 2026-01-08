package com.example.appctvt.ui.screens

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import com.example.appctvt.ui.components.AppScaffold

@Composable
fun KhachHangListScreen(
    navController: NavController
) {
    AppScaffold(
        title = "Khách hàng",
        showBack = true,
        onBack = { navController.popBackStack() }
    ) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(16.dp)
        ) {

            Button(
                onClick = {
                    navController.navigate("khach_hang_create")
                },
                modifier = Modifier.fillMaxWidth()
            ) {
                Text("+ Thêm khách hàng")
            }

            Spacer(modifier = Modifier.height(16.dp))

            Text("Danh sách khách hàng (chưa có dữ liệu)")
        }
    }
}
