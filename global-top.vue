<template>
  <div class="fixed top-3 right-4 z-50 flex items-center gap-2 pointer-events-auto">
    <!-- Light / Dark Mode Toggle Button -->
    <button
      @click="toggleTheme()"
      type="button"
      :title="isDark ? 'Switch to Light Mode' : 'Switch to Dark Mode'"
      class="theme-toggle-btn text-xs font-mono border border-red-500/40 rounded-lg px-2.5 py-1 shadow-xl focus:outline-none focus:border-red-500 cursor-pointer backdrop-blur-md transition-all flex items-center gap-1.5 font-bold select-none"
    >
      <span v-if="isDark" class="text-amber-400 flex items-center gap-1">
        <span>☀️</span>
        <span class="hidden sm:inline">Light</span>
      </span>
      <span v-else class="text-indigo-400 flex items-center gap-1">
        <span>🌙</span>
        <span class="hidden sm:inline">Dark</span>
      </span>
    </button>

    <!-- Language Selector -->
    <select
      v-model="currentLang"
      class="lang-select text-xs font-mono border border-red-500/40 rounded-lg px-2.5 py-1 shadow-xl focus:outline-none focus:border-red-500 cursor-pointer backdrop-blur-md transition-colors"
    >
      <option value="en">🇺🇸 English</option>
      <option value="zh">🇹🇼 繁體中文</option>
    </select>
  </div>
</template>

<script setup>
import { currentLang } from './composables/useLang'
import { isDark, toggleTheme } from './composables/useTheme'
</script>

