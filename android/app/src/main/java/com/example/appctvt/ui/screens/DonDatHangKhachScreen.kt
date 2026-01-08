package com.example.appctvt.ui.screens

import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.navigation.NavController
import com.example.appctvt.ui.components.AppScaffold

@Composable
fun DonDatHangKhachScreen(
    navController: NavController
) {
    AppScaffold(
        title = "Đơn đặt hàng khách",
        showBack = true,
        onBack = { navController.popBackStack() }
    ) {
        Text("Nội dung Đơn đặt hàng khách")
    }
}
