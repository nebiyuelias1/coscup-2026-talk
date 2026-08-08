<template>
  <div class="mobile-requirement-slide w-full my-auto flex flex-col justify-center text-left">
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">{{ currentLang === 'zh' ? '⚠️ 抉擇時刻' : '⚠️ The Dilemma' }}</span>
      <span class="text-xs font-mono text-slate-400">{{ currentLang === 'zh' ? '跨平台挑戰' : 'Cross-Platform Challenge' }}</span>
    </div>

    <h2 class="text-3xl font-black tracking-tight text-white mb-5">
      <template v-if="currentLang === 'zh'">
        我們需要 <span class="text-red-500">Mobile Apps</span>... 該怎麼做？ 🤔
      </template>
      <template v-else>
        We Need <span class="text-red-500">Mobile Apps</span>... Now What? 🤔
      </template>
    </h2>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-5">
      <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-2">
        <span class="text-2xl">🌐</span>
        <h3 class="text-sm font-bold text-amber-400 m-0">Option A: PWA</h3>
        <p class="text-xs text-slate-300 m-0">
          {{ currentLang === 'zh' ? '快速但受限：缺乏 App Store 上架與完整原生能力。' : 'Fast but limited: Lacks App Store presence & full native capabilities.' }}
        </p>
      </div>

      <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-2">
        <span class="text-2xl">⚛️</span>
        <h3 class="text-sm font-bold text-cyan-400 m-0">Option B: React Native / Flutter</h3>
        <p class="text-xs text-slate-300 m-0">
          {{ currentLang === 'zh' ? '強大但高昂：需重寫所有前端與 logic，維護雙重 Codebase。' : 'Powerful but expensive: Duplicate business logic & components.' }}
        </p>
      </div>

      <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-2">
        <span class="text-2xl">🍎🤖</span>
        <h3 class="text-sm font-bold text-purple-400 m-0">Option C: Swift & Kotlin</h3>
        <p class="text-xs text-slate-300 m-0">
          {{ currentLang === 'zh' ? '頂級體驗但成本巨大：需招募 2 個獨立的原生開發團隊。' : 'Top experience but maximum cost: Requires 2 dedicated native teams.' }}
        </p>
      </div>
    </div>

    <div class="p-3 bg-red-950/30 border border-red-500/30 rounded-xl text-xs flex items-center justify-between">
      <span class="text-slate-200">
        💡 <strong>{{ currentLang === 'zh' ? '挑戰關鍵:' : 'The Key Challenge:' }}</strong> {{ currentLang === 'zh' ? '如何在保留 Web 開發優勢的同時交付原生 App 體驗。' : 'Shipping native iOS & Android apps without sacrificing developer productivity.' }}
      </span>
    </div>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
