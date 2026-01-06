package com.example.appctvt.network

import android.content.Context
import okhttp3.OkHttpClient
import okhttp3.logging.HttpLoggingInterceptor
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object RetrofitClient {

    private const val BASE_URL = "http://192.168.1.119:8000/"

    private val loggingInterceptor = HttpLoggingInterceptor().apply {
        level = HttpLoggingInterceptor.Level.BODY
    }

    lateinit var apiService: ApiService
        private set

    fun init(context: Context) {

        val tokenManager = TokenManager(context)

        val client = OkHttpClient.Builder()
            .addInterceptor(AuthInterceptor(tokenManager))
            .addInterceptor(loggingInterceptor)
            .build()

        val retrofit = Retrofit.Builder()
            .baseUrl(BASE_URL) // ✅ ĐÚNG CÚ PHÁP
            .addConverterFactory(GsonConverterFactory.create()) // ✅ ĐÚNG CÚ PHÁP
            .client(client)
            .build()

        apiService = retrofit.create(ApiService::class.java)
    }
}
