package com.example.appctvt.ui.screens

import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.navigation.NavController
import com.example.appctvt.ui.components.AppScaffold

@Composable
fun HoaDonBanScreen(
    navController: NavController
) {
    AppScaffold(
        title = "Hóa đơn bán",
        showBack = true,
        onBack = { navController.popBackStack() }
    ) {
        Text("Nội dung Hóa đơn bán")
    }
}
