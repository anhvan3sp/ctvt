package com.example.appctvt.network

data class HoaDonBanRequest(
    val ngay: String,          // yyyy-MM-dd
    val ma_kh: String,
    val ma_sp: String,
    val ma_kho: String,
    val so_luong: Double,
    val gia: Double,
    val tien_mat: Double,
    val tien_ck: Double,
    val no_lai: Double
)