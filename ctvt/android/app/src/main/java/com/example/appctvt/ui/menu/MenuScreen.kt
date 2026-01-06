package com.example.appctvt.ui.menu

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import com.example.appctvt.ui.components.AppScaffold

@Composable
fun MenuScreen(
    navController: NavController
) {
    AppScaffold(
        title = "Menu",
        showBack = false,
        onBack = {}
    ) {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .verticalScroll(rememberScrollState())
                .padding(8.dp)
        ) {

            MenuSection("Bán hàng") {
                MenuItem("Hóa đơn bán") {
                    navController.navigate("hoa_don_ban")
                }
                MenuItem("Đơn đặt hàng khách") {
                    navController.navigate("don_dat_hang_khach")
                }
            }

            MenuSection("Nhập hàng") {
                MenuItem("Hóa đơn nhập") {
                    navController.navigate("hoa_don_nhap")
                }
                MenuItem("Đơn đặt hàng nhà cung cấp") {
                    navController.navigate("don_dat_hang_ncc")
                }
            }

            MenuSection("Thu – Chi") {
                MenuItem("Phiếu thu") {
                    navController.navigate("phieu_thu")
                }
                MenuItem("Phiếu chi") {
                    // làm sau
                }
            }

            MenuSection("Quỹ") {
                MenuItem("Quỹ nhân viên") { }
                MenuItem("Quỹ công ty") { }
            }

            MenuSection("Công nợ") {
                MenuItem("Công nợ khách hàng") { }
                MenuItem("Công nợ nhà cung cấp") { }
            }

            MenuSection("Kho") {
                MenuItem("Tồn kho") { }
                MenuItem("Vỏ bình – nợ vỏ") { }
            }

            MenuSection("Danh mục") {
                MenuItem("Khách hàng") {
                    navController.navigate("khach_hang")
                }
                MenuItem("Nhân viên") { }
            }

            MenuSection("Thuế – VAT") {
                MenuItem("VAT đầu vào") { }
                MenuItem("VAT đầu ra") { }
                MenuItem("Nhập VAT khách không tên") { }
                MenuItem("Báo cáo VAT") { }
                MenuItem("Xuất Excel VAT") { }
            }

            MenuSection("Báo cáo") {
                MenuItem("Doanh thu hôm nay") { }
                MenuItem("Lãi hôm nay") { }
                MenuItem("Doanh thu theo tháng") { }
            }
        }
    }
}
