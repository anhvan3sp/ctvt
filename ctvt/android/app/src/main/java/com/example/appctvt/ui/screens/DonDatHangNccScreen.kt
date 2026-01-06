package com.example.appctvt.ui.screens

import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.navigation.NavController
import com.example.appctvt.ui.components.AppScaffold

@Composable
fun DonDatHangNccScreen(
    navController: NavController
) {
    AppScaffold(
        title = "Đơn đặt hàng nhà cung cấp",
        showBack = true,
        onBack = { navController.popBackStack() }
    ) {
        Text("Nội dung Đơn đặt hàng nhà cung cấp")
    }
}
