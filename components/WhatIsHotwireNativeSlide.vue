<template>
  <div class="what-is-hotwire-native-slide w-full my-auto flex flex-col justify-center text-left">
    
    <!-- Header Badge -->
    <div class="flex justify-between items-center mb-2">
      <span class="hotwire-badge font-bold">⚡ Core Philosophy</span>
      <span class="text-xs font-mono text-slate-400">The Hybrid Architecture</span>
    </div>

    <!-- Main Title -->
    <h2 class="text-3xl font-black tracking-tight text-white mb-6">
      What is <span class="text-red-500">Hotwire Native?</span>
    </h2>

    <!-- 3 Pillars Cards Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      
      <!-- Pillar 1 Card: Thin Native Shell -->
      <div class="bg-slate-900/90 border border-red-500/30 rounded-2xl p-5 shadow-xl space-y-3 relative overflow-hidden flex flex-col justify-between">
        <div class="flex items-center gap-2 text-red-400 font-bold text-base">
          <span>📱 Thin Native Shell</span>
        </div>
        <p class="text-xs text-slate-300 leading-relaxed m-0">
          Native Swift & Kotlin container managing top navbars, bottom tab bars, and push notifications.
        </p>
        <div class="pt-2.5 border-t border-slate-800 text-xs font-mono text-red-300 font-bold">
          iOS & Android Shell
        </div>
      </div>

      <!-- Pillar 2 Card: Renders Web Views -->
      <div class="bg-slate-900/90 border border-amber-500/30 rounded-2xl p-5 shadow-xl space-y-3 relative overflow-hidden flex flex-col justify-between">
        <div class="flex items-center gap-2 text-amber-400 font-bold text-base">
          <span>🌐 Renders Web Views</span>
        </div>
        <p class="text-xs text-slate-300 leading-relaxed m-0">
          Reuses 100% of your existing Rails ERB views and business logic with zero code duplication.
        </p>
        <div class="pt-2.5 border-t border-slate-800 text-xs font-mono text-amber-300 font-bold">
          Single Majestic Monolith
        </div>
      </div>

      <!-- Pillar 3 Card: Drops to Native UI -->
      <div class="bg-slate-900/90 border border-emerald-500/30 rounded-2xl p-5 shadow-xl space-y-3 relative overflow-hidden flex flex-col justify-between">
        <div class="flex items-center gap-2 text-emerald-400 font-bold text-base">
          <span>⚡ Native Where It Matters</span>
        </div>
        <p class="text-xs text-slate-300 leading-relaxed m-0">
          Seamlessly drop down to 100% native screens for camera, biometrics, or heavy custom components.
        </p>
        <div class="pt-2.5 border-t border-slate-800 text-xs font-mono text-emerald-300 font-bold">
          Frictionless Native Fallback
        </div>
      </div>

    </div>

  </div>
</template>

<script setup>
</script>
