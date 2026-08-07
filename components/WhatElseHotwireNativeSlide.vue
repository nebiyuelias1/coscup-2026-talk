<template>
  <div class="what-else-hotwire-native-slide w-full my-auto flex flex-col justify-center text-left">
    
    <!-- Header Badge -->
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">⚡ Capabilities</span>
      <span class="text-xs font-mono text-slate-400">Beyond WebViews</span>
    </div>

    <!-- Main Title -->
    <h2 class="text-3xl font-black tracking-tight text-white mb-5">
      What Else Can You Do With <span class="text-red-500">Hotwire Native?</span>
    </h2>

    <!-- 4 Balanced Cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      
      <!-- 1. Native Bridge Components -->
      <div class="bg-slate-900/90 border border-red-500/30 rounded-2xl p-4 shadow-xl flex items-start gap-3.5">
        <span class="text-2xl shrink-0">🌉</span>
        <div class="space-y-1">
          <div class="flex items-center justify-between gap-2">
            <h3 class="text-sm font-bold text-white m-0">Native Bridge Components</h3>
            <span class="text-[10px] font-mono font-bold text-red-400 bg-red-950/80 px-2 py-0.5 rounded border border-red-800/60 shrink-0">
              Strada
            </span>
          </div>
          <p class="text-xs text-slate-300 leading-snug m-0">
            Control native Swift & Kotlin UI elements directly from HTML <code class="text-red-300">data-bridge</code> attributes.
          </p>
        </div>
      </div>

      <!-- 2. Push Notifications & Deep Links -->
      <div class="bg-slate-900/90 border border-amber-500/30 rounded-2xl p-4 shadow-xl flex items-start gap-3.5">
        <span class="text-2xl shrink-0">🔔</span>
        <div class="space-y-1">
          <div class="flex items-center justify-between gap-2">
            <h3 class="text-sm font-bold text-white m-0">Push Notifications & Deep Links</h3>
            <span class="text-[10px] font-mono font-bold text-amber-400 bg-amber-950/80 px-2 py-0.5 rounded border border-amber-800/60 shrink-0">
              APNs / FCM
            </span>
          </div>
          <p class="text-xs text-slate-300 leading-snug m-0">
            Handle APNs & FCM notifications natively and route deep links straight to Rails controllers.
          </p>
        </div>
      </div>

      <!-- 3. Instant OTA Deployments -->
      <div class="bg-slate-900/90 border border-emerald-500/30 rounded-2xl p-4 shadow-xl flex items-start gap-3.5">
        <span class="text-2xl shrink-0">🚀</span>
        <div class="space-y-1">
          <div class="flex items-center justify-between gap-2">
            <h3 class="text-sm font-bold text-white m-0">Instant OTA Deployments</h3>
            <span class="text-[10px] font-mono font-bold text-emerald-400 bg-emerald-950/80 px-2 py-0.5 rounded border border-emerald-800/60 shrink-0">
              Zero Queue
            </span>
          </div>
          <p class="text-xs text-slate-300 leading-snug m-0">
            Update copy, layouts, and feature bug fixes on your server live — with zero App Store review delays.
          </p>
        </div>
      </div>

      <!-- 4. Full Native Escape Hatch -->
      <div class="bg-slate-900/90 border border-cyan-500/30 rounded-2xl p-4 shadow-xl flex items-start gap-3.5">
        <span class="text-2xl shrink-0">📱</span>
        <div class="space-y-1">
          <div class="flex items-center justify-between gap-2">
            <h3 class="text-sm font-bold text-white m-0">100% Native Fallback</h3>
            <span class="text-[10px] font-mono font-bold text-cyan-400 bg-cyan-950/80 px-2 py-0.5 rounded border border-cyan-800/60 shrink-0">
              SwiftUI / Compose
            </span>
          </div>
          <p class="text-xs text-slate-300 leading-snug m-0">
            Need heavy camera filters or custom SDKs? Effortlessly drop down to full native Swift or Kotlin screens.
          </p>
        </div>
      </div>

    </div>

  </div>
</template>

<script setup>
</script>
