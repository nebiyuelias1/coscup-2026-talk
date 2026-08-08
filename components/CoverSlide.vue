<template>
  <div class="flex flex-col items-center justify-center h-auto my-auto px-4 py-2 text-center">
    <div class="flex items-center gap-2.5 mb-4 flex-wrap justify-center">
      <div class="title-chip">
        <img src="/coscup_logo.png" alt="COSCUP Logo" class="h-3.5 object-contain" />
        <span>COSCUP 2026</span>
      </div>
      <div class="title-chip flex items-center gap-1.5">
        <img src="/ruby_taiwan_logo.svg" alt="Ruby Taiwan Logo" class="h-4.5 object-contain" />
        <img src="/ruby_taiwan_logotype.svg" alt="Ruby Taiwan" class="h-3.5 object-contain filter invert brightness-200" />
      </div>
    </div>

    <h1 class="text-5xl font-extrabold tracking-tight mb-4 leading-tight">
      <template v-if="currentLang === 'zh'">
        使用 Rails 開發<br>
        <span class="text-red-500">
          Native 原生手機 App
        </span>
      </template>
      <template v-else>
        Building Native Mobile Apps<br>
        <span class="text-red-500">
          Using Rails
        </span>
      </template>
    </h1>

    <p class="text-xl text-slate-300 max-w-2xl mx-auto font-medium mb-8">
      {{ currentLang === 'zh' 
        ? '透過 Hotwire Native，直接將現有的 Web 應用發佈至 iOS 與 Android 平台' 
        : 'Ship iOS and Android from the app you already have — with Hotwire Native.' }}
    </p>

    <div class="flex items-center justify-center gap-3 text-sm font-semibold flex-wrap">
      <div class="flex items-center gap-2 bg-slate-900/80 px-4 py-2 rounded-xl border border-red-500/30">
        <span class="w-2.5 h-2.5 rounded-full bg-red-500 animate-pulse"></span>
        <span class="text-white">{{ currentLang === 'zh' ? '講者:' : 'Speaker:' }}</span>
        <span class="text-red-400 font-bold">Neba</span>
      </div>
      <div class="bg-slate-900/80 px-4 py-2 rounded-xl border border-slate-700 text-slate-300 font-mono text-xs flex items-center gap-1.5">
        <span>📅 Aug 8, 2026</span>
      </div>
      <div class="bg-slate-900/80 px-4 py-2 rounded-xl border border-slate-700 text-slate-300 font-mono text-xs flex items-center gap-1.5">
        <span>📍 {{ currentLang === 'zh' ? '台灣台北 台灣科技大學' : 'NTUST, Taipei, Taiwan' }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
