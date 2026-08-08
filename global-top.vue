<template>
  <div class="fixed top-3 right-4 z-50 flex items-center gap-2 pointer-events-auto">
    <select
      v-model="currentLang"
      class="bg-slate-900/90 text-white text-xs font-mono border border-red-500/40 rounded-lg px-2.5 py-1 shadow-xl focus:outline-none focus:border-red-500 cursor-pointer backdrop-blur-md hover:bg-slate-800 transition-colors"
    >
      <option value="en">🇺🇸 English</option>
      <option value="zh">🇹🇼 繁體中文</option>
    </select>
  </div>
</template>

<script setup>
import { currentLang } from './composables/useLang'
</script>
