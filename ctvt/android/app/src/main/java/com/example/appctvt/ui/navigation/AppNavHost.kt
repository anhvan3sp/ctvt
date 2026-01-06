package com.example.appctvt.ui.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import com.example.appctvt.ui.menu.MenuScreen
import com.example.appctvt.ui.screens.*

@Composable
fun AppNavHost() {

    val navController = rememberNavController()

    NavHost(
        navController = navController,
        startDestination = "menu"
    ) {

        composable("menu") {
            MenuScreen(navController)
        }

        composable("hoa_don_ban") {
            HoaDonBanScreen(navController)
        }

        composable("hoa_don_nhap") {
            HoaDonNhapScreen(navController)
        }

        composable("phieu_thu") {
            PhieuThuScreen(navController)
        }

        composable("don_dat_hang_khach") {
            DonDatHangKhachScreen(navController)
        }

        composable("don_dat_hang_ncc") {
            DonDatHangNccScreen(navController)
        }

        composable("khach_hang") {
            KhachHangListScreen(navController)
        }

        composable("khach_hang_create") {
            KhachHangCreateScreen(navController)
        }
    }
}
