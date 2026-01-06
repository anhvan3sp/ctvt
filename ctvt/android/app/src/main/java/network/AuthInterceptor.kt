package com.example.appctvt.network

import okhttp3.Interceptor
import okhttp3.Response

class AuthInterceptor(
    private val tokenManager: TokenManager
) : Interceptor {

    override fun intercept(chain: Interceptor.Chain): Response {
        val originalRequest = chain.request()

        val token = tokenManager.getToken()

        // Nếu chưa có token (chưa login) → gửi request bình thường
        if (token.isNullOrEmpty()) {
            return chain.proceed(originalRequest)
        }

        // Có token → gắn Authorization header
        val newRequest = originalRequest.newBuilder()
            .addHeader("Authorization", "Bearer $token")
            .build()

        return chain.proceed(newRequest)
    }
}
