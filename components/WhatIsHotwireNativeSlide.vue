<template>
  <div class="what-is-hotwire-slide w-full my-auto flex flex-col justify-center text-left">
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">{{ currentLang === 'zh' ? '🚀 核心解答' : '🚀 The Solution' }}</span>
      <span class="text-xs font-mono text-slate-400">Hybrid Magic</span>
    </div>

    <h2 class="text-3xl font-black tracking-tight text-white mb-5">
      <template v-if="currentLang === 'zh'">
        什麼是 <span class="text-red-500">Hotwire Native？</span> 📱
      </template>
      <template v-else>
        What is <span class="text-red-500">Hotwire Native?</span> 📱
      </template>
    </h2>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-5">
      <div class="bg-slate-900/90 border border-red-500/40 rounded-2xl p-5 shadow-xl space-y-3">
        <span class="text-3xl">🌐</span>
        <h3 class="text-base font-bold text-white m-0">
          {{ currentLang === 'zh' ? '伺服器渲染 Web 頁面' : 'Server-Rendered Web' }}
        </h3>
        <p class="text-xs text-slate-300 leading-relaxed m-0">
          {{ currentLang === 'zh' ? '在 Rails 端處理大部分頁面與邏輯，更新即時生效，免去 App Store 重新審核！' : 'Render 90% of screens on the server. Instant updates without App Store reviews.' }}
        </p>
      </div>

      <div class="bg-slate-900/90 border border-emerald-500/40 rounded-2xl p-5 shadow-xl space-y-3">
        <span class="text-3xl">⚡</span>
        <h3 class="text-base font-bold text-white m-0">
          {{ currentLang === 'zh' ? '原生導覽與外殼' : 'Native Shell & Navigation' }}
        </h3>
        <p class="text-xs text-slate-300 leading-relaxed m-0">
          {{ currentLang === 'zh' ? '原生導覽列、Tab Bar、推送通知與相機存取，帶來 100% 原生手機質感。' : 'Native navigation bars, tabs, push notifications, and camera access for native UX.' }}
        </p>
      </div>
    </div>

    <div class="p-3 bg-slate-950 border border-slate-800 rounded-xl text-xs flex items-center justify-between">
      <span class="text-slate-300">
        💡 <strong>{{ currentLang === 'zh' ? '最佳組合:' : 'Best of Both Worlds:' }}</strong> {{ currentLang === 'zh' ? 'Web 的開發速度 + 原生 App 的優質體驗。' : 'Web speed of development combined with native user experience.' }}
      </span>
    </div>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
