package com.example.appctvt.network

import com.example.appctvt.network.models.*
import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.http.Query

interface ApiService {

    // =======================
    // AUTH / LOGIN
    // =======================
    @POST("auth/login")
    fun login(
        @Body request: LoginRequest
    ): Call<LoginResponse>

    // =======================
    // PRODUCT
    // =======================
    @GET("products")
    fun getProducts(): Call<List<Product>>

    // =======================
    // KHÁCH HÀNG (THEO SWAGGER)
    // =======================

    // Lấy danh sách khách hàng
    @GET("khach-hang/khach-hang/")
    fun getKhachHang(): Call<List<KhachHangResponse>>

    // Tìm kiếm khách hàng
    @GET("khach-hang/khach-hang/search")
    fun searchKhachHang(
        @Query("keyword") keyword: String
    ): Call<List<KhachHangResponse>>

    // Tạo khách hàng mới
    @POST("khach-hang/khach-hang/")
    fun createKhachHang(
        @Body request: KhachHangRequest
    ): Call<KhachHangResponse>

    // =======================
    // HÓA ĐƠN BÁN
    // =======================
    @POST("hoa_don_ban")
    fun createHoaDonBan(
        @Body request: HoaDonBanRequest
    ): Call<Void>
}
