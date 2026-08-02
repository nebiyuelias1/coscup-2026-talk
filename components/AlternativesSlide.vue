<template>
  <div class="alternatives-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge">⚖️ Trade-off Analysis</span>
      <span class="text-xs font-mono text-slate-400">Evaluating Current Options</span>
    </div>

    <h2 class="text-2xl font-black tracking-tight text-white mb-4 text-left">
      Alternative Mobile Approaches & <span class="text-transparent bg-clip-text bg-gradient-to-r from-red-400 via-amber-300 to-red-500">Their Limitations</span>
    </h2>

    <!-- 3 Column Layout for PWAs, Native (Swift/Kotlin), React Native -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
      <!-- 1. PWA Card -->
      <div class="bg-slate-900/90 border border-red-500/30 rounded-2xl p-4 text-left shadow-xl relative overflow-hidden flex flex-col justify-between">
        <div class="absolute -right-8 -top-8 w-24 h-24 bg-red-600/10 rounded-full blur-2xl pointer-events-none"></div>

        <div>
          <!-- Header -->
          <div class="flex items-center justify-between border-b border-slate-800 pb-2 mb-3">
            <div class="flex items-center gap-1.5">
              <span class="text-lg">🌐</span>
              <h3 class="text-sm font-bold text-white m-0">PWAs</h3>
            </div>
            <span class="text-[9px] bg-red-950 text-red-300 px-1.5 py-0.5 rounded border border-red-800 font-mono">
              ⚠️ High Friction
            </span>
          </div>

          <!-- Simplified Points -->
          <ul class="space-y-2.5 text-xs text-slate-300 pl-0 list-none mb-3">
            <li class="flex items-start gap-1.5">
              <span class="text-red-400 font-bold shrink-0">❌</span>
              <span><strong>Low Adoption:</strong> Users search App Stores, not web shortcuts.</span>
            </li>
            <li class="flex items-start gap-1.5">
              <span class="text-red-400 font-bold shrink-0">❌</span>
              <span><strong>Flaky Behavior:</strong> Unreliable push & session storage on iOS Safari.</span>
            </li>
            <li class="flex items-start gap-1.5">
              <span class="text-red-400 font-bold shrink-0">❌</span>
              <span><strong>No App Stores:</strong> Zero presence on iOS App Store & Google Play.</span>
            </li>
          </ul>
        </div>

        <div class="p-2 bg-slate-950/80 rounded-lg border border-red-500/20 text-[10px] font-mono text-red-300">
          Verdict: Weak user reach & retention
        </div>
      </div>

      <!-- 2. Separate Native Apps (Swift & Kotlin) -->
      <div class="bg-slate-900/90 border border-purple-500/30 rounded-2xl p-4 text-left shadow-xl relative overflow-hidden flex flex-col justify-between">
        <div class="absolute -right-8 -top-8 w-24 h-24 bg-purple-600/10 rounded-full blur-2xl pointer-events-none"></div>

        <div>
          <!-- Header -->
          <div class="flex items-center justify-between border-b border-slate-800 pb-2 mb-3">
            <div class="flex items-center gap-1.5">
              <span class="text-lg">📱</span>
              <h3 class="text-sm font-bold text-white m-0">Native Apps</h3>
              <span class="text-[9px] text-slate-400 font-mono">(Swift / Kotlin)</span>
            </div>
            <span class="text-[9px] bg-purple-950 text-purple-300 px-1.5 py-0.5 rounded border border-purple-800 font-mono">
              🔴 High Overhead
            </span>
          </div>

          <!-- Simplified Points -->
          <ul class="space-y-2.5 text-xs text-slate-300 pl-0 list-none mb-3">
            <li class="flex items-start gap-1.5">
              <span class="text-purple-400 font-bold shrink-0">❌</span>
              <span><strong>3 Codebases:</strong> Rails + Swift (iOS) + Kotlin (Android).</span>
            </li>
            <li class="flex items-start gap-1.5">
              <span class="text-purple-400 font-bold shrink-0">❌</span>
              <span><strong>Tripled Team:</strong> Requires dedicated iOS & Android engineers.</span>
            </li>
            <li class="flex items-start gap-1.5">
              <span class="text-purple-400 font-bold shrink-0">❌</span>
              <span><strong>Duplicated Logic:</strong> Business logic written 3x; review queue per edit.</span>
            </li>
          </ul>
        </div>

        <div class="p-2 bg-slate-950/80 rounded-lg border border-purple-500/20 text-[10px] font-mono text-purple-300">
          Verdict: Tripled cost & slow velocity
        </div>
      </div>

      <!-- 3. React Native Card -->
      <div class="bg-slate-900/90 border border-amber-500/30 rounded-2xl p-4 text-left shadow-xl relative overflow-hidden flex flex-col justify-between">
        <div class="absolute -right-8 -top-8 w-24 h-24 bg-amber-600/10 rounded-full blur-2xl pointer-events-none"></div>

        <div>
          <!-- Header -->
          <div class="flex items-center justify-between border-b border-slate-800 pb-2 mb-3">
            <div class="flex items-center gap-1.5">
              <span class="text-lg">⚛️</span>
              <h3 class="text-sm font-bold text-white m-0">React Native</h3>
            </div>
            <span class="text-[9px] bg-amber-950 text-amber-300 px-1.5 py-0.5 rounded border border-amber-800 font-mono">
              📦 Ecosystem Tax
            </span>
          </div>

          <!-- Simplified Points -->
          <ul class="space-y-2.5 text-xs text-slate-300 pl-0 list-none mb-3">
            <li class="flex items-start gap-1.5">
              <span class="text-amber-400 font-bold shrink-0">⚠️</span>
              <span><strong>JS Ecosystem Friction:</strong> Forces Rails teams into npm & Redux.</span>
            </li>
            <li class="flex items-start gap-1.5">
              <span class="text-amber-400 font-bold shrink-0">⚠️</span>
              <span><strong>API Tax:</strong> Must write, version, and sync JSON endpoints.</span>
            </li>
            <li class="flex items-start gap-1.5">
              <span class="text-amber-400 font-bold shrink-0">⚠️</span>
              <span><strong>Ignores Server HTML:</strong> Throws away existing Rails views & Turbo.</span>
            </li>
          </ul>
        </div>

        <div class="p-2 bg-slate-950/80 rounded-lg border border-amber-500/20 text-[10px] font-mono text-amber-300">
          Verdict: Heavy API & state sync tax
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>
