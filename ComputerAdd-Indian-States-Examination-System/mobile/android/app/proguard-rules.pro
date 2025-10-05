# Add project specific ProGuard rules here.
-keepattributes *Annotation*
-keepclassмembers class * {
    @android.webkit.JavascriptInterface <methods>;
}
-keep class com.computeradd.indianstates.models.** { *; }
