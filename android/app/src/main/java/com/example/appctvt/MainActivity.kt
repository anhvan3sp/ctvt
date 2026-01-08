package com.example.appctvt

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import com.example.appctvt.network.RetrofitClient
import com.example.appctvt.ui.navigation.AppNavHost
import com.example.appctvt.ui.theme.AppCTVTTheme

class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        RetrofitClient.init(this)

        setContent {
            AppCTVTTheme {
                AppNavHost()
            }
        }
    }
}
